# ROSPL project report notes

**Title:** Memory Match Arena — A Flask-Based Interactive Memory Game With Leaderboard

**Category:** Web application / educational game / open-source group project

**Application domain:** Casual gaming and cognitive skill practice

**Technical domain:** Python Flask, HTML/CSS/JavaScript, SQLite, Git/GitHub, pytest and CI

## Problem statement
Provide a lightweight, visually appealing browser-based memory matching game with multiple difficulty levels, score tracking and persistent rankings that can be developed collaboratively by a four-person team.

## Objective
Develop a working web game, use server-side validation to store results, test API behavior, and demonstrate genuine GitHub collaboration through independent branches and pull requests.

## System architecture
Browser (HTML/CSS/JS) → Flask HTTP API → SQLite database. The browser handles live card interactions; Flask validates and calculates scores before saving them. `/api/leaderboard` reads sorted results from the database.

## Modules
1. UI and responsive design
2. Game logic, timer, moves, difficulty and hints
3. Flask API, scoring and SQLite leaderboard
4. Testing, continuous integration and documentation

## Screenshots to capture
1. New game (easy difficulty)
2. A matched pair and move counter
3. Completed game modal and final score
4. Leaderboard after saving a score
5. Passing pytest command
6. GitHub branches, PR reviews and merged PRs **only once they actually exist**

## Evaluation and limits
Test API rejection of invalid JSON/player names, persistence of valid scores, board size per difficulty, timer and hints. Note that client results can be forged without server-owned game sessions. Do not claim actual GitHub contributions before the team members submit them.

## Suggested demo
Start Flask; show easy/medium/hard cards; finish easy, save score; refresh leaderboard; demonstrate tests; show each member's GitHub PR.
