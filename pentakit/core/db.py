"""
PentaKit — MongoDB Persistence Layer
All scan data, findings, CVE cache and history stored here.
"""

from datetime import datetime, timezone
from typing import Optional
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.collection import Collection
from rich.console import Console

console = Console()

MONGO_URI = "mongodb://localhost:27017"
DB_NAME   = "pentakit"


class Database:
    def __init__(self, uri: str = MONGO_URI):
        try:
            self.client = MongoClient(uri, serverSelectionTimeoutMS=3000)
            self.client.server_info()          # Trigger connection
            self.db = self.client[DB_NAME]
            self._setup_indexes()
            console.print("[bold green]✅  MongoDB connected[/bold green]")
        except Exception as e:
            console.print(f"[bold yellow]⚠️   MongoDB not available: {e}[/bold yellow]")
            console.print("[yellow]   Results will not be persisted.[/yellow]")
            self.db = None

    def _setup_indexes(self):
        """Create indexes and TTL on cve_cache."""
        if self.db is None:
            return
        # cve_cache — TTL of 7 days
        self.db.cve_cache.create_index(
            "fetched_at",
            expireAfterSeconds=604800   # 7 days
        )
        # Common query indexes
        self.db.vulnerabilities.create_index([("target", ASCENDING), ("severity", DESCENDING)])
        self.db.scans.create_index([("target", ASCENDING), ("timestamp", DESCENDING)])
        self.db.osint_results.create_index("target", unique=False)

    @property
    def available(self) -> bool:
        return self.db is not None

    # ── Scans ────────────────────────────────────────────────
    def save_scan(self, scan_data: dict) -> Optional[str]:
        if not self.available:
            return None
        scan_data["timestamp"] = datetime.now(timezone.utc)
        result = self.db.scans.insert_one(scan_data)
        return str(result.inserted_id)

    def get_scan(self, scan_id: str) -> Optional[dict]:
        if not self.available:
            return None
        from bson import ObjectId
        return self.db.scans.find_one({"_id": ObjectId(scan_id)})

    def list_scans(self, target: str = None, limit: int = 20) -> list:
        if not self.available:
            return []
        query = {"target": target} if target else {}
        cursor = self.db.scans.find(query).sort("timestamp", DESCENDING).limit(limit)
        return list(cursor)

    # ── Vulnerabilities ──────────────────────────────────────
    def save_vulnerability(self, vuln: dict) -> Optional[str]:
        if not self.available:
            return None
        vuln.setdefault("status", "pending")
        vuln.setdefault("found_at", datetime.now(timezone.utc))
        result = self.db.vulnerabilities.insert_one(vuln)
        return str(result.inserted_id)

    def update_vuln_status(self, vuln_id: str, status: str):
        """status: pending | reported | confirmed | false_positive | fixed"""
        if not self.available:
            return
        from bson import ObjectId
        self.db.vulnerabilities.update_one(
            {"_id": ObjectId(vuln_id)},
            {"$set": {"status": status, "updated_at": datetime.now(timezone.utc)}}
        )

    def get_vulns(self, target: str = None, severity: str = None,
                  status: str = None, vuln_type: str = None) -> list:
        if not self.available:
            return []
        query = {}
        if target:   query["target"]   = target
        if severity: query["severity"] = severity
        if status:   query["status"]   = status
        if vuln_type:query["type"]     = vuln_type
        return list(self.db.vulnerabilities.find(query).sort("found_at", DESCENDING))

    # ── CVE Cache ────────────────────────────────────────────
    def get_cve(self, cve_id: str) -> Optional[dict]:
        if not self.available:
            return None
        return self.db.cve_cache.find_one({"cve_id": cve_id})

    def save_cve(self, cve_data: dict):
        if not self.available:
            return
        cve_data["fetched_at"] = datetime.now(timezone.utc)
        self.db.cve_cache.update_one(
            {"cve_id": cve_data["cve_id"]},
            {"$set": cve_data},
            upsert=True
        )

    # ── OSINT ────────────────────────────────────────────────
    def save_osint(self, target: str, data: dict) -> Optional[str]:
        if not self.available:
            return None
        data["target"]    = target
        data["timestamp"] = datetime.now(timezone.utc)
        result = self.db.osint_results.insert_one(data)
        return str(result.inserted_id)

    def get_osint(self, target: str) -> list:
        if not self.available:
            return []
        return list(self.db.osint_results.find({"target": target}).sort("timestamp", DESCENDING))

    # ── Targets ──────────────────────────────────────────────
    def upsert_target(self, domain: str, data: dict):
        if not self.available:
            return
        data["domain"]     = domain
        data["last_seen"]  = datetime.now(timezone.utc)
        self.db.targets.update_one({"domain": domain}, {"$set": data}, upsert=True)

    def list_targets(self) -> list:
        if not self.available:
            return []
        return list(self.db.targets.find().sort("last_seen", DESCENDING))

    # ── Compare scans ────────────────────────────────────────
    def compare_scans(self, scan_id_1: str, scan_id_2: str) -> dict:
        """Diff two scans — new, persisting, fixed vulnerabilities."""
        if not self.available:
            return {}
        from bson import ObjectId
        v1 = set(
            v["type"] + "|" + v.get("url", "")
            for v in self.db.vulnerabilities.find({"scan_id": scan_id_1})
        )
        v2 = set(
            v["type"] + "|" + v.get("url", "")
            for v in self.db.vulnerabilities.find({"scan_id": scan_id_2})
        )
        return {
            "new":        list(v2 - v1),
            "persisting": list(v1 & v2),
            "fixed":      list(v1 - v2),
        }

    # ── Credentials ──────────────────────────────────────────
    def save_credential(self, cred: dict):
        if not self.available:
            return
        cred["found_at"] = datetime.now(timezone.utc)
        self.db.credentials.insert_one(cred)

    def get_credentials(self, target: str = None) -> list:
        if not self.available:
            return []
        query = {"target": target} if target else {}
        return list(self.db.credentials.find(query))


# Singleton
db = Database()
