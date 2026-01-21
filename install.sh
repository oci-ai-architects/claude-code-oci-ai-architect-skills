#!/bin/bash
# Claude Code Oracle Skills Installer
# Usage: curl -sSL https://raw.githubusercontent.com/FrankX/claude-code-oracle-skills/main/install.sh | bash
# Or: ./install.sh [skill-name]

set -e

REPO_URL="https://github.com/FrankX/claude-code-oracle-skills.git"
SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
REPO_CACHE="${CLAUDE_SKILLS_REPOS:-$HOME/.claude/skills-repos}/claude-code-oracle-skills"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Claude Code Oracle Skills Installer${NC}"
echo "======================================"

# Create directories if needed
mkdir -p "$SKILLS_DIR"
mkdir -p "$(dirname "$REPO_CACHE")"

# Clone or update repo
if [ -d "$REPO_CACHE" ]; then
    echo -e "${YELLOW}Updating existing repository...${NC}"
    cd "$REPO_CACHE"
    git pull --quiet
else
    echo -e "${YELLOW}Cloning repository...${NC}"
    git clone --quiet "$REPO_URL" "$REPO_CACHE"
    cd "$REPO_CACHE"
fi

# Available skills
SKILLS=("oracle-adk" "oracle-agent-spec" "oci-services-expert" "oracle-ai-architect" "oracle-diagram-generator")

# Install function
install_skill() {
    local skill=$1
    if [ -d "skills/$skill" ]; then
        echo -e "  Installing ${GREEN}$skill${NC}..."
        cp -r "skills/$skill" "$SKILLS_DIR/"
        echo -e "    ${GREEN}Done${NC}"
    else
        echo -e "  ${RED}Skill not found: $skill${NC}"
        return 1
    fi
}

# Install specific skill or all
if [ -n "$1" ]; then
    # Install specific skill(s)
    for skill in "$@"; do
        install_skill "$skill"
    done
else
    # Install all skills
    echo -e "${YELLOW}Installing all Oracle skills...${NC}"
    for skill in "${SKILLS[@]}"; do
        install_skill "$skill"
    done
fi

echo ""
echo -e "${GREEN}Installation complete!${NC}"
echo ""
echo "Installed skills:"
for skill in "${SKILLS[@]}"; do
    if [ -d "$SKILLS_DIR/$skill" ]; then
        echo -e "  ${GREEN}[x]${NC} $skill"
    fi
done

echo ""
echo "Skills are now available in Claude Code."
echo "Restart Claude Code to load the new skills."
echo ""
echo "To update skills later:"
echo "  ./install.sh"
echo ""
echo "To install a specific skill:"
echo "  ./install.sh oracle-adk"
