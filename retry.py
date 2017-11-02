#!/usr/bin/env python3
#
# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/subprocess.html

import argparse
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("command", help="The command to be retried.")
parser.add_argument("--max_attempts", help="The maximum number of attempts before giving up.")
parser.add_argument("--timeout_seconds", help="Timeout for each run in second.")

args = parser.parse_args()

max_attempts = int(args.max_attempts)
timeout_seconds = int(args.timeout_seconds)
command = args.command.split(' ')

print("Running commands: %s" % ' '.join(command))
print("Timeout:          %d seconds" % timeout_seconds)
print("Max attempt:      %d times" % max_attempts)
print("")

attempt = 1

while attempt < max_attempts:
    print("========== Attempt %d Start ==========" % attempt)
    completed_process = subprocess.run(
        args=command,
        timeout=timeout_seconds,
    )
    print("========== Attempt %d Finished ==========" % attempt)
    print("Return code: %d" % completed_process.returncode)
    print("")

    if completed_process.returncode != 0:
        attempt += 1
        time.sleep(1)
    else:
        break
