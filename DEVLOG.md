# Development Log

## Template
**Did:**
**Learned:** 
**Problems:** 
**Next:** 

## 2026-11-04 — Session 1
**Did:** 
- Created Base Repo Structure

**Learned:**
- RFC3164 SSH log format attributes

**Problems:**
- Need to learn how to create a global object that is divided in 3 parts
    - Time
    - Host
    - Message


**Next:**
- Create Object Class 

## 2026-11-04 — Session 2
**Did:**
- Created the LogEntry class (time, host, msg) with getter functions
- Set up a tests folder and wrote the first pytest test for LogEntry
- Added pyproject.toml so pytest can find project modules

**Learned:**
- The constructor must be named `__init__` (double underscores), otherwise it never runs
- How Python finds modules, and why tests in a subfolder hit `ModuleNotFoundError`
- pytest finds tests by the `test_` prefix and checks results with `assert`

**Problems:**
- Constructor didn't run because it was named `_init_`
- Test couldn't import LogEntry from the tests folder; fixed with `pythonpath` in pyproject.toml

**Next:**
- Tidy up: use `self`, lowercase file/folder names, test the getter functions
- Start read_3164: read the log file line by line
