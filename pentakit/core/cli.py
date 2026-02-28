"""
PentaKit — Main TUI Interface
Beautiful terminal UI built with Rich.
"""

import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich import box
from rich.prompt import Prompt, Confirm
from core.config import config
from core.api_manager import show_api_status, get_active_apis
from core.db import db

console = Console()


BANNER = """
██████╗ ███████╗███╗   ██╗████████╗ █████╗ ██╗  ██╗██╗████████╗
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝
██████╔╝█████╗  ██╔██╗ ██║   ██║   ███████║█████╔╝ ██║   ██║   
██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██╔═██╗ ██║   ██║   
██║     ███████╗██║ ╚████║   ██║   ██║  ██║██║  ██╗██║   ██║   
╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   
"""

MENU_ITEMS = [
    ("0", "🚀", "AUTO MODE",           "Full audit: company name → report"),
    ("1", "🔍", "Information Gathering","Recon · subdomains · ports · tech"),
    ("2", "👤", "OSINT",               "Emails · breaches · leaks · intel"),
    ("3", "🎯", "Bug Bounty",          "CVEs · EPSS · KEV · 15 vuln types"),
    ("4", "🔑", "Password Attacks",    "Brute force · hashcrack · stuffing"),
    ("5", "📡", "Wireless Testing",    "WiFi · WPA2 · Evil Twin · Bluetooth"),
    ("6", "💥", "Exploitation Tools",  "CVE PoCs · CMS · RCE · file upload"),
    ("7", "🕵️", "Sniffing & Spoofing", "MITM · ARP · SSL Strip · DNS"),
    ("8", "🌐", "Web Hacking",         "CMS · FFuf · panels · CF bypass"),
    ("9", "💀", "Post Exploitation",   "Shells · privesc · lateral move"),
    ("r", "📄", "Reports",             "HTML · PDF · JSON · HackerOne fmt"),
    ("h", "🗄️", "History",             "Scans · vulns · compare · search"),
    ("k", "🔑", "API Status",          "Check configured API keys"),
    ("q", "❌", "Exit",                ""),
]


def print_banner():
    console.print(f"[bold green]{BANNER}[/bold green]", justify="center")
    console.print(
        Align.center(
            Text("The Business Penetration Testing Toolkit", style="bold white")
        )
    )
    console.print(
        Align.center(
            Text(
                "⚠️  For authorized security testing only. Always get written permission.",
                style="bold yellow"
            )
        )
    )
    console.print()


def print_status_bar():
    targets = config.targets
    scans   = db.list_scans(limit=1000) if db.available else []
    vulns   = db.get_vulns() if db.available else []
    pending = [v for v in vulns if v.get("status") == "pending"]
    apis    = get_active_apis()

    cols = [
        f"[cyan]Target scope:[/cyan] [white]{len(targets)} host(s)[/white]",
        f"[cyan]Total scans:[/cyan] [white]{len(scans)}[/white]",
        f"[cyan]Pending vulns:[/cyan] [bold {'red' if pending else 'green'}]{len(pending)}[/bold {'red' if pending else 'green'}]",
        f"[cyan]Active APIs:[/cyan] [white]{len(apis)}/16[/white]",
    ]
    console.print("  " + "  │  ".join(cols))
    console.print()


def print_menu():
    table = Table(
        show_header=False,
        box=box.ROUNDED,
        border_style="green",
        padding=(0, 1),
        expand=False,
    )
    table.add_column("Key",   style="bold cyan",  width=4)
    table.add_column("Icon",  width=3)
    table.add_column("Name",  style="bold white",  width=24)
    table.add_column("Desc",  style="dim",         width=44)

    for key, icon, name, desc in MENU_ITEMS:
        if key == "0":
            table.add_row(
                f"[bold yellow]{key}[/bold yellow]",
                icon,
                f"[bold yellow]{name}[/bold yellow]",
                f"[yellow]{desc}[/yellow]",
            )
        elif key == "q":
            table.add_row(f"[red]{key}[/red]", icon, f"[red]{name}[/red]", "")
        else:
            table.add_row(key, icon, name, desc)

    console.print(Align.center(table))
    console.print()


def route(choice: str):
    """Route menu choice to the appropriate module."""
    c = choice.strip().lower()

    if c == "0":
        from modules._00_auto.full_audit import run_auto_mode
        run_auto_mode()

    elif c == "1":
        from modules._01_recon.recon_menu import run_recon_menu
        run_recon_menu()

    elif c == "2":
        from modules._02_osint.osint_menu import run_osint_menu
        run_osint_menu()

    elif c == "3":
        from modules._03_bugbounty.bugbounty_menu import run_bugbounty_menu
        run_bugbounty_menu()

    elif c == "4":
        from modules._04_password_attacks.password_menu import run_password_menu
        run_password_menu()

    elif c == "5":
        from modules._05_wireless.wireless_menu import run_wireless_menu
        run_wireless_menu()

    elif c == "6":
        from modules._06_exploitation.exploit_menu import run_exploit_menu
        run_exploit_menu()

    elif c == "7":
        from modules._07_sniffing_spoofing.sniff_menu import run_sniff_menu
        run_sniff_menu()

    elif c == "8":
        from modules._08_web_hacking.web_menu import run_web_menu
        run_web_menu()

    elif c == "9":
        from modules._09_post_exploitation.postexploit_menu import run_postexploit_menu
        run_postexploit_menu()

    elif c == "r":
        from modules._10_reporting.report_menu import run_report_menu
        run_report_menu()

    elif c == "h":
        run_history_menu()

    elif c == "k":
        show_api_status()

    elif c == "q":
        console.print("\n[bold green]root@pentakit:~$[/bold green] [dim]logout[/dim]\n")
        sys.exit(0)

    else:
        console.print("[yellow]Invalid option. Try again.[/yellow]")


def run_history_menu():
    console.print(Panel("[bold]🗄️  Scan History[/bold]", border_style="green"))
    if not db.available:
        console.print("[yellow]MongoDB not connected. History unavailable.[/yellow]")
        return

    scans = db.list_scans(limit=20)
    if not scans:
        console.print("[dim]No scans found.[/dim]")
        return

    table = Table(show_header=True, header_style="bold cyan", border_style="green")
    table.add_column("#",        width=3)
    table.add_column("ID",       width=26)
    table.add_column("Target",   width=30)
    table.add_column("Date",     width=20)
    table.add_column("Findings", width=10)

    for i, scan in enumerate(scans, 1):
        table.add_row(
            str(i),
            str(scan.get("_id", "")),
            scan.get("target", ""),
            str(scan.get("timestamp", ""))[:19],
            str(scan.get("total_findings", "?")),
        )
    console.print(table)

    console.print("\n[cyan]Commands:[/cyan] [white]list · search <query> · compare <id1> <id2> · back[/white]")
    cmd = Prompt.ask("[green]history>[/green]")
    if cmd.startswith("compare"):
        parts = cmd.split()
        if len(parts) == 3:
            diff = db.compare_scans(parts[1], parts[2])
            console.print(f"[green]New:[/green] {len(diff.get('new',[]))}")
            console.print(f"[yellow]Persisting:[/yellow] {len(diff.get('persisting',[]))}")
            console.print(f"[dim]Fixed:[/dim] {len(diff.get('fixed',[]))}")


def main_loop():
    while True:
        console.clear()
        print_banner()
        print_status_bar()
        print_menu()
        choice = Prompt.ask("[bold green]root@pentakit:~$[/bold green]")
        console.print()
        route(choice)
        if choice.lower() != "q":
            Prompt.ask("\n[dim]Press Enter to continue[/dim]", default="")
