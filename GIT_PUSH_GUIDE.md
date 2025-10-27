# Git Push Guide - Farm Management System

## Prerequisites

Before pushing to Git, ensure you have:
- Git installed on your system
- GitHub/GitLab/Bitbucket account created
- Repository created on your Git platform

---

## Step-by-Step Guide

### Step 1: Install Git (if not already installed)

**Windows:**
1. Download Git from: https://git-scm.com/download/win
2. Run the installer
3. Use default settings

**Verify installation:**
```bash
git --version
```

---

### Step 2: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### Step 3: Create a Repository on GitHub/GitLab

1. Go to GitHub (https://github.com)
2. Click "New Repository" or "+"
3. Enter repository name: `farm-management-system`
4. Description: `Web-based Farm Management System with Flask and MySQL`
5. Choose Public or Private
6. **DO NOT** initialize with README, .gitignore, or license
7. Click "Create Repository"

---

### Step 4: Initialize Git in Your Project

Open terminal/command prompt in the project directory:

```bash
# Navigate to project directory
cd "farmer system"

# Initialize git repository
git init
```

---

### Step 5: Add Files to Git

```bash
# Add all files to staging
git add .

# Check status
git status
```

---

### Step 6: Create Initial Commit

```bash
# Commit with message
git commit -m "Initial commit: Farm Management System with testing framework"
```

---

### Step 7: Connect to Remote Repository

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values:

```bash
# For GitHub
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# For GitLab
git remote add origin https://gitlab.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# For Bitbucket
git remote add origin https://YOUR_USERNAME@bitbucket.org/YOUR_USERNAME/YOUR_REPO_NAME.git
```

**Verify remote:**
```bash
git remote -v
```

---

### Step 8: Push to Remote Repository

```bash
# Push to main branch (or master depending on your setup)
git push -u origin main

# If you get an error about 'main' branch, try:
git branch -M main
git push -u origin main
```

**Note:** You may be prompted for your username and password/token.

---

### Step 9: Authentication

#### Using Personal Access Token (Recommended)

**GitHub:**
1. Go to Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Select scopes: `repo` (full control)
4. Copy the token
5. Use token as password when pushing

**Alternative: Using SSH**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add SSH key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy SSH key (Windows)
clip < ~/.ssh/id_ed25519.pub

# Add SSH key to GitHub: Settings → SSH and GPG keys → New SSH key
```

Then update remote URL:
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
```

---

## Quick Reference Commands

### Common Git Commands

```bash
# Check status
git status

# Add specific file
git add filename.py

# Add all files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to remote
git push

# Pull from remote
git pull

# View commit history
git log

# Create new branch
git checkout -b feature-branch-name

# Switch branches
git checkout branch-name

# Merge branch
git merge branch-name
```

---

## Complete Command Sequence (Copy-Paste Ready)

```bash
# 1. Navigate to project
cd "farmer system"

# 2. Initialize git
git init

# 3. Add all files
git add .

# 4. Initial commit
git commit -m "Initial commit: Farm Management System with testing framework"

# 5. Add remote (replace with your URL)
git remote add origin https://github.com/YOUR_USERNAME/farm-management-system.git

# 6. Rename branch to main
git branch -M main

# 7. Push to remote
git push -u origin main
```

---

## For Subsequent Pushes

After initial setup, use these commands for future changes:

```bash
# 1. Check what changed
git status

# 2. Add changes
git add .

# 3. Commit with message
git commit -m "Description of changes"

# 4. Push to remote
git push
```

---

## Troubleshooting

### Error: "failed to push some refs"

```bash
# Pull changes first
git pull origin main --rebase

# Then push
git push origin main
```

### Error: "repository not found"

- Check remote URL: `git remote -v`
- Verify repository exists on GitHub/GitLab
- Check repository name spelling

### Error: "permission denied"

- Verify authentication token/SSH key
- Check repository access permissions
- Re-generate access token if expired

### Error: "refusing to merge unrelated histories"

```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

---

## Creating README for GitHub

Create a `README.md` file in your project root:

```bash
# Create README
echo "# Farm Management System" > README.md

# Add and commit
git add README.md
git commit -m "Add README"
git push
```

---

## Best Practices

1. **Commit Often**: Make small, frequent commits
2. **Descriptive Messages**: Use clear commit messages
3. **Branch Strategy**: Use branches for new features
4. **Pull Before Push**: Always pull before pushing
5. **Review Changes**: Use `git status` and `git diff`
6. **.gitignore**: Keep sensitive data out of version control

---

## Example Workflow

```bash
# Start working on new feature
git checkout -b feature-new-report

# Make changes to files
# ... edit files ...

# Stage changes
git add .

# Commit changes
git commit -m "Add new report generation feature"

# Push feature branch
git push -u origin feature-new-report

# Switch back to main
git checkout main

# Merge feature (after testing)
git merge feature-new-report

# Push to main
git push
```

---

## Repository Structure Recommendation

```
farm-management-system/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── farmers.sql
├── tests/
│   ├── test_auth.py
│   ├── test_farmer.py
│   └── test_config.py
├── templates/
├── static/
└── Documentation/
    ├── TEST_PLAN.md
    ├── TEST_CASES.md
    └── TESTING_README.md
```

---

## Additional Resources

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

**Happy Coding! 🚀**

