#!/usr/bin/env python3
"""
Study Guide Template Initializer
Automatically replaces placeholders across the repository for your specific course.

Usage:
    python3 scripts/setup_template.py --interactive
    or:
    python3 scripts/setup_template.py \
        --subject "Operating Systems" \
        --course-code "UE25CS242A" \
        --units "Units 1–3" \
        --textbooks "Silberschatz 10e, Stallings 9e" \
        --exam-date "Oct 28, 2026" \
        --exam-pattern "100 MCQs (35 U1 + 35 U2 + 30 U3)" \
        --github-user "imyash0722" \
        --repo-name "UE25CS242A-SEM3-STUDY-MATERIAL" \
        --author "Course Prep Team"
"""

import argparse
import os
import sys
from pathlib import Path

TARGET_FILES = [
    "zensical.yml",
    "mkdocs.yml",
    "docs/index.md",
    "docs/unit1/01_sample_topic.md",
    "docs/unit1/02_sample_topic.md",
    "docs/unit2/03_sample_topic.md",
    "docs/unit3/15_sample_memory_management.md",
]

def parse_args():
    parser = argparse.ArgumentParser(description="Configure Study Guide Template for a course")
    parser.add_argument("--interactive", action="store_true", help="Prompt interactively for all variables")
    parser.add_argument("--subject", help="Subject name (e.g. Operating Systems, Computer Networks)")
    parser.add_argument("--course-code", help="Course code (e.g. UE25CS242A)")
    parser.add_argument("--units", help="Units covered (e.g. Units 1–3)")
    parser.add_argument("--textbooks", help="Prescribed textbooks citation string")
    parser.add_argument("--exam-date", help="Exam date (e.g. Oct 28, 2026)")
    parser.add_argument("--exam-pattern", help="Exam pattern (e.g. 100 MCQs)")
    parser.add_argument("--github-user", help="GitHub username")
    parser.add_argument("--repo-name", help="GitHub repository name")
    parser.add_argument("--author", help="Author or institution name")
    return parser.parse_args()

def prompt_with_default(prompt_text, default_val):
    resp = input(f"{prompt_text} [{default_val}]: ").strip()
    return resp if resp else default_val

def main():
    args = parse_args()
    root_dir = Path(__file__).resolve().parent.parent

    if args.interactive or not (args.subject and args.course_code and args.repo_name and args.github_user):
        print("\n🎓 --- Study Guide Template Initializer ---\n")
        subject = prompt_with_default("Subject Name", args.subject or "Computer Networks")
        course_code = prompt_with_default("Course Code", args.course_code or "UE25CS243A")
        units = prompt_with_default("Units Covered", args.units or "Units 1–4")
        textbooks = prompt_with_default("Prescribed Textbooks", args.textbooks or "Kurose & Ross 9e, Tanenbaum 6e")
        exam_date = prompt_with_default("Exam Date", args.exam_date or "TBD")
        exam_pattern = prompt_with_default("Exam Question Pattern", args.exam_pattern or "100 MCQs")
        github_user = prompt_with_default("GitHub Username", args.github_user or "imyash0722")
        repo_name = prompt_with_default("GitHub Repo Name", args.repo_name or f"{course_code}-STUDY-MATERIAL")
        author = prompt_with_default("Author / Maintainer", args.author or github_user)
    else:
        subject = args.subject
        course_code = args.course_code
        units = args.units or "Units 1–3"
        textbooks = args.textbooks or "Standard Course Textbooks"
        exam_date = args.exam_date or "TBD"
        exam_pattern = args.exam_pattern or "Standard Exam Pattern"
        github_user = args.github_user
        repo_name = args.repo_name
        author = args.author or github_user

    replacements = {
        "{SUBJECT}": subject,
        "{COURSE_CODE}": course_code,
        "{UNITS}": units,
        "{TEXTBOOKS}": textbooks,
        "{EXAM_DATE}": exam_date,
        "{EXAM_PATTERN}": exam_pattern,
        "{GITHUB_USER}": github_user,
        "{REPO_NAME}": repo_name,
        "{AUTHOR_NAME}": author,
    }

    print("\n📝 Updating template files...")
    updated_count = 0
    for rel_path in TARGET_FILES:
        file_path = root_dir / rel_path
        if not file_path.exists():
            continue
        try:
            content = file_path.read_text(encoding="utf-8")
            original = content
            for placeholder, val in replacements.items():
                content = content.replace(placeholder, val)
            if content != original:
                file_path.write_text(content, encoding="utf-8")
                print(f"  ✓ Updated {rel_path}")
                updated_count += 1
            else:
                print(f"  - No changes in {rel_path}")
        except Exception as e:
            print(f"  ✗ Error updating {rel_path}: {e}", file=sys.stderr)

    print(f"\n✨ Successfully configured {updated_count} files for {subject} ({course_code})!")
    print(f"Next steps:")
    print(f"  1. Review zensical.yml nav topics")
    print(f"  2. Run local preview: zensical serve")
    print(f"  3. Build site:        zensical build")

if __name__ == "__main__":
    main()
