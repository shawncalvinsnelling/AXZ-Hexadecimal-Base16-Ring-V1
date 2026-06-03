# GitHub publishing checklist

1. Create the repository with no README, no .gitignore, and no license selected.
2. Upload all package contents.
3. Ensure `.github/workflows/verify.yml` and `.gitignore` are present.
4. If hidden files do not upload, copy from `VISIBLE_GITHUB_ACTIONS_verify.yml` and `VISIBLE_GITIGNORE.txt`.
5. Wait for GitHub Actions to pass.
6. Publish release `v1.0.0`.
