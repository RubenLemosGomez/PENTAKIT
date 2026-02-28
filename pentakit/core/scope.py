"""
PentaKit — Scope Guardian
Validates that every target is explicitly authorized before scanning.
"""

import ipaddress
import fnmatch
from urllib.parse import urlparse
from rich.console import Console
from core.config import config

console = Console()


def _extract_domain(target: str) -> str:
    """Extract bare domain/IP from URL or domain string."""
    if "://" in target:
        return urlparse(target).hostname or target
    return target.split("/")[0].split(":")[0]


def _matches(host: str, pattern: str) -> bool:
    """Check if host matches a scope pattern (wildcard supported)."""
    # Wildcard subdomain match: *.example.com
    if pattern.startswith("*."):
        base = pattern[2:]
        return host == base or host.endswith("." + base)
    # CIDR range
    try:
        network = ipaddress.ip_network(pattern, strict=False)
        addr    = ipaddress.ip_address(host)
        return addr in network
    except ValueError:
        pass
    # Exact or glob match
    return fnmatch.fnmatch(host, pattern)


def is_in_scope(target: str) -> bool:
    """Return True if target is within the defined scope."""
    if not config.targets:
        return False
    host = _extract_domain(target)
    return any(_matches(host, pattern) for pattern in config.targets)


def enforce_scope(target: str) -> None:
    """
    Raise SystemExit if target is out of scope.
    Call this before ANY active operation against a target.
    """
    if not config.targets:
        console.print("\n[bold red]❌  No targets defined in scope.yaml[/bold red]")
        console.print("[yellow]   Add authorized targets to scope.yaml before scanning.[/yellow]\n")
        raise SystemExit(1)

    if not is_in_scope(target):
        host = _extract_domain(target)
        console.print(f"\n[bold red]🚫  OUT OF SCOPE: {host}[/bold red]")
        console.print("[yellow]   This target is not in your scope.yaml.[/yellow]")
        console.print("[yellow]   Only scan systems you are authorized to test.[/yellow]\n")
        raise SystemExit(1)

    console.print(f"[bold green]✅  Scope verified:[/bold green] [cyan]{_extract_domain(target)}[/cyan]")
