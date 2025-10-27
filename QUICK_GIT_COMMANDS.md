# ⚡ Quick Git Commands Reference

## 🚀 Initial Push (Copy-Paste All)

```bash
cd "farmer system"
git init
git add .
git commit -m "Initial commit: Farm Management System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/farm-management-system.git
git push -u origin main
```

**⚠️ Replace YOUR_USERNAME with your GitHub username!**

---

## 🔄 Daily Workflow

### Check Status
```bash
git status
```

### Add Changes
```bash
# Add all files
git add .

# Add specific file
git add filename.py
```

### Commit Changes
```bash
git commit -m "Brief description of changes"
```

### Push to GitHub
```bash
git push
```

### Pull from GitHub
```bash
git pull
```

---

## 🌿 Branch Operations

### Create New Branch
```bash
git checkout -b feature-name
```

### Switch Branch
```bash
git checkout branch-name
```

### List Branches
```bash
git branch
```

### Merge Branch
```bash
git checkout main
git merge feature-name
```

### Delete Branch
```bash
git branch -d feature-name
```

---

## 📝 Commit Message Examples

```bash
# Good commit messages
git commit -m "Add user authentication feature"
git commit -m "Fix farmer deletion bug"
git commit -m "Update README with installation steps"
git commit -m "Add test cases for agro products"
git commit -m "Improve database query performance"

# Bad commit messages (avoid)
git commit -m "update"
git commit -m "fix"
git commit -m "changes"
```

---

## 🔍 View History

### View Commits
```bash
git log
```

### View Compact Log
```bash
git log --oneline
```

### View Specific File History
```bash
git log filename.py
```

---

## ↩️ Undo Changes

### Undo Last Commit (keep changes)
```bash
git reset --soft HEAD~1
```

### Undo Last Commit (discard changes)
```bash
git reset --hard HEAD~1
```

### Discard Local Changes
```bash
git checkout -- filename.py
```

### Discard All Local Changes
```bash
git reset --hard
```

---

## 🔧 Configuration

### View Config
```bash
git config --list
```

### Set User Name
```bash
git config --global user.name "Your Name"
```

### Set Email
```bash
git config --global user.email "your.email@example.com"
```

---

## 🌐 Remote Operations

### View Remote
```bash
git remote -v
```

### Add Remote
```bash
git remote add origin URL
```

### Change Remote URL
```bash
git remote set-url origin NEW_URL
```

### Remove Remote
```bash
git remote remove origin
```

---

## 🆘 Troubleshooting Commands

### Fix "failed to push"
```bash
git pull origin main --rebase
git push origin main
```

### Fix "divergent branches"
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### Force Push (use carefully!)
```bash
git push -f origin main
```

### Clean Untracked Files
```bash
git clean -fd
```

---

## 📊 Status & Diff

### Show Status
```bash
git status
```

### Show Differences
```bash
git diff
```

### Show Staged Differences
```bash
git diff --staged
```

### Show Differences for Specific File
```bash
git diff filename.py
```

---

## 🏷️ Tags

### Create Tag
```bash
git tag v1.0.0
```

### Push Tag
```bash
git push origin v1.0.0
```

### List Tags
```bash
git tag
```

### Delete Tag
```bash
git tag -d v1.0.0
```

---

## 💡 Useful Aliases

Add these to your git config for shortcuts:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
```

Then use:
```bash
git st      # instead of git status
git co main # instead of git checkout main
git br      # instead of git branch
git ci      # instead of git commit
```

---

## 📅 Complete Update Workflow

```bash
# 1. Check current status
git status

# 2. Pull latest changes
git pull

# 3. Make your changes to files
# ... edit files ...

# 4. Check what changed
git status

# 5. Add changes
git add .

# 6. Commit changes
git commit -m "Description of changes"

# 7. Push to GitHub
git push

# 8. Verify on GitHub
```

---

## 🎯 Best Practices

✅ **DO**
- Commit often with clear messages
- Pull before you push
- Use branches for new features
- Keep commits small and focused
- Write descriptive commit messages

❌ **DON'T**
- Commit sensitive data (passwords, keys)
- Force push to main branch
- Commit large binary files
- Use vague commit messages
- Work directly on main branch

---

## 📚 Quick Reference

| Command | Description |
|---------|-------------|
| `git init` | Initialize repository |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
| `git push` | Push to remote |
| `git pull` | Pull from remote |
| `git status` | Check status |
| `git log` | View history |
| `git branch` | List branches |
| `git checkout -b name` | Create branch |
| `git merge branch` | Merge branch |

---

## 🔗 Useful Links

- Git Docs: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

**Keep this reference handy! 📌**

