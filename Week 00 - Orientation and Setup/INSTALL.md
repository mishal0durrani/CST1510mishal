# Installing everything this module needs

Five things, in order. Do not skip ahead — Git needs Python's PATH working
first, VS Code needs both.

> **Prefer a visual, step-by-step version?** Open the
> [**Setup Guide**](https://anna29.github.io/CST1510/setup-guide.html)
> — the same steps below, with a Mac/Windows toggle and a "prove it worked"
> terminal check after each one. This page is the reliable text fallback.

---

## 1. Python

**Check if you already have it.** Open a terminal (see below if you don't
know how) and run:

```
python3 --version
```

If that prints `Python 3.10` or higher, skip to step 2. If it says
"command not found", or shows something older than 3.10:

- **Windows / macOS**: download the installer from
  [python.org/downloads](https://www.python.org/downloads/) and run it.
  **Windows only** — tick **"Add python.exe to PATH"** on the first screen.
  This is the single most common install mistake; if you miss it, nothing
  after this step works and the fix is to reinstall.
- Close and reopen your terminal after installing, then run
  `python3 --version` again to confirm.

**Finding a terminal**, if you've never opened one:
- **Windows**: Start menu → type `PowerShell` → open it.
- **macOS**: `Cmd + Space` → type `Terminal` → open it.

---

## 2. VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/) and
install it. Then open VS Code and install two extensions (the Extensions
icon on the left sidebar, or `Cmd/Ctrl + Shift + X`):

- **Python** (by Microsoft)
- **Jupyter** (by Microsoft)

You need both — the walkthroughs in this module are Jupyter notebooks
(`.ipynb`), and the Jupyter extension is what lets VS Code run them.

---

## 3. Git and GitHub

- Install Git from [git-scm.com](https://git-scm.com/downloads) — accept
  the defaults during install.
- Create a free account at [github.com](https://github.com/) if you don't
  already have one.
- In a terminal, tell Git who you are (use the same email as your GitHub
  account):

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

This is a one-time setup. For the three commands you'll actually run every
week from Week 1 onward — add, commit, push — see `GIT.md`.

---

## 4. Create your own GitHub repository

There is no module repository to clone — you create your own, once, and it
holds every week's work from now to Week 12.

1. On [github.com](https://github.com/), click the **+** top right →
   **New repository**.
2. Name it something like `cst1510-yourname` — lowercase, no spaces.
3. Tick **"Add a README file."** This one box saves you several commands
   later — without it, the repository is created completely empty and
   cloning it takes an extra couple of steps.
4. Click **Create repository**.
5. On the new repo's page, click the green **Code** button and copy the
   HTTPS URL — it looks like `https://github.com/<you>/<repo-name>.git`.
6. In a terminal:

```
cd Documents
mkdir CST1510
cd CST1510
git clone https://github.com/<you>/<repo-name>.git
cd <repo-name>
```

This folder is now your repository for the whole module — every week's
material from Moodle goes here, and `GIT.md`'s weekly routine
(`add` / `commit` / `push`) applies to it from Week 1 onward.

---

## 5. Install the Python packages this module uses

From inside the repository, in the `Week 00 - Orientation and Setup`
folder:

```
pip3 install -r requirements.txt
```

This installs everything used across all 12 weeks in one go — pandas,
bcrypt, Streamlit, and the rest — so you won't need to stop and install
something new most weeks. If you'd rather keep this module's packages
separate from anything else on your machine, that's what a **virtual
environment** is for — worth knowing, not required to start:

```
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
pip3 install -r requirements.txt
```

---

## Now check it worked

```
python3 verify_setup.py
```

Every line should say `OK`. If something says `MISSING`, the line under it
tells you the exact fix — do that one thing and run the script again.

---

## If something won't cooperate

| Problem | Likely fix |
|---|---|
| `python3: command not found` | Python isn't on PATH — reinstall and tick the PATH box (Windows), or restart your terminal |
| `pip3: command not found` | Try `python3 -m pip install -r requirements.txt` instead |
| VS Code doesn't offer a Python kernel for `.ipynb` files | Install the Jupyter extension (step 2), then reopen the notebook and click "Select Kernel" top-right |
| `git: command not found` | Restart your terminal after installing Git; on Windows, use "Git Bash" if PowerShell still can't find it |
| Permission errors installing packages on macOS | Add `--user` to the pip command, or use a virtual environment (above) |

Still stuck at the end of the session — flag it. This is exactly what
today is for.
