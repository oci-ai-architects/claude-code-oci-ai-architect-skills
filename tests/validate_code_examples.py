#!/usr/bin/env python3
"""
Validate Python code examples in skill files.
Extracts code blocks and checks for syntax errors.
"""

import ast
import re
import sys
from pathlib import Path


def extract_python_blocks(markdown_content: str) -> list[tuple[int, str]]:
    """Extract Python code blocks from markdown content."""
    pattern = r'```python\n(.*?)```'
    blocks = []

    for match in re.finditer(pattern, markdown_content, re.DOTALL):
        # Find line number of this block
        line_num = markdown_content[:match.start()].count('\n') + 1
        code = match.group(1)
        blocks.append((line_num, code))

    return blocks


def validate_python_syntax(code: str) -> tuple[bool, str]:
    """Check if Python code has valid syntax."""
    try:
        ast.parse(code)
        return True, ""
    except SyntaxError as e:
        return False, str(e)


def validate_skill_file(skill_path: Path) -> list[str]:
    """Validate all Python code blocks in a skill file."""
    errors = []
    content = skill_path.read_text()
    blocks = extract_python_blocks(content)

    for line_num, code in blocks:
        # Skip code that's intentionally incomplete (has comments like "# ...")
        if '# ...' in code or '...' in code.strip():
            continue

        # Skip YAML/JSON embedded in Python strings
        if code.strip().startswith('{') or code.strip().startswith('version:'):
            continue

        valid, error = validate_python_syntax(code)
        if not valid:
            errors.append(f"{skill_path}:{line_num}: Syntax error in Python block: {error}")

    return errors


def main():
    """Main entry point."""
    skills_dir = Path("skills")
    all_errors = []

    for skill_file in skills_dir.glob("*/SKILL.md"):
        print(f"Validating: {skill_file}")
        errors = validate_skill_file(skill_file)
        all_errors.extend(errors)

    if all_errors:
        print("\nValidation errors found:")
        for error in all_errors:
            print(f"  {error}")
        sys.exit(1)
    else:
        print("\nAll Python code blocks are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
