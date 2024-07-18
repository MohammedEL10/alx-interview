#!/usr/bin/python3


import sys
from collections import defaultdict

def print_metrics(total_size, status_code_counts):
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

def main():
    total_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            # Example line: 192.168.0.1 - [18/Sep/2023:15:34:34 +0000] "GET /projects/260 HTTP/1.1" 200 1234
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = parts[-1]
                try:
                    file_size = int(file_size)
                except ValueError:
                    continue  # Skip if file size is not an integer

                if status_code.isdigit():
                    status_code = int(status_code)
                    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        total_size += file_size
                        status_code_counts[status_code] += 1
                        line_count += 1

                        if line_count % 10 == 0:
                            print_metrics(total_size, status_code_counts)
                            print()  # Just for readability

    except KeyboardInterrupt:
        pass  # Handle KeyboardInterrupt (CTRL + C)

    # Print final metrics before exiting
    print_metrics(total_size, status_code_counts)

if __name__ == "__main__":
    main()
