#!/usr/bin/env python3
import sys
import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: logger.py <logfilename>")
        sys.exit(1)
    log_filename = sys.argv[1]
    with open(log_filename, 'a') as logfile:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.strip()
            if line == "QUIT":
                break
            if not line:
                continue
            parts = line.split(maxsplit=1)
            if len(parts) == 1:
                action = parts[0]
                message = ""
            else:
                action, message = parts
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M")
            log_entry = f"{timestamp} [{action}] {message}\n"
            logfile.write(log_entry)
            logfile.flush()

if __name__ == "__main__":
    main()
