#!/bin/bash

LOG_FILE="data/server.log"
REPORT_FILE="reports/error-report.txt"

{
    echo "LINUX SERVER LOG ANALYSIS REPORT"
    echo "================================"
    echo
    echo "Dataset: $LOG_FILE"
    echo "Total Requests: $(wc -l < "$LOG_FILE")"
    echo

    echo "HTTP STATUS SUMMARY"
    echo "-------------------"
    awk '{print $6}' "$LOG_FILE" | sort | uniq -c | sort -nr
    echo

    echo "TOP ERROR-GENERATING IP"
    echo "-----------------------"
    awk '$6 != 200 {print $3}' "$LOG_FILE" |
        sort | uniq -c | sort -nr | head -5
    echo

    echo "TOP ERROR-ENDPOINTS"
    echo "-------------------"
    awk '$6 != 200 {print $5}' "$LOG_FILE" |
        sort | uniq -c | sort -nr
    echo
} > "$REPORT_FILE"

echo "Report generated: $REPORT_FILE"
