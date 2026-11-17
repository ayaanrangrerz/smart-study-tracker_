# Smart Study Tracker

A small command-line study planner written in Python. Tasks are stored locally in a JSON file so they remain available between runs.

## Features
- Add a task with a subject
- View tasks and their pending/completed status
- Mark a task complete or delete it
- Save changes to `tasks.json`

## Run
Requires Python 3.

```bash
python smart_study_tracker.py
```

The program creates `tasks.json` in the current working directory when it first saves tasks.

## Notes
This is a learning project and stores data in a local JSON file; it does not sync across devices.
