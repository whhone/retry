#!/usr/bin/env python3
#
# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/subprocess.html

import argparse
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("command", help="The command to be retried.",
                    nargs='+')
parser.add_argument("--max_attempts", help="The maximum number of attempts before giving up.",
                    type=int, default=1024)
parser.add_argument("--timeout_seconds", help="The timeout, in second, for each run.",
                    type=int, default=None)
parser.add_argument("--interval_seconds", help="The interval, in second, after a failed run.",
                    type=int, default=1)
args = parser.parse_args()

print("Running commands:  %s" % ' '.join(args.command))
print("Max # of attempts: %d times" % args.max_attempts)
print("Failed interval:   %d seconds" % args.interval_seconds)
if args.timeout_seconds:
    print("Timeout:           %d seconds" % args.timeout_seconds)

print("")

attempt = 1
while attempt < args.max_attempts:
    print("========== Attempt %d Start ==========" % attempt)
    print("Running: " + ' '.join(args.command))
    print("STDOUT: ")
    completed_process = subprocess.run(
        args=args.command,
        timeout=args.timeout_seconds,
    )
    print("========== Attempt %d Finished ==========" % attempt)
    print("Return code: %d" % completed_process.returncode)
    print("")

    if completed_process.returncode != 0:
        attempt += 1
        time.sleep(args.interval_seconds)
    else:
        break
