# Official Oracle OCI Icons Setup Guide

## Quick Start (5 Minutes)

### Step 1: Download Official Icons

**Download from Oracle:**
```
https://docs.oracle.com/en-us/iaas/Content/General/Reference/graphicsfordiagrams.htm
```

Direct downloads:
- **Draw.io**: [OCI-Style-Guide-for-Drawio.zip](https://docs.oracle.com/iaas/Content/Resources/Assets/OCI-Style-Guide-for-Drawio.zip)
- **PowerPoint**: [OCI_Icons.pptx](https://docs.oracle.com/iaas/Content/Resources/Assets/OCI_Icons.pptx)
- **Visio**: [OCI_Icons_Visio.zip](https://docs.oracle.com/iaas/Content/Resources/Assets/OCI_Icons_Visio.zip)

### Step 2: Import into Draw.io

1. Open [app.diagrams.net](https://app.diagrams.net/) or Draw.io desktop
2. Go to **File → Open Library From → Device**
3. Select the `.xml` file from the extracted ZIP
4. OCI icons now appear in left sidebar under "OCI"

### Step 3: Verify Installation

Look for these icon categories in the sidebar:
- OCI Compute (VM, BM, OKE, Functions)
- OCI Database (ATP, ADW, MySQL)
- OCI Networking (VCN, LB, API Gateway)
- OCI AI/ML (GenAI, Data Science)
- OCI Storage (Object, Block, File)
- OCI Security (IAM, Vault, WAF)

---

## Icon Reference (Official Shape Names)

After importing the library, these shapes become available:

### Compute & Containers
```
mxgraph.oci.compute_vm           → Virtual Machine
mxgraph.oci.compute_bm           → Bare Metal
mxgraph.oci.container_engine     → OKE (Kubernetes)
mxgraph.oci.container_instance   → Container Instance
mxgraph.oci.functions            → Functions (Serverless)
mxgraph.oci.instance_pool        → Instance Pool
mxgraph.oci.autoscaling          → Auto Scaling
```

### Database
```
mxgraph.oci.autonomous_database  → Autonomous Database (ATP/ADW)
mxgraph.oci.database_system      → DB System
mxgraph.oci.exadata              → Exadata Cloud
mxgraph.oci.mysql                → MySQL HeatWave
mxgraph.oci.nosql                → NoSQL Database
```

### AI & Machine Learning
```
mxgraph.oci.generative_ai        → OCI Generative AI
mxgraph.oci.data_science         → Data Science Platform
mxgraph.oci.ai_vision            → AI Vision
mxgraph.oci.ai_language          → AI Language
mxgraph.oci.ai_speech            → AI Speech
mxgraph.oci.ai_document          → Document Understanding
mxgraph.oci.anomaly_detection    → Anomaly Detection
```

### Storage
```
mxgraph.oci.object_storage       → Object Storage
mxgraph.oci.block_storage        → Block Volume
mxgraph.oci.file_storage         → File Storage (NFS)
mxgraph.oci.archive_storage      → Archive Storage
```

### Networking
```
mxgraph.oci.vcn                  → Virtual Cloud Network
mxgraph.oci.subnet               → Subnet
mxgraph.oci.load_balancer        → Load Balancer (L7)
mxgraph.oci.network_load_balancer → Network Load Balancer (L4)
mxgraph.oci.api_gateway          → API Gateway
mxgraph.oci.fastconnect          → FastConnect
mxgraph.oci.drg                  → Dynamic Routing Gateway
mxgraph.oci.nat_gateway          → NAT Gateway
mxgraph.oci.internet_gateway     → Internet Gateway
mxgraph.oci.service_gateway      → Service Gateway
mxgraph.oci.waf                  → Web Application Firewall
mxgraph.oci.dns                  → DNS
```

### Integration & Messaging
```
mxgraph.oci.streaming            → Streaming (Kafka)
mxgraph.oci.integration          → Integration Cloud
mxgraph.oci.events               → Events Service
mxgraph.oci.notifications        → Notifications
mxgraph.oci.queue                → Queue Service
```

### Security & Identity
```
mxgraph.oci.iam                  → IAM
mxgraph.oci.vault                → Vault (KMS)
mxgraph.oci.bastion              → Bastion Service
mxgraph.oci.cloud_guard          → Cloud Guard
mxgraph.oci.data_safe            → Data Safe
mxgraph.oci.certificates         → Certificates
```

### Observability
```
mxgraph.oci.logging              → Logging Service
mxgraph.oci.monitoring           → Monitoring
mxgraph.oci.apm                  → APM
mxgraph.oci.logging_analytics    → Logging Analytics
```

### DevOps
```
mxgraph.oci.devops               → DevOps Service
mxgraph.oci.resource_manager     → Resource Manager
mxgraph.oci.container_registry   → Container Registry
```

---

## Pre-Built Templates

The OCI icon set includes starter templates. After importing:

1. Scroll to the bottom of the OCI icons in the sidebar
2. Look for "Logical" and "Physical" template examples
3. Drag a template to your canvas as a starting point

**Available Templates:**
- 3-Tier Web Application
- Hub-and-Spoke Network
- DR Architecture
- Data Platform
- AI/ML Platform

---

## Python Diagrams Library (Alternative)

For code-generated diagrams, the Python `diagrams` library has OCI icons built-in:

```bash
pip install diagrams
# Requires Graphviz: brew install graphviz (macOS)
```

```python
from diagrams import Diagram
from diagrams.oci.compute import Container, VM
from diagrams.oci.database import AutonomousDatabase
from diagrams.oci.network import LoadBalancer

with Diagram("OCI Architecture", show=False):
    lb = LoadBalancer("LB")
    app = [VM("App-1"), VM("App-2")]
    db = AutonomousDatabase("ATP")

    lb >> app >> db
```

**OCI icons included:**
- `diagrams.oci.compute` - VM, BM, OKE, Functions, etc.
- `diagrams.oci.database` - AutonomousDatabase, MySQL, etc.
- `diagrams.oci.network` - LoadBalancer, VCN, APIGateway, etc.
- `diagrams.oci.storage` - ObjectStorage, BlockStorage, etc.
- `diagrams.oci.security` - Vault, CloudGuard, etc.

---

## Troubleshooting

### "Shape not found" Error
**Cause:** OCI library not imported
**Fix:** File → Open Library From → select the OCI XML file

### Icons appear as generic boxes
**Cause:** Using incorrect shape name
**Fix:** Use exact names from the reference above (e.g., `mxgraph.oci.autonomous_database`)

### Icons missing after reopening
**Cause:** Library not saved to diagram
**Fix:** When saving, check "Include custom libraries"

### Colors don't match Oracle brand
**Use these official colors:**
```
Oracle Red:       #C74634
Oracle Red Dark:  #8B2500
Oracle Black:     #312D2A
Oracle Gray:      #6B6B6B
```

---

## Resources

- [OCI Architecture Diagram Toolkits](https://docs.oracle.com/en-us/iaas/Content/General/Reference/graphicsfordiagrams.htm) - Official download
- [Layered Architecture Diagrams with Draw.io](https://blogs.oracle.com/cloud-infrastructure/post/layered-architecture-diagrams-drawio) - Oracle Blog tutorial
- [OCI Architecture Center](https://docs.oracle.com/en/solutions/) - Reference architectures
- [Python Diagrams Library](https://diagrams.mingrammer.com/) - Code-based diagrams

---

*Last Updated: January 2026*
*Part of the Claude Code Oracle Skills Plugin*
