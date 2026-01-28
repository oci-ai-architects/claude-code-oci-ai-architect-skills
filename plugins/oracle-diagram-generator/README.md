# Oracle Diagram Generator Plugin

Generate professional OCI architecture diagrams using official Oracle icons.

## Quick Start

```bash
# Generate RAG architecture diagram
python scripts/generate_oci_diagram.py --type rag --output ~/diagrams/my-rag-platform

# Generate multi-agent diagram
python scripts/generate_oci_diagram.py --type agent --output ~/diagrams/my-agents

# Generate general AI platform diagram
python scripts/generate_oci_diagram.py --type platform --output ~/diagrams/my-platform
```

## Setup Requirements

### One-Time Setup (No sudo required)

```bash
# Install miniconda in user space
curl -L -o miniconda.sh "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
./miniconda.sh -b -p $HOME/miniconda3

# Accept ToS and install Graphviz
$HOME/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
$HOME/miniconda3/bin/conda install -y graphviz

# Install Python diagrams library
$HOME/miniconda3/bin/pip install diagrams
```

## Diagram Types

| Type | Command | Use Case |
|------|---------|----------|
| `rag` | `--type rag` | RAG/GenAI platforms with vector search |
| `agent` | `--type agent` | Multi-agent orchestration systems |
| `platform` | `--type platform` | General OCI AI/ML platforms |

## Output Quality

Diagrams use:
- **Official OCI icons** from Python diagrams library
- **Oracle brand colors** (#C74634 red, #2d5967 teal, #312D2A text)
- **200 DPI resolution** for crisp presentation quality
- **Orthogonal splines** for clean connection lines
- **White background** for professional appearance

## Example Output

![RAG Architecture](../../examples/visuals/rag-architecture.png)

## Alternative Methods

See [skills/SKILL.md](skills/SKILL.md) for:
- Mermaid.js diagrams (for documentation)
- Draw.io templates (for interactive editing)
- ASCII diagrams (for quick planning)

## Oracle Brand Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Oracle Red | `#C74634` | Primary OCI services |
| OCI Teal | `#2d5967` | Secondary elements |
| Oracle Black | `#312D2A` | Text, lines |
| Light Gray | `#f5f4f2` | Container backgrounds |

## Version History

- **3.0.0** - Python diagrams with official OCI icons (validated)
- **2.0.0** - Documented icon limitations, added Mermaid.js
- **1.0.0** - Initial Draw.io templates

---

*Part of [claude-code-oracle-skills](https://github.com/frankxai/claude-code-oracle-skills)*
