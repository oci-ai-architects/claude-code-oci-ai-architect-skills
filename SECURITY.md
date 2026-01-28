# Security Policy

## Reporting Vulnerabilities

If you discover a security vulnerability in this project, please report it responsibly:

1. **Do NOT** open a public GitHub issue
2. Email the maintainer directly (see profile)
3. Include detailed description and steps to reproduce
4. Allow reasonable time for response before disclosure

## What This Project Does NOT Handle

This is a skill/plugin repository containing documentation and patterns. It does NOT:

- Store credentials or secrets
- Execute code on external systems
- Handle authentication/authorization
- Process sensitive data

## User Responsibilities

When using these skills, YOU are responsible for:

### Credentials & Secrets
- Never commit API keys, passwords, or tokens
- Use environment variables or secret managers
- Rotate credentials if accidentally exposed

### Customer Data
- Never include real customer names in examples
- Use codenames or anonymized data
- Follow your organization's data policies

### Generated Content
- Review AI-generated diagrams before sharing
- Ensure no confidential information is included
- Verify no official logos are present

## Secure Usage Guidelines

### Environment Variables
```bash
# Good - use environment variables
export OCI_TENANCY_OCID="ocid1.tenancy..."
export COHERE_API_KEY="your-key"

# Bad - hardcoded in files
api_key = "sk-actual-key-here"  # NEVER DO THIS
```

### .gitignore Recommendations
```gitignore
# Secrets (add to your project)
.env
.env.local
*.pem
*.key
credentials.json
service-account.json

# Client data
clients/*/deliverables/*
clients/*/notes/*
.private/
```

### Before Committing Checklist
- [ ] No API keys or tokens in code
- [ ] No customer names or identifiers
- [ ] No internal URLs or endpoints
- [ ] No pricing or contract details
- [ ] No security configurations

## Dependencies

This project has no runtime dependencies that execute code. All content is documentation/configuration only.

## Updates

Security-relevant updates will be noted in release notes.

---

*Last updated: January 2026*
