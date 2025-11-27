# GitHub Metadata

This directory contains GitHub-specific configuration and templates.

## 📁 Contents

### Issue Templates

**Location:** `ISSUE_TEMPLATE/`

- **bug_report.md** - Template for reporting bugs
- **feature_request.md** - Template for suggesting new features

When users create issues, they'll be prompted to use these templates, ensuring consistent and complete bug reports and feature requests.

### Workflows

**Location:** `workflows/`

- **python-package.yml** - CI workflow for automated testing
  - Runs on push to main and pull requests
  - Tests across Python 3.8, 3.9, 3.10, 3.11
  - Lints code with flake8
  - Ensures code quality

### Funding

**Location:** `FUNDING.yml`

Links to my published book on Amazon:
**["Fiber Optics: A Comprehensive Guide"](https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/)**

Displays a "Sponsor" button on the repository with a link to support.

## 🎯 Purpose

These files enhance the GitHub experience by:

1. **Standardizing Issues** - Templates ensure bug reports and feature requests contain all necessary information
2. **Automating Quality Checks** - CI workflow runs automatically on every push
3. **Supporting the Author** - Funding link provides easy access to the companion book

## 🔧 Customization

All templates and workflows can be customized:

- **Issue Templates:** Modify markdown files in `ISSUE_TEMPLATE/`
- **CI Workflow:** Edit `workflows/python-package.yml`
- **Funding:** Update `FUNDING.yml` with additional platforms

## 📚 GitHub Documentation

- [Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Funding Configuration](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)

---

**Professional GitHub configuration for open-source fiber optics toolkit** ⚙️
