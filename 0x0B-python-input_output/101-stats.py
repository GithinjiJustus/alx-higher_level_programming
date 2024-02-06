#!/usr/bin/python3
"""
101-stats
"""

import signal
import sys

def print_stats(total_size, status_codes):
    """Print statistics based on total file size and status codes."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(signal, frame):
    """Handle keyboard interrupt (CTRL + C)."""
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            total_size += int(parts[-1])
            status_codes[parts[-2]] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    pass

print_stats(total_size, status_codes)
