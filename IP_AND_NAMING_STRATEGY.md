# IP, Naming & Account Strategy

## The Problem

1. **"Oracle" in name** - Could imply endorsement or official affiliation
2. **Trademark risk** - Oracle is a registered trademark
3. **Professional separation** - FrankX/Arcanea IP vs. work-related projects
4. **Employer considerations** - Potential conflicts of interest

## Trademark Analysis

### What's Allowed (Generally)
- Describing compatibility: "Skills for OCI" or "Works with Oracle Cloud"
- Factual statements: "Supports Oracle Database"
- Nominative use: "Patterns for Oracle ADK"

### What's Risky
- "Oracle Skills" - Implies Oracle made/endorsed it
- Using Oracle logo - Definitely not allowed
- "Official Oracle" - False endorsement
- Colors that mimic Oracle branding

### Safe Naming Alternatives

| Current | Alternative | Notes |
|---------|------------|-------|
| `claude-code-oracle-skills` | `oci-architect-skills` | Describes function, uses OCI (allowed) |
| | `cloud-ai-architect-toolkit` | Completely generic |
| | `enterprise-cloud-skills` | No trademark issues |
| | `agentic-cloud-patterns` | Focus on patterns |

## Account Strategy

### Option A: Keep on frankxai (Current)
**Pros:**
- Already set up
- Your personal brand
- Simple

**Cons:**
- Mixes personal brand with potentially work-adjacent content
- If Oracle has concerns, it affects your personal account

### Option B: Separate Account (Recommended)
**Pros:**
- Clean IP separation
- Professional for this specific use case
- Protects FrankX/Arcanea brand
- Can disclaim "unofficial community project"

**Cons:**
- More accounts to manage
- Need to build reputation

### Option C: Organization Account
**Pros:**
- Most professional
- Can add contributors
- Clear separation from personal
- "Community project" feel

**Cons:**
- More setup
- Overkill if solo project

## Recommended Approach

### 1. Rename the Project
From: `claude-code-oracle-skills`
To: `oci-architect-skills` or `cloud-ai-patterns`

### 2. Add Clear Disclaimer
```markdown
> **Disclaimer:** This is an unofficial community project.
> Not affiliated with, endorsed by, or sponsored by Oracle Corporation.
> Oracle, OCI, and related marks are trademarks of Oracle Corporation.
```

### 3. Keep on frankxai OR Create New Account

**If staying on frankxai:**
- Add disclaimer prominently
- Remove Oracle-specific branding
- Focus on "patterns for cloud AI" rather than "Oracle skills"

**If creating new account:**
- Name: `cloud-ai-patterns` or similar
- Transfer/recreate repo
- Keep frankxai for Arcanea/personal

### 4. Color/Visual Updates
- Remove Oracle Red (#C74634)
- Use neutral tech colors (blue, cyan, purple)
- No Oracle-style visual elements

## FrankX/Arcanea IP Protection

Your personal IP (Arcanea, FrankX brand, creative work) should stay clearly separated:

```
GitHub Accounts:
├── frankxai (PERSONAL)
│   ├── Arcanea plugins
│   ├── FrankX.AI website
│   ├── Creative/spiritual content
│   └── Personal brand projects
│
└── [new-account] (COMMUNITY/WORK-ADJACENT)
    ├── oci-architect-skills (this project)
    ├── Cloud patterns
    └── Professional/technical open source
```

## Quick Decision Matrix

| Factor | Stay on frankxai | New Account |
|--------|-----------------|-------------|
| Simplicity | ✅ | ❌ |
| IP Protection | ⚠️ | ✅ |
| Professional Image | ⚠️ | ✅ |
| Community Feel | ❌ | ✅ |
| Trademark Safety | ⚠️ | ✅ |

## Recommendation

**Short term:**
1. Rename to `oci-architect-skills`
2. Add disclaimer
3. Update visuals to remove Oracle branding
4. Keep on frankxai for now

**Long term:**
1. Create organization account for professional OSS
2. Move cloud/enterprise projects there
3. Keep FrankX/Arcanea purely personal brand
