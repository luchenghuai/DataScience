# DataScience

A day-by-day Python / data science learning log, published as a website with [Hugo](https://gohugo.io/).

🌐 **Live site:** https://luchenghuai.github.io/DataScience/

## Clone the repo

```bash
git clone git@github.com:luchenghuai/DataScience.git
```

## Contents
![VS Code editing a Python file](img/vscode_page.png)

## How publishing works

1. This repo uses Hugo to build and publish the site at [luchenghuai.github.io/DataScience](https://luchenghuai.github.io/DataScience/).
2. You don't need to run Hugo yourself — a GitHub Actions workflow builds and deploys the site automatically.
3. Edit files and push your changes to `main`. GitHub Actions will build a new version of the site and update the link shown on the repo page:

   ![Repo page showing the published site link](img/hugo_url.png)

4. To check whether the build succeeded, open the **Actions** tab and look for a green checkmark next to your commit:

   ![GitHub Actions run status](img/action.png)



5. If a build fails (red ❌), click into the run to see the error, fix the issue in your files, and push again.

## How to use git to check recent changes

1. **See which files have changed but aren't tracked or staged yet:** `git status`

   ```
   $ git status
   On branch main
   Your branch is up to date with 'origin/main'.

   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
       modified:   README.md
       modified:   git_demo.txt

   Untracked files:
     (use "git add <file>..." to include in what will be committed)
       .DS_Store
       readme.txt

   no changes added to commit (use "git add" and/or "git commit -a")
   ```

2. **See what you've changed but haven't committed yet:** `git diff`

   ```
   $ git diff
   diff --git a/git_demo.txt b/git_demo.txt
   index 08fe272..06fcdd7 100644
   --- a/git_demo.txt
   +++ b/git_demo.txt
   @@ -1 +1,2 @@
    first line
   +second line
   ```

   `+` marks a line that was added, `-` marks a line that was removed.

3. **See your commit history:** `git log`

   ```
   $ git log
   commit 96e6ad54681f323b8d2af5a77dce8248d2e870f0 (HEAD -> main, origin/main)
   Author: Chenghuai Lu <chenghuai_lu@apple.com>
   Date:   Fri Jul 10 12:12:48 2026 -0700

       dad's 1st commit

   commit f3eca6a4f5350144a8f226a74d317aed7159fdaf
   Author: Chenghuai Lu <chenghuai_lu@apple.com>
   Date:   Fri Jul 10 12:06:00 2026 -0700

       fix
   ```

4. **See everything that changed since a specific commit:** copy that commit's hash from `git log`, then run `git diff <hash>..`

   ```
   $ git diff 4551e53856d1c3c173cbad14c8545568dc05d55b..
   diff --git a/git_demo.txt b/git_demo.txt
   new file mode 100644
   index 0000000..08fe272
   --- /dev/null
   +++ b/git_demo.txt
   @@ -0,0 +1 @@
   +first line
   diff --git a/img/action.png b/img/action.png
   new file mode 100644
   index 0000000..0471ca0
   Binary files /dev/null and b/img/action.png differ
   diff --git a/img/hugo_url.png b/img/hugo_url.png
   new file mode 100644
   index 0000000..19cc2fd
   Binary files /dev/null and b/img/hugo_url.png differ
   ```

   This tells us: `git_demo.txt` was created with one line, and `action.png` / `hugo_url.png` were added.
