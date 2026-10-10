# Git and GitHub — the weekly workflow

> **Prefer a visual, step-by-step version of the one-time setup?** Open the
> [**Git & GitHub Guide**](https://anna29.github.io/CST1510/git-and-github-guide.html)
> — registering GitHub, installing Git, and creating your own repository,
> with an OS toggle. This page is the reliable text fallback, and the one
> you'll actually return to every week for the routine below.

`INSTALL.md` got Git installed and walked you through creating and cloning
your own repository — a one-time job. This file is different: it's what
you actually do **every single week**,
from Week 1 to Week 12, at the end of the lab.

The first time, go through it slowly, one step at a time, and actually type
each command yourself — don't copy-paste the whole block at once. By Week 3
or so this will take you under a minute and you won't need this file open.

---

## Why this matters, not just "because we said so"

Your repository is not just backup — it *is* the evidence. From the CW1
specification: **"Keep your work in the module repository throughout the
term. The weekly commit history may be used as supporting evidence of
progress."** A tutor can open your repository and see, week by week, that
you did the work, in order, on time. A pile of files pushed once in Week 12
does not show that, even if the final code is identical.

---

## Step 0 — open a terminal, in the right place

If you don't remember how to open a terminal, `INSTALL.md` step 1 covers it
(Windows: Start menu → `PowerShell`. macOS: `Cmd + Space` → `Terminal`).

You need to be **inside your repository folder** — the one you created and
cloned in `INSTALL.md`, the one you're building up with a `Week NN - ...`
folder every week. If you have it open in VS Code, the easiest way is: in VS Code,
open the built-in terminal (`` Ctrl+` `` on Windows/Linux, `` Cmd+` `` on
macOS) — it opens already inside the right folder.

Otherwise, in any terminal, check where you are:

```
pwd
```

This prints the folder you're currently in. If it does not end in your
repository's folder name (e.g. `.../cst1510-yourname`), navigate there:

```
cd path/to/your/repository
```

Everything below assumes you are standing in this folder. If you run these
commands from the wrong place, nothing works right — this is the single
most common way students think they've saved their work and haven't.

---

## Step 1 — see what you changed

```
git status
```

You'll see something like this (your exact filenames will differ):

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
	modified:   Week 04 - Lists, Dictionaries and Files/LAB/W04_Lab.ipynb
	modified:   Week 04 - Lists, Dictionaries and Files/LAB/template.py

Untracked files:
	Week 04 - Lists, Dictionaries and Files/LAB/my_records.csv

no changes added to commit (use "git add" and/or "git commit -a")
```

Read this as: **"modified"** = a file that already existed and you edited
it. **"Untracked"** = something brand new Git has never seen before (like
your own data file, if this week's mini-project loads from one). Both need
to go in — that's the next step.

Weeks 1–7, your journal lives *inside* the notebook — you paste the photo
straight into a markdown cell, so it shows up as part of the
`W0N_Lab.ipynb` "modified" line above, not as a separate untracked file.

This step doesn't change anything — it's just looking. Run it as often as
you like.

---

## Step 2 — stage everything

```
git add .
```

This command prints **nothing** if it works — that's normal, not an error.
The `.` means "everything in this folder and every folder inside it."

Check it worked by running `git status` again:

```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
	modified:   Week 04 - Lists, Dictionaries and Files/LAB/W04_Lab.ipynb
	modified:   Week 04 - Lists, Dictionaries and Files/LAB/template.py
	new file:   Week 04 - Lists, Dictionaries and Files/LAB/my_records.csv
```

Everything has moved from "not staged" to **"Changes to be committed"** —
that's what "staged" means: marked and ready to be saved in the next step.

---

## Step 3 — save a snapshot

```
git commit -m "Week 4 lab and mini-project"
```

(Change the `4` to whatever week you're actually on.) You'll see something
like:

```
[main 3f2a9c1] Week 4 lab and mini-project
 3 files changed, 42 insertions(+), 5 deletions(-)
```

This has saved a snapshot **on your own machine only** — it is not on
GitHub yet. That's the next and final step.

The text inside the quotes is called the **commit message** — see "write a
message that means something" below before you get into the habit of
typing something lazy here.

---

## Step 4 — send it to GitHub

```
git push
```

You'll see something like:

```
Enumerating objects: 7, done.
Writing objects: 100% (4/4), 1.02 KiB | 1.02 MiB/s, done.
To github.com:yourusername/your-repo.git
   1a2b3c4..3f2a9c1  main -> main
```

The first time you ever push, your terminal may ask you to sign in to
GitHub — follow whatever it asks for. If it asks for a password and
rejects it, see "if something won't cooperate" below — GitHub no longer
accepts a plain password here.

---

## Step 5 — check it's actually there

Open **github.com**, sign in, open your repository, and look for this
week's folder. `git push` finishing without a red error message is a good
sign, but seeing the actual files sitting there in your browser is the
only real proof. Do this every week, not just the first time.

---

## Every week, once you know the steps

Once you've done the five steps above a couple of times, this is the whole
thing, back to back:

```
git status
git add .
git commit -m "Week N lab and mini-project"
git push
```

Then check GitHub in a browser. That's it — same four lines, every week,
whether it's Week 1 or Week 12.

---

## What actually gets committed each week

You never hand-pick files — `git add .` sweeps up **everything** that
changed. You don't need to remember what follows below or add each file
individually — `.` already means "everything," and that's the point of
using it. But it's worth knowing what actually matters, versus what just
comes along for the ride.

**Weeks 1–7.** Only **2 files** are kept and count towards CW1:

- that week's `LAB/W0N_Lab.ipynb` — your drill answers, your mini-project
  notes, **and your Cheat Sheet photo, pasted directly into a markdown
  cell at the end of the notebook** (paste the image in; Jupyter embeds
  it in the notebook file automatically — there is no separate journal
  file or `journal/weekNN/` folder these weeks). The rest of that week's
  journal — the diagram, the three concepts, your errors — stays on
  paper; it's not photographed or pushed.
- that week's `LAB/template.py`, your mini-project

Some weeks' mini-project genuinely needs a data file to run (Weeks 4–7,
Typical tier and above) — that file is part of the project, not extra
clutter, and is expected alongside the 2. The `LAB/warmup/*.py` fixes are
worth doing, but are not required to be pushed or kept — if `git add .`
sweeps them in too, that's harmless, they're just not checked.

**Weeks 8–12.** There's no journal and no Cheat Sheet any more — just the
one continuous `project/` folder, committed and pushed at the end of every
lab so progress actually accumulates week to week rather than turning up
all at once. `git add .` handles all of it the same way either side of
Week 7.

---

## Write a commit message that means something

`"Week 4 lab and mini-project"` tells you something, months later, when you
need to find it. `"stuff"` or `"update"` does not — and you will be the one
scrolling back through this history before the CW1/CW2 deadline. Stick to
the pattern **`"Week N lab and mini-project"`**, every week, so your own
history is easy to scan later.

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| running the commands from the wrong folder | `fatal: not a git repository`, or a push that "succeeds" but nothing appears on GitHub | `pwd` first, `cd` into your repository root, try again |
| forgetting `git add .` before committing | `nothing to commit, working tree clean` — even though you definitely changed files | run `git add .`, then `git status` to confirm, then commit |
| committing but never running `git push` | it looks saved, but GitHub still shows last week's version | `git commit` only saves *on your machine* — `git push` is what actually sends it |
| a vague commit message like `"stuff"` | a history that's useless when you actually need to find something in it | describe what changed: `"Week N lab and mini-project"` |
| a `.db` file or real secret gets committed by accident | private data sitting in a public repository, hard to undo | check `git status` before committing; see Week 9 Topic 4 on `.gitignore` |

---

## If something won't cooperate

| Problem | Likely fix |
|---|---|
| `fatal: not a git repository (or any of the parent directories)` | you're not inside your repository — `cd` into it first (Step 0) |
| `git push` rejects your password | GitHub no longer accepts a plain password over HTTPS — use a **personal access token** in its place, or set up SSH (ask if you're stuck — this is a one-time fix) |
| `Everything up-to-date` but your file isn't on GitHub | the commit may not have actually happened — run `git log` and check your message is at the top; if not, repeat Steps 2-4 |
| a merge conflict message | rare if you only ever work from one machine — flag it rather than guessing, this is genuinely worth asking about |
| `git status` shows files you don't recognise | stop before committing — work out what they are first (a stray download, a cache folder) rather than adding them blindly |

---

## The one thing to actually remember

Every week, standing inside your repository folder:

```
git status
git add .
git commit -m "Week N lab and mini-project"
git push
```

Then check GitHub in a browser. If it's there, you're done.
