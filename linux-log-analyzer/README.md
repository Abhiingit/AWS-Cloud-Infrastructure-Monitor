# Linux Server Log Analyzer

A hands-on Linux practical project built using Ubuntu in Docker.

This project demonstrates Linux filesystem navigation, file operations, permissions, ownership, Bash scripting, and command-line log analysis.

## Problem

Analyze a server log dataset and answer:

- How many requests were successful or failed?
- Which client IP generated the most errors?
- Which endpoints generated the most errors?

## Project Structure

linux-log-analyzer/
|-- data/
|   |-- server.log
|-- reports/
|   |-- error-report.txt
|-- scripts/
    |-- analyze.sh
## Linux Concepts Practiced

Filesystem and Navigation:
- pwd
- ls
- cd
- Absolute and relative paths
- Linux filesystem hierarchy

File Operations:
- mkdir
- touch
- cp
- mv
- rm
- cat

Permissions and Ownership:
- chmod
- chown
- rwx permissions
- Numeric permissions: 755, 644, 700
- Linux file types

Log Analysis:
- awk
- sort
- uniq
- Linux command pipelines

Bash Scripting:
- Bash scripts
- Executable permissions
- Automatic report generation

## Dataset

The sample dataset contains 93 server requests with:

- Client IP addresses
- HTTP methods
- Endpoints
- HTTP status codes
- Timestamps

Example:

2026-09-03 09:01:12 192.168.1.10 GET / 200

## Analysis Results

HTTP Status Summary:

200 Successful     : 69
401 Unauthorized   : 6
404 Not Found      : 11
500 Server Error   : 7

Total Requests: 93

Top Error-Generating IP:

192.168.1.17 -> 4 failed requests

Top Error Endpoints:

/products/999 -> 7
/checkout     -> 7
/login        -> 6
/unknown      -> 3
/favicon.ico  -> 1

## Automated Analysis

The analysis script:

./scripts/analyze.sh

reads:

data/server.log

and generates:

reports/error-report.txt

Workflow:

Server Log
    |
    v
Bash Script
    |
    v
awk / sort / uniq
    |
    v
Analysis
    |
    v
Error Report

## Permissions Demonstration

The analysis script was initially created without execute permission:

-rw-r--r--

It was then made executable using:

chmod +x scripts/analyze.sh

Result:

-rwxr-xr-x

The script was then executed using:

./scripts/analyze.sh

## Key Learning Outcomes

- Understanding the Linux filesystem hierarchy
- Navigating Linux directories
- Managing files and directories
- Understanding Linux permissions and ownership
- Using command pipelines for data processing
- Writing and executing Bash scripts
- Performing basic server log analysis
- Generating a reproducible analysis report

## Environment

- Ubuntu 24.04
- Docker Desktop
- Bash
- Windows 11

## Author

Hands-on Linux and Cloud learning project.

Linux | Bash | Docker | Cloud | DevOps