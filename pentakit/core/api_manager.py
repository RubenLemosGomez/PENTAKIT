"""
PentaKit — API Manager
Shows status of all integrated APIs and manages rate limits.
"""

from rich.console import Console
from rich.table import Table
from core.config import config

console = Console()


API_REGISTRY = [
    # (name, key_attr, free_limit, required)
    ("NVD NIST (CVEs)",     None,                "Unlimited",    True),
    ("OSV API",             None,                "Unlimited",    True),
    ("EPSS API",            None,                "Unlimited",    True),
    ("CISA KEV Catalog",    None,                "Unlimited",    True),
    ("crt.sh",              None,                "Unlimited",    True),
    ("Wayback CDX",         None,                "Unlimited",    True),
    ("HaveIBeenPwned",      None,                "Unlimited",    True),
    ("DNSDumpster",         None,                "Unlimited",    True),
    ("Robtex",              None,                "Unlimited",    True),
    ("ThreatFox",           None,                "Unlimited",    True),
    ("GitHub API",          "github_token",      "5000 req/hr",  False),
    ("VirusTotal",          "virustotal_key",    "4 req/min",    False),
    ("AlienVault OTX",      "alienvault_key",    "Unlimited",    False),
    ("URLScan.io",          "urlscan_key",       "1000/day",     False),
    ("Shodan",              "shodan_key",        "Free tier",    False),
    ("ViewDNS",             "viewdns_key",       "Free tier",    False),
]

NOTIFY_REGISTRY = [
    ("Telegram",  "telegram_token"),
    ("Slack",     "slack_webhook"),
    ("Discord",   "discord_webhook"),
]


def show_api_status():
    """Print a rich table showing which APIs are configured."""
    table = Table(
        title="🌐 API Integration Status",
        show_header=True,
        header_style="bold cyan",
        border_style="green",
        show_lines=True,
    )
    table.add_column("API",         style="white",  min_width=20)
    table.add_column("Status",      style="bold",   min_width=12)
    table.add_column("Free Limit",  style="dim",    min_width=14)
    table.add_column("Required",    style="dim",    min_width=8)

    for name, key_attr, limit, required in API_REGISTRY:
        if key_attr is None:
            status = "[green]✅ Active[/green]"
        else:
            val = getattr(config, key_attr, "")
            status = "[green]✅ Configured[/green]" if val else "[yellow]⚠️  No key[/yellow]"
        req = "[green]Yes[/green]" if required else "[dim]Optional[/dim]"
        table.add_row(name, status, limit, req)

    console.print(table)

    # Notifications
    ntable = Table(
        title="🔔 Notification Channels",
        show_header=True,
        header_style="bold cyan",
        border_style="green",
    )
    ntable.add_column("Channel", style="white",  min_width=12)
    ntable.add_column("Status",  style="bold",   min_width=16)

    for name, key_attr in NOTIFY_REGISTRY:
        val = getattr(config, key_attr, "")
        status = "[green]✅ Configured[/green]" if val else "[dim]Not configured[/dim]"
        ntable.add_row(name, status)

    console.print(ntable)


def get_active_apis() -> list:
    """Return list of API names that are active/configured."""
    active = []
    for name, key_attr, _, _ in API_REGISTRY:
        if key_attr is None or getattr(config, key_attr, ""):
            active.append(name)
    return active
