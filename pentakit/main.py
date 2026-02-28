#!/usr/bin/env python3
"""
██████╗ ███████╗███╗   ██╗████████╗ █████╗ ██╗  ██╗██╗████████╗
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝
██████╔╝█████╗  ██╔██╗ ██║   ██║   ███████║█████╔╝ ██║   ██║
██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██╔═██╗ ██║   ██║
██║     ███████╗██║ ╚████║   ██║   ██║  ██║██║  ██╗██║   ██║
╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝

PentaKit v1.0 — The Business Penetration Testing Toolkit
By Manteigha (Rubén Lemos Gómez) — github.com/RubenLemosGomez

⚠️  For authorized security testing ONLY.
"""

import sys
import click
from rich.console import Console

console = Console()


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    🔐 PentaKit — Business Penetration Testing Toolkit\n
    Run without arguments to launch the interactive TUI menu.
    """
    if ctx.invoked_subcommand is None:
        from core.cli import main_loop
        main_loop()


@cli.command()
@click.option("--company", "-c", required=True, help="Target company name")
@click.option("--output", "-o", default="html,pdf,json", help="Report formats")
def auto(company, output):
    """🚀 Full automated audit from company name to report."""
    from modules._00_auto.full_audit import run_auto_mode
    run_auto_mode(company=company, output_formats=output.split(","))


@cli.command()
@click.option("--target", "-t", required=True, help="Target domain or IP")
@click.option("--modules", "-m", default="all", help="Modules: sub,ports,tech,waf")
def recon(target, modules):
    """🔍 Information gathering and reconnaissance."""
    from core.scope import enforce_scope
    enforce_scope(target)
    from modules._01_recon.recon_menu import run_recon
    run_recon(target=target, modules=modules.split(","))


@cli.command()
@click.option("--target", "-t", required=True, help="Target domain or company name")
def osint(target):
    """👤 OSINT — emails, breaches, leaks, threat intel."""
    from modules._02_osint.osint_menu import run_osint
    run_osint(target=target)


@cli.command()
@click.option("--url", "-u", required=True, help="Target URL")
@click.option("--deep", is_flag=True, default=False, help="Enable deep scan")
def bugbounty(url, deep):
    """🎯 Bug bounty scanner — CVEs, EPSS, KEV, 15 vuln types."""
    from core.scope import enforce_scope
    enforce_scope(url)
    from modules._03_bugbounty.bugbounty_menu import run_bugbounty
    run_bugbounty(url=url, deep=deep)


@cli.command()
@click.option("--target", "-t", required=True, help="Target domain or URL")
def passwords(target):
    """🔑 Password attacks — brute force, hash crack, credential stuffing."""
    from core.scope import enforce_scope
    enforce_scope(target)
    from modules._04_password_attacks.password_menu import run_passwords
    run_passwords(target=target)


@cli.command()
@click.option("--interface", "-i", default="en0", help="Network interface (e.g. en0, wlan0)")
@click.option("--mode", "-m", default="passive", type=click.Choice(["passive", "active"]))
def network(interface, mode):
    """🕵️ Network analysis — MITM, ARP, SSL Strip, packet capture."""
    if mode == "active":
        console.print("[bold yellow]⚠️  Active mode requires explicit authorization.[/bold yellow]")
        confirm = click.confirm("Do you have written authorization to test this network?")
        if not confirm:
            console.print("[red]Aborted.[/red]")
            sys.exit(1)
    from modules._07_sniffing_spoofing.sniff_menu import run_sniff
    run_sniff(interface=interface, mode=mode)


@cli.command()
@click.option("--scan-id", "-s", required=True, help="Scan ID from MongoDB")
@click.option("--format", "-f", default="html,pdf", help="Output formats")
def report(scan_id, format):
    """📄 Generate professional report from a scan."""
    from modules._10_reporting.report_menu import generate_report
    generate_report(scan_id=scan_id, formats=format.split(","))


@cli.command()
@click.option("--target", "-t", default=None, help="Filter by target")
@click.option("--severity", "-s", default=None, help="Filter by severity")
@click.option("--compare", "-c", nargs=2, help="Compare two scan IDs")
def history(target, severity, compare):
    """🗄️ View and manage scan history from MongoDB."""
    from core.db import db
    if compare:
        diff = db.compare_scans(compare[0], compare[1])
        console.print(f"[green]New:[/green]        {len(diff.get('new', []))} findings")
        console.print(f"[yellow]Persisting:[/yellow] {len(diff.get('persisting', []))} findings")
        console.print(f"[dim]Fixed:[/dim]       {len(diff.get('fixed', []))} findings")
    else:
        vulns = db.get_vulns(target=target, severity=severity)
        console.print(f"[bold cyan]Found {len(vulns)} vulnerabilities[/bold cyan]")
        for v in vulns[:20]:
            sev = v.get("severity", "?").upper()
            col = {"CRITICAL": "red", "HIGH": "orange3", "MEDIUM": "yellow", "LOW": "green"}.get(sev, "white")
            console.print(f"  [{col}]{sev}[/{col}]  {v.get('type','?')}  {v.get('url','')}")


@cli.command()
def apis():
    """🔑 Show API integration status."""
    from core.api_manager import show_api_status
    show_api_status()


if __name__ == "__main__":
    cli()
