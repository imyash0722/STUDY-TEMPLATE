# Raw Course Materials Staging

Place your source materials here before generating the study guide site:

```
raw_materials/
├── syllabus/        # Course syllabus, lesson plan, evaluation policy
├── textbooks/       # Prescribed textbook chapters or OCR extractions
├── slides/          # Lecture slide presentations (.pptx, .pdf)
├── labs/            # Lab manuals, hands-on C/Python programs
└── question_banks/  # Previous year exam questions, MCQs, sample papers
```

These files serve as input for the **Master Prompt** (`PROMPT_STUDY_WEBSITE.md`).
The prompt scans this directory to extract topics, code examples, numerical traces, and question patterns.
