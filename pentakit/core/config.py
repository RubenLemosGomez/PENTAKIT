"""
PentaKit — Core Configuration
Centralized config loader for API keys, scope and settings.
"""

import os
import yaml
from pathlib import Path

BASE_DIR   = Path(__file__).parent.parent
SCOPE_FILE = BASE_DIR / "scope.yaml"
KEYS_FILE  = BASE_DIR / "api_keys.yaml"
REPORTS_DIR = BASE_DIR / "reports"
WORDLISTS_DIR = BASE_DIR / "wordlists"

# Ensure reports dir exists
REPORTS_DIR.mkdir(exist_ok=True)


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


class Config:
    def __init__(self):
        self._keys   = load_yaml(KEYS_FILE)
        self._scope  = load_yaml(SCOPE_FILE)

    # ── API keys ─────────────────────────────────────────────
    @property
    def github_token(self) -> str:
        return self._keys.get("github_token", "")

    @property
    def virustotal_key(self) -> str:
        return self._keys.get("virustotal_api_key", "")

    @property
    def alienvault_key(self) -> str:
        return self._keys.get("alienvault_api_key", "")

    @property
    def urlscan_key(self) -> str:
        return self._keys.get("urlscan_api_key", "")

    @property
    def shodan_key(self) -> str:
        return self._keys.get("shodan_api_key", "")

    @property
    def viewdns_key(self) -> str:
        return self._keys.get("viewdns_api_key", "")

    @property
    def telegram_token(self) -> str:
        return self._keys.get("telegram_bot_token", "")

    @property
    def telegram_chat_id(self) -> str:
        return self._keys.get("telegram_chat_id", "")

    @property
    def slack_webhook(self) -> str:
        return self._keys.get("slack_webhook_url", "")

    @property
    def discord_webhook(self) -> str:
        return self._keys.get("discord_webhook_url", "")

    # ── Scope ─────────────────────────────────────────────────
    @property
    def targets(self) -> list:
        return self._scope.get("targets") or []

    @property
    def program(self) -> dict:
        return self._scope.get("program") or {}

    @property
    def tester(self) -> dict:
        return self._scope.get("tester") or {}

    def has_key(self, key_name: str) -> bool:
        val = self._keys.get(key_name, "")
        return bool(val and val.strip())


# Singleton
config = Config()
