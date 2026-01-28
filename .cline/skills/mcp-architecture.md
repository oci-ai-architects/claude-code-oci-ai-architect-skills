# MCP Architecture for Oracle

You are an expert in Model Context Protocol (MCP) integration with Oracle Cloud Infrastructure.

## When to Use This Skill
- Integrating MCP servers with OCI services
- Building Oracle Database MCP connections
- Creating OCI infrastructure MCP tools
- Enterprise MCP architecture patterns

## MCP + OCI Overview

Model Context Protocol enables AI assistants to interact with external systems through standardized tools. Oracle provides official MCP servers for:

1. **Oracle Database MCP** - SQL queries, schema exploration
2. **Oracle Cloud MCP** - OCI resource management

## Oracle Database MCP

### Capabilities
- Execute SQL queries against Oracle databases
- Explore database schemas and objects
- Retrieve data with proper access controls
- Handle connection pooling and security

### Configuration
```json
{
  "mcpServers": {
    "oracle-database": {
      "command": "npx",
      "args": ["-y", "@anthropic/oracle-database-mcp"],
      "env": {
        "ORACLE_USER": "your_user",
        "ORACLE_PASSWORD": "your_password",
        "ORACLE_CONNECT_STRING": "host:port/service"
      }
    }
  }
}
```

### Example Tools
| Tool | Description |
|------|-------------|
| `query` | Execute SELECT statements |
| `describe_table` | Get table structure |
| `list_tables` | List available tables |
| `get_ddl` | Retrieve object DDL |

## Oracle Cloud MCP

### Capabilities
- List and manage OCI resources
- Query compartments, instances, databases
- Check service status and metrics
- Invoke OCI APIs programmatically

### Configuration
```json
{
  "mcpServers": {
    "oracle-cloud": {
      "command": "npx",
      "args": ["-y", "@anthropic/oracle-cloud-mcp"],
      "env": {
        "OCI_CONFIG_FILE": "~/.oci/config",
        "OCI_PROFILE": "DEFAULT"
      }
    }
  }
}
```

## MCP Architecture Patterns

### Pattern 1: Direct Database Access
```
Claude Code → Oracle DB MCP → Autonomous Database
```
- Simple queries and data retrieval
- Schema exploration
- Ad-hoc analysis

### Pattern 2: OCI Resource Management
```
Claude Code → OCI MCP → OCI APIs → Resources
```
- Infrastructure queries
- Resource status checks
- Configuration retrieval

### Pattern 3: Hybrid (Data + Infrastructure)
```
                ┌→ Oracle DB MCP → Database
Claude Code ────┤
                └→ OCI MCP → Infrastructure
```
- Full stack visibility
- Correlated insights

### Pattern 4: Agent-Orchestrated
```
                        ┌→ Oracle DB MCP
Claude Code → ADK Agent ┼→ OCI MCP
                        └→ Custom Tools
```
- Complex workflows
- Multi-step operations
- Business logic integration

## Security Considerations

### Authentication
- Use OCI config files with proper permissions
- Rotate credentials regularly
- Use instance principals where possible

### Authorization
- Principle of least privilege
- Separate read-only and write operations
- Audit all MCP tool invocations

### Network
- Use private endpoints
- VCN service gateways
- No public exposure of MCP servers

## Enterprise Deployment

```
┌─────────────────────────────────────────────┐
│              Enterprise Zone                │
├─────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────────────┐│
│  │ Claude Code │───▶│    MCP Gateway      ││
│  │ (Workstation)│   │ (Authentication +   ││
│  └─────────────┘    │  Rate Limiting)     ││
│                     └──────────┬──────────┘│
│                                │            │
│      ┌─────────────────────────┼───────────┤
│      ▼                         ▼           │
│  ┌───────────┐          ┌───────────┐      │
│  │ DB MCP    │          │ OCI MCP   │      │
│  │ Server    │          │ Server    │      │
│  └─────┬─────┘          └─────┬─────┘      │
│        │                      │            │
│        ▼                      ▼            │
│  ┌───────────┐          ┌───────────┐      │
│  │ Oracle    │          │ OCI       │      │
│  │ Database  │          │ Services  │      │
│  └───────────┘          └───────────┘      │
└─────────────────────────────────────────────┘
```

## Resources
- [Oracle MCP Servers GitHub](https://github.com/oracle/mcp-servers)
- [MCP Specification](https://modelcontextprotocol.io/)
