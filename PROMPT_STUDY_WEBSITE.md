# Reusable Master Prompt: Create Study Guide Website from Course Materials

Use this master prompt with any LLM or AI coding agent (e.g. Antigravity, Claude, ChatGPT) along with your course materials (PDFs, PPTs, notes, lab code) to generate a complete, deployable static study website.

---

## 📋 Master Prompt

> **Role**: You are an expert technical documentation engineer and academic course specialist. Create a complete, deployable static study website from raw course materials for any academic or technical subject.
>
> **Input**:
> - Course materials directory (`raw_materials/`: PDFs, lecture notes, textbook chapters, lab code, previous exams)
> - Course metadata: `{SUBJECT}`, `{COURSE_CODE}`, `{UNITS}`, `{EXAM_DATE}`, `{EXAM_PATTERN}`
> - Textbook references: `{TEXTBOOKS}`
> - Repository information: `{GITHUB_USER}`, `{REPO_NAME}`
>
> **Output**:
> - Fully structured markdown topic files organized sequentially (`docs/unitX/NN_topic-name.md` or `docs/NN_topic-name.md`)
> - Configured static site using Zensical (Material theme) with horizontal unit tabs, left navigation, and right TOC
> - Dark/Light mode toggle (single, non-duplicated sun/moon button before search)
> - Clean GitHub repository link showing "GitHub" and star/fork stats without repo title truncation
> - Deployed to GitHub Pages via GitHub Actions or manual subtree push

---

## 🎯 Course Customization Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{SUBJECT}` | Full course name | Operating Systems / Computer Networks / DBMS |
| `{COURSE_CODE}` | Academic course catalog ID | UE25CS242A / CS301 / EE450 |
| `{UNITS}` | Range of units or chapters covered | Units 1–3 / Units 1–4 / Modules A–D |
| `{TEXTBOOKS}` | Primary textbooks and authors | Silberschatz 10e, Stallings 9e, Stevens & Rago 3e |
| `{EXAM_DATE}` | Target examination date | Oct 28, 2026 / Dec 15, 2026 |
| `{EXAM_PATTERN}` | Breakdown of question types | 100 MCQs (35 U1 + 35 U2 + 30 U3) |
| `{REPO_NAME}` | GitHub repository name | UE25CS242A-SEM3-STUDY-MATERIAL |
| `{GITHUB_USER}` | GitHub username or organization | imyash0722 |
| `{AUTHOR_NAME}` | Course author / maintainer | Course Prep Team |

---

## 📐 Topic Content Structure Blueprint (Image 3 Standard)

Every generated topic file must strictly follow this structure:

```markdown
# Topic NN: {TOPIC_TITLE} — {TOPIC_SUBTITLE}

**Source**: Lecture X.Y (Unit Z) + Textbook Ch. W ({TEXTBOOKS})

---

## NN.1 {PRIMARY_CONCEPT_NAME}

### Logical / Conceptual Flow
```text
[Component A] ──► [Processing / Translation Unit] ──► [Component B]
```

### Hardware Support / Core Invariants
- **Base / Relocation Registers**: Definition and purpose.
- **Limit Registers**: Legal range condition `0 ≤ Address < Limit`.
- **Hardware Trap Behavior**: Action triggered if condition is violated.
- **Control Registers**: Pointers to translation structures (e.g., PTBR).

---

## NN.2 {ALGORITHMS_AND_POLICIES}

### Comparative Strategy Table
| Strategy / Algorithm | Description / Mechanism | Trade-off / Complexity |
|----------------------|-------------------------|------------------------|
| **Strategy A**       | How candidate A operates| Fastest; fragmentation risk |
| **Strategy B**       | How candidate B operates| Leaves smallest leftover hole |
| **Strategy C**       | How candidate C operates| Leaves largest remaining hole |

### Protection & Sub-Policies
- Valid / Invalid bits and permission flags (Read, Write, Execute).
- Shared memory semantics (Copy-on-Write, reentrant code).

---

## NN.3 {IMPLEMENTATION_AND_CODE_PATTERNS}

### System APIs & Lab Code
```c
#include <header.h>

// Exact function signature and system call invocation
void *system_call_pattern(void *addr, size_t len, int prot, int flags);
```

### Parameter Reference Table
| Parameter | Type / Macro | Description |
|-----------|--------------|-------------|
| `param1`  | `type`       | Role and valid values |

### Real-World Systems Use Cases
- High-performance buffer caching.
- Dynamic library loading (`dlopen` / `mmap`).

---

## NN.4 Key Takeaways

1. **Core Mechanism** = High-yield summary rule.
2. **Key Trade-off** = Space vs. time trade-off.
3. **Primary Trap** = Common edge case or misconception.

---

## NN.5 Exam-Relevant MCQ Patterns

??? question "MCQ Pattern 1: {CONCEPT_TRAP}"
    {Question stem testing boundary condition or edge case}
    
    - [ ] A) {Plausible distractor}
    - [x] B) {Correct technical answer}
    - [ ] C) {Common miscalculation}
    - [ ] D) {Unrelated concept}

    ??? success "Explanation"
        {Detailed technical explanation of why B is correct and why other options fail.}

---

## NN.6 Practice Problems & Numerical Traces

### Problem 1: {ALGORITHM_TRACE}
Given:
- Input parameters: {Values}
- Step-by-step trace requirement.

??? success "Solution Trace"
    {Step-by-step manual computation trace showing intermediate and final values.}
```

---

## ⚙️ Configuration & Key Learnings

### 1. Dark/Light Mode Toggle (Single Button Fix)
- **Do NOT** define `toggle:` under `palette:` in `zensical.yml` / `mkdocs.yml`. Adding `toggle:` in YAML creates a native palette button that conflicts with `theme-toggle.js`, causing the duplicate toggle bug (Image 1).
- In `zensical.yml`:
  ```yaml
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
    - scheme: slate
      primary: indigo
      accent: indigo
  ```
- In `overrides/assets/javascripts/theme-toggle.js`:
  Injects a single sun/moon button before the search box with deduplication protection.

### 2. GitHub Repo Header Link (Clean Style)
- In `zensical.yml`, explicitly set `repo_name: GitHub`:
  ```yaml
  repo_url: https://github.com/{GITHUB_USER}/{REPO_NAME}
  repo_name: GitHub
  ```
- This renders the GitHub icon, the word "GitHub", and live star/fork statistics without displaying a truncated repo slug like `SEM3-CN-UE25CS243A-STU...` (Matches Image 4 & Image 3).

### 3. Next / Previous Page Navigation at the Bottom (Footer Navigation)
- Ensure `navigation.footer` is included under `theme.features:` in `zensical.yml` / `mkdocs.yml`:
  ```yaml
  features:
    - navigation.footer
  ```
  This automatically renders the **"Next"** and **"Previous"** topic navigation buttons at the bottom of each page.

### 4. Git Push Buffer for Large Repositories
- Run `git config http.postBuffer 524288000` to prevent RPC push failures when pushing repos containing slides or images.

### 5. Build & Serve Commands
- Local live preview: `zensical serve` (or `~/.local/bin/zensical serve`)
- Production build: `zensical build --config-file zensical.yml`
