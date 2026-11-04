# 📚 Study Guide Website Template

A production-ready, high-yield static study website template powered by **[Zensical](https://github.com/zensical/zensical)** (Material design). Designed for fast exam revision, conceptual clarity, code tracing, and MCQ drills across any academic or engineering course.

---

## 🌟 Key Highlights & Design Decisions

- **Clean Dark / Light Theme Toggle**: Single, sleek Sun ☀️ / Moon 🌙 toggle button positioned right next to the search bar. Configured to prevent the duplicate toggle icon bug seen in Image 1.
- **Next & Previous Page Buttons**: Seamless footer navigation cards (`navigation.footer`) at the bottom of each page guiding learners sequentially through the syllabus with arrow icons and topic titles.
- **Polished GitHub Header Link**: Configured with `repo_name: GitHub` so the top-right header displays the Git branch logo, "GitHub", and live repository star / fork counters (matching Image 4 & Image 3) rather than an ugly truncated repo name slug (`SEM3-CN-UE25CS243A-STU...` in Image 2).
- **Identical Content Structure (Image 3 Standard)**: Every topic follows a rigorous, uniform pedagogical blueprint:
  - Source lecture and textbook chapter references
  - Concept overview & architectural diagrams
  - Comparative strategy & policy tables
  - System call signatures, parameter tables, and hands-on lab code
  - Concise "Key Takeaways" checklist
  - Collapsible "Exam-Relevant MCQ Patterns" with traps & explanations
  - Collapsible "Practice Problems & Numerical Traces" with step-by-step solutions
- **Dual Deployment Options**:
  - **Automated**: Pre-configured GitHub Actions workflow (`.github/workflows/deploy.yml`) builds and deploys to GitHub Pages on push.
  - **Manual / CLI**: Standalone deployment script (`scripts/build_and_deploy.sh`) supporting `git subtree push`.

---

## 📁 Repository Directory Structure

```text
STUDY-TEMPLATE/
├── .github/
│   └── workflows/
│       └── deploy.yml              # Automated GitHub Pages CI/CD workflow
├── docs/                           # Markdown content source directory
│   ├── index.md                    # Course landing page, syllabus, & master checklist
│   ├── TOPIC_BLUEPRINT.md          # Reference blueprint for writing new topics
│   ├── unit1/                      # Unit 1 topics
│   │   ├── 01_sample_topic.md      # Topic 01: System architecture & privilege rings
│   │   └── 02_sample_topic.md      # Topic 02: Process lifecycle & PCBs
│   ├── unit2/                      # Unit 2 topics
│   │   └── 03_sample_topic.md      # Topic 03: Synchronization & IPC
│   └── unit3/                      # Unit 3 topics
│       └── 15_sample_memory_management.md  # Topic 15: Exact replica of Image 3
├── overrides/                      # Zensical template customizations
│   └── assets/
│       └── javascripts/
│           └── theme-toggle.js     # Single toggle button logic with deduplication
├── raw_materials/                  # Staging area for raw PDFs, slides, and notes
│   └── README.md                   # Instructions for staging source files
├── scripts/
│   ├── setup_template.py           # Interactive / CLI script to populate placeholders
│   └── build_and_deploy.sh         # One-command build & git subtree push script
├── .gitignore                      # Python, OS, editor, and build cache ignores
├── zensical.yml                    # Primary Zensical static site configuration
├── mkdocs.yml                      # MkDocs/Zensical compatibility configuration
├── PROMPT_STUDY_WEBSITE.md         # Reusable Master Prompt for AI generation
└── README.md                       # Documentation & method of use (this file)
```

---

## 🎯 Placeholders Reference

The template uses standardized placeholders across all files. You can replace them automatically using the helper script or manually:

| Placeholder | Meaning / Role | Example |
|-------------|----------------|---------|
| `{SUBJECT}` | Full course name | `Operating Systems` / `Computer Networks` |
| `{COURSE_CODE}` | Academic course catalog ID | `UE25CS242A` / `UE25CS243A` |
| `{UNITS}` | Range of covered units | `Units 1–3` / `Units 1–4` |
| `{TEXTBOOKS}` | Primary textbooks and authors | `Silberschatz 10e, Stallings 9e, Stevens & Rago 3e` |
| `{EXAM_DATE}` | Target examination date | `Oct 28, 2026` |
| `{EXAM_PATTERN}` | Question distribution / format | `100 MCQs (35 U1 + 35 U2 + 30 U3)` |
| `{REPO_NAME}` | GitHub repository name | `UE25CS242A-SEM3-STUDY-MATERIAL` |
| `{GITHUB_USER}` | GitHub username / organization | `imyash0722` |
| `{AUTHOR_NAME}` | Maintainer or author credit | `Course Prep Team` |
| `{UNIT_X_TITLE}` | Title of a course unit / module | `Memory Management` |

---

## 🚀 Method of Use: How to Build Your Study Site

### Method A: Automated Setup Script (Fastest)

Run the included initialization script to customize all placeholders across the repository in seconds:

#### Interactive Mode
```bash
python3 scripts/setup_template.py --interactive
```

#### CLI One-Liner
```bash
python3 scripts/setup_template.py \
    --subject "Computer Networks" \
    --course-code "UE25CS243A" \
    --units "Units 1–4" \
    --textbooks "Kurose & Ross 9e, Tanenbaum 6e" \
    --exam-date "Dec 15, 2026" \
    --exam-pattern "100 MCQs (25 per Unit)" \
    --github-user "imyash0722" \
    --repo-name "UE25CS243A-SEM3-STUDY-MATERIAL" \
    --author "Yashwanth Karthik"
```

---

### Method B: Generating from Course Notes using the Master Prompt

If you have raw course materials (lecture slides, textbook PDFs, lab programs, past exams):

1. **Stage your files**: Copy your lecture PDFs and notes into the `raw_materials/` directory.
2. **Open your AI coding assistant**: Open Antigravity, Claude Code, or ChatGPT.
3. **Execute the Master Prompt**: Pass the contents of [`PROMPT_STUDY_WEBSITE.md`](PROMPT_STUDY_WEBSITE.md) to the model along with your course metadata.
4. The AI will:
   - Extract key concepts, diagrams, and formulas into numbered topic files in `docs/`.
   - Update `nav:` in `zensical.yml` and `mkdocs.yml`.
   - Update the master preparation checklist in `docs/index.md`.

---

### Method C: Manual Configuration

If creating or editing topics by hand:

1. Copy [`docs/TOPIC_BLUEPRINT.md`](docs/TOPIC_BLUEPRINT.md) to a new topic file:
   ```bash
   cp docs/TOPIC_BLUEPRINT.md docs/unit1/04_my_topic.md
   ```
2. Fill in the content following the standard headers (`## NN.1`, `## NN.2`, `## NN.3`, etc.).
3. Add the topic to the `nav` section of [`zensical.yml`](zensical.yml).

---

## 💻 Local Development & Preview

### 1. Prerequisites
Ensure Python 3.10+ and `zensical` are installed:
```bash
pip install zensical pymdown-extensions
```

### 2. Live Local Server
Start the development server with live reload:
```bash
zensical serve
# or:
~/.local/bin/zensical serve
```
Open `http://localhost:8000` in your web browser.

### 3. Production Build
Compile the static HTML and assets into `./site/`:
```bash
zensical build --config-file zensical.yml
# or:
zensical build
```

---

## 🌐 Deployment to GitHub Pages

### Option 1: Automated CI/CD with GitHub Actions (Recommended)

1. Push your repository to GitHub:
   ```bash
   gh repo create {REPO_NAME} --public --source=. --remote=origin --push
   ```
2. Navigate to your GitHub repository: **Settings &rarr; Pages &rarr; Build and deployment &rarr; Source**.
3. Select **GitHub Actions**.
4. The workflow in `.github/workflows/deploy.yml` will automatically build with Zensical and deploy your site on every push!

### Option 2: Manual Deployment via Script (`git subtree push`)

If you prefer deploying directly from your local terminal:

```bash
# Builds site, commits changes, pushes main, and deploys 'site/' to gh-pages branch:
./scripts/build_and_deploy.sh "Deploy updated study materials"
```

*Note: Ensure GitHub Pages is configured to serve from the `gh-pages` branch with path `/` (root).*

---

## 🔧 Technical Details & Bug Fixes Explained

### 1. Preventing Duplicate Dark / Light Mode Buttons (Image 1 Fix)
In Material for MkDocs / Zensical, adding `toggle:` under `palette:` in YAML causes the generator to render default toggle icons into the DOM. If a custom JavaScript toggle (`theme-toggle.js`) is also loaded, both buttons appear side-by-side in the header (the bug in Image 1).

**Solution in this template**:
- In `zensical.yml`, `theme.palette` contains **only** `scheme: default` and `scheme: slate` without any `toggle:` keys.
- In `overrides/assets/javascripts/theme-toggle.js`, a deduplication guard hides any native palette labels and injects a single clean toggle button before the search input.

### 2. Clean GitHub Repo Link (Image 4 Fix)
If `repo_name` is omitted, Zensical displays the full repository name slug (e.g. `SEM3-CN-UE25CS243A-STU...` in Image 2), which is truncated and unappealing.

**Solution in this template**:
```yaml
repo_url: https://github.com/{GITHUB_USER}/{REPO_NAME}
repo_name: GitHub
```
This cleanly renders the Git branch logo, the text **GitHub**, and live star / fork counters as shown in Image 4 and Image 3.

### 3. Git HTTP Post Buffer for Large Course Repositories
Large repositories containing PDFs, presentation slides, or diagrams may trigger RPC failure during `git push`. This template script automatically configures:
```bash
git config http.postBuffer 524288000
```

---

## 📄 License

This template is open-source and free to adapt for any academic course, university revision guide, or technical documentation project.
