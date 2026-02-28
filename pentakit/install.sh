#!/bin/bash
# ============================================================
#  PentaKit — Installation Script
#  Tested on: macOS (M1/M2), Ubuntu 22.04, Kali Linux
# ============================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}"
echo "██████╗ ███████╗███╗   ██╗████████╗ █████╗ ██╗  ██╗██╗████████╗"
echo "██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝"
echo "██████╔╝█████╗  ██╔██╗ ██║   ██║   ███████║█████╔╝ ██║   ██║   "
echo "██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██╔═██╗ ██║   ██║   "
echo "██║     ███████╗██║ ╚████║   ██║   ██║  ██║██║  ██╗██║   ██║   "
echo "╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝  "
echo -e "${NC}"
echo -e "${YELLOW}Installing PentaKit — The Business Pentesting Toolkit${NC}"
echo ""

# ── Python check ─────────────────────────────────────────────
echo -e "${GREEN}[1/6] Checking Python version...${NC}"
python3 --version || { echo -e "${RED}Python 3 not found. Install Python 3.12+${NC}"; exit 1; }

# ── Pip dependencies ─────────────────────────────────────────
echo -e "${GREEN}[2/6] Installing Python dependencies...${NC}"
pip3 install -r requirements.txt

# ── External tools (optional but recommended) ────────────────
echo -e "${GREEN}[3/6] Installing external tools...${NC}"

install_tool() {
    if command -v $1 &> /dev/null; then
        echo -e "  ${GREEN}✅ $1 already installed${NC}"
    else
        echo -e "  ${YELLOW}⚠️  $1 not found — install manually for full functionality${NC}"
    fi
}

install_tool nmap
install_tool nuclei
install_tool subfinder
install_tool httpx
install_tool amass
install_tool ffuf
install_tool nikto
install_tool sqlmap

# ── API keys setup ───────────────────────────────────────────
echo -e "${GREEN}[4/6] Setting up API keys...${NC}"
if [ ! -f api_keys.yaml ]; then
    cp api_keys.example.yaml api_keys.yaml
    echo -e "  ${YELLOW}⚠️  api_keys.yaml created — add your free API keys for full power${NC}"
else
    echo -e "  ${GREEN}✅ api_keys.yaml already exists${NC}"
fi

# ── Scope setup ──────────────────────────────────────────────
echo -e "${GREEN}[5/6] Scope configuration...${NC}"
echo -e "  ${YELLOW}ℹ️  Edit scope.yaml to add your authorized targets before scanning${NC}"

# ── Docker environment ───────────────────────────────────────
echo -e "${GREEN}[6/6] Docker lab environment...${NC}"
if command -v docker &> /dev/null; then
    echo -e "  ${GREEN}✅ Docker found${NC}"
    echo -e "  ${YELLOW}   Run 'docker-compose up -d' to start the lab environment${NC}"
else
    echo -e "  ${YELLOW}⚠️  Docker not found — lab environment unavailable${NC}"
fi

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║        ✅  PentaKit installed successfully!           ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  Start PentaKit:    ${YELLOW}python3 main.py${NC}"
echo -e "  Quick scan:        ${YELLOW}python3 main.py bugbounty --url https://target.com${NC}"
echo -e "  Full auto audit:   ${YELLOW}python3 main.py auto --company 'Target Corp'${NC}"
echo -e "  API status:        ${YELLOW}python3 main.py apis${NC}"
echo ""
echo -e "${YELLOW}⚠️  Always obtain written authorization before testing.${NC}"
echo ""
