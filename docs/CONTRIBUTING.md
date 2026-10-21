# Contribution guide — four-person ROSPL team

Each person should make **their own real changes and commits**. A shared repository does not automatically prove four contributions.

## Team roles (assign actual names after your group decides)

| Member | Owned module | Suggested independent contribution |
|---|---|---|
| Member 1 | `templates/index.html`, `static/css/style.css` | Responsive layout, accessibility improvements, mobile UI |
| Member 2 | `static/js/game.js` | Card matching, timer, hint, difficulty, animations |
| Member 3 | `app.py`, `game_rules.py` | Flask routes, SQLite leaderboard, server-side scoring and validation |
| Member 4 | `tests/test_app.py`, `.github/workflows/tests.yml`, documentation | Automated tests, CI workflow, help docs and QA |

The starter includes the initial implementation of **all** these modules. To demonstrate legitimate teamwork, each student should now implement and test a real enhancement on their own branch. Do not claim a member authored starter code they did not write.

## Collaboration workflow

1. One team member creates a **new GitHub repository** and uploads this starter as the initial commit.
2. Invite the other three students using GitHub **Settings → Collaborators**.
3. Each student clones the repository, then creates a new branch:
   `git switch -c feature/member2-keyboard-controls`.
4. Each student implements an actual change in their assigned module and tests it.
5. Commit under their own GitHub identity: `git add ...` followed by `git commit -m "Add keyboard card controls"`.
6. Push their branch: `git push -u origin feature/member2-keyboard-controls`.
7. Open a Pull Request on GitHub, get another member to review it, then merge.
8. Put each **real PR link** and a screenshot in the ROSPL logbook.

### Good follow-up contribution ideas

- Member 1: improve contrast and keyboard focus on mobile.
- Member 2: add difficulty-specific preview countdown or keyboard card navigation.
- Member 3: add score filters and pagination, or rate limiting.
- Member 4: add JavaScript unit tests, end-to-end browser tests, and CI evidence.

### Review checklist

- [ ] Feature actually works in the browser.
- [ ] Python tests pass: `python -m pytest -q`.
- [ ] No secrets, database files, or virtual environments committed.
- [ ] PR explains what changed and includes screenshots.
- [ ] Each teammate has their own commits and at least one meaningful reviewed PR.
