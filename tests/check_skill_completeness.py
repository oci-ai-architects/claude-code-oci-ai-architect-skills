#!/usr/bin/env python3
"""
Check that all skills have required sections and metadata.
"""

import re
import sys
import yaml
from pathlib import Path


# Required sections in each skill file
REQUIRED_SECTIONS = [
    "Purpose",
    "Resources",
]

# Recommended sections (warning only)
RECOMMENDED_SECTIONS = [
    "Best Practices",
    "Examples",
]


def check_frontmatter(content: str) -> tuple[bool, dict, str]:
    """Extract and validate YAML frontmatter."""
    if not content.startswith('---'):
        return False, {}, "Missing YAML frontmatter"

    try:
        # Extract frontmatter
        end_idx = content.index('---', 3)
        frontmatter = content[3:end_idx].strip()
        metadata = yaml.safe_load(frontmatter)

        # Check required fields
        required = ['name', 'description', 'version']
        missing = [f for f in required if f not in metadata]

        if missing:
            return False, metadata, f"Missing frontmatter fields: {missing}"

        return True, metadata, ""
    except Exception as e:
        return False, {}, f"Invalid frontmatter: {e}"


def check_sections(content: str) -> tuple[list[str], list[str]]:
    """Check for required and recommended sections."""
    # Extract all headers
    headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    headers_lower = [h.lower() for h in headers]

    missing_required = []
    missing_recommended = []

    for section in REQUIRED_SECTIONS:
        if not any(section.lower() in h for h in headers_lower):
            missing_required.append(section)

    for section in RECOMMENDED_SECTIONS:
        if not any(section.lower() in h for h in headers_lower):
            missing_recommended.append(section)

    return missing_required, missing_recommended


def check_code_examples(content: str) -> bool:
    """Check if skill has at least one code example."""
    return '```' in content


def validate_skill(skill_path: Path) -> tuple[list[str], list[str]]:
    """Validate a skill file. Returns (errors, warnings)."""
    errors = []
    warnings = []

    content = skill_path.read_text()

    # Check frontmatter
    valid, metadata, error = check_frontmatter(content)
    if not valid:
        errors.append(f"Frontmatter: {error}")

    # Check sections
    missing_req, missing_rec = check_sections(content)
    if missing_req:
        errors.append(f"Missing required sections: {missing_req}")
    if missing_rec:
        warnings.append(f"Missing recommended sections: {missing_rec}")

    # Check for code examples
    if not check_code_examples(content):
        warnings.append("No code examples found")

    # Check minimum content length
    if len(content) < 1000:
        warnings.append(f"Content seems thin ({len(content)} chars)")

    return errors, warnings


def check_manifest_consistency() -> list[str]:
    """Check that manifest.yaml matches actual skills."""
    errors = []

    manifest_path = Path("manifest.yaml")
    if not manifest_path.exists():
        return ["manifest.yaml not found"]

    manifest = yaml.safe_load(manifest_path.read_text())
    manifest_skills = set(manifest.get('skills', {}).keys())

    # Get actual skill directories
    skills_dir = Path("skills")
    actual_skills = set(d.name for d in skills_dir.iterdir() if d.is_dir())

    # Check for mismatches
    missing_in_manifest = actual_skills - manifest_skills
    missing_in_dir = manifest_skills - actual_skills

    if missing_in_manifest:
        errors.append(f"Skills not in manifest: {missing_in_manifest}")
    if missing_in_dir:
        errors.append(f"Skills in manifest but not found: {missing_in_dir}")

    return errors


def main():
    """Main entry point."""
    skills_dir = Path("skills")
    all_errors = []
    all_warnings = []

    print("Checking skill completeness...")
    print("=" * 50)

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            all_errors.append(f"{skill_dir.name}: Missing SKILL.md")
            continue

        print(f"\n{skill_dir.name}:")
        errors, warnings = validate_skill(skill_file)

        if errors:
            for e in errors:
                print(f"  ERROR: {e}")
                all_errors.append(f"{skill_dir.name}: {e}")

        if warnings:
            for w in warnings:
                print(f"  WARNING: {w}")
                all_warnings.append(f"{skill_dir.name}: {w}")

        if not errors and not warnings:
            print("  OK")

    # Check manifest consistency
    print("\n" + "=" * 50)
    print("Checking manifest consistency...")
    manifest_errors = check_manifest_consistency()
    all_errors.extend(manifest_errors)
    for e in manifest_errors:
        print(f"  ERROR: {e}")

    # Summary
    print("\n" + "=" * 50)
    print(f"Total errors: {len(all_errors)}")
    print(f"Total warnings: {len(all_warnings)}")

    if all_errors:
        print("\nFailed with errors!")
        sys.exit(1)
    else:
        print("\nAll checks passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
