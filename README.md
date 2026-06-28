# Orphaned Account Detector

A Python automation tool that detects stale and orphaned user accounts by parsing identity exports, calculating inactivity windows, and generating audit reports. Built as a portfolio project to demonstrate IAM security automation skills.

## The Problem

In enterprise environments, user accounts are frequently left active long after an employee leaves or changes roles. These orphaned accounts are a serious security risk, they represent open doors into systems that nobody is actively monitoring. Detecting them manually is slow and error prone at scale.

## What It Does

- Reads a CSV identity export containing usernames, last login dates, account status, and department
- Calculates how many days each account has been inactive
- Flags any account exceeding a configurable inactivity threshold (default: 90 days)
- Generates a timestamped audit report summarizing flagged accounts and overall statistics

## Technologies Used

- Python 3
- csv module (built-in)
- datetime module (built-in)

## How To Run It

1. Clone this repository
2. Make sure Python 3 is installed on your machine
3. Navigate to the project folder in your terminal
4. Run the script:

```bash
python detector.py
```

5. Open `report.txt` to view the generated audit report

## Configuration

The inactivity threshold is set at the top of `detector.py`:

```python
THRESHOLD = 90
```

Change this value to match your organization's account review policy.

## Example Output
