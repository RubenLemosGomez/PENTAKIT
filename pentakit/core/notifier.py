"""
PentaKit — Real-time Notifier
Sends instant alerts for critical findings via Telegram, Slack or Discord.
"""

import httpx
from rich.console import Console
from core.config import config

console = Console()

SEVERITY_EMOJI = {
    "critical": "🔴",
    "high":     "🟠",
    "medium":   "🟡",
    "low":      "🟢",
    "info":     "🔵",
}


def _format_message(finding: dict) -> str:
    sev   = finding.get("severity", "info").lower()
    emoji = SEVERITY_EMOJI.get(sev, "⚪")
    return (
        f"🔐 *PentaKit Alert*\n"
        f"{emoji} *{sev.upper()}* — {finding.get('type', 'Unknown')}\n"
        f"🎯 Target: `{finding.get('target', 'N/A')}`\n"
        f"🔗 URL: `{finding.get('url', 'N/A')}`\n"
        f"📝 {finding.get('description', '')}\n"
        f"💥 CVSS: {finding.get('cvss', 'N/A')}"
    )


async def send_telegram(message: str):
    token   = config.telegram_token
    chat_id = config.telegram_chat_id
    if not token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    async with httpx.AsyncClient() as client:
        try:
            await client.post(url, json={
                "chat_id": chat_id,
                "text": message,
                "parse_mode": "Markdown"
            }, timeout=10)
        except Exception as e:
            console.print(f"[yellow]⚠️  Telegram error: {e}[/yellow]")


async def send_slack(message: str):
    webhook = config.slack_webhook
    if not webhook:
        return
    async with httpx.AsyncClient() as client:
        try:
            await client.post(webhook, json={"text": message}, timeout=10)
        except Exception as e:
            console.print(f"[yellow]⚠️  Slack error: {e}[/yellow]")


async def send_discord(message: str):
    webhook = config.discord_webhook
    if not webhook:
        return
    async with httpx.AsyncClient() as client:
        try:
            await client.post(webhook, json={"content": message}, timeout=10)
        except Exception as e:
            console.print(f"[yellow]⚠️  Discord error: {e}[/yellow]")


async def notify_finding(finding: dict):
    """Send alert for a finding. Only fires for critical and high by default."""
    sev = finding.get("severity", "info").lower()
    if sev not in ("critical", "high"):
        return
    message = _format_message(finding)
    await send_telegram(message)
    await send_slack(message)
    await send_discord(message)
    console.print(f"[bold green]🔔  Alert sent for {sev.upper()} finding[/bold green]")


async def notify_scan_complete(target: str, stats: dict):
    """Summary alert when a full scan completes."""
    message = (
        f"🔐 *PentaKit — Scan Complete*\n"
        f"🎯 Target: `{target}`\n"
        f"🔴 Critical: {stats.get('critical', 0)}\n"
        f"🟠 High: {stats.get('high', 0)}\n"
        f"🟡 Medium: {stats.get('medium', 0)}\n"
        f"🟢 Low: {stats.get('low', 0)}\n"
        f"⏱️ Duration: {stats.get('duration', 'N/A')}"
    )
    await send_telegram(message)
    await send_slack(message)
    await send_discord(message)
