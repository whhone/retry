#!/usr/bin/env python3
#
# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/subprocess.html

import argparse

from retryer import Retryer

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


def main():
    print("Running commands:  %s" % ' '.join(args.command))
    print("Max # of attempts: %d times" % args.max_attempts)
    print("Failed interval:   %d seconds" % args.interval_seconds)
    if args.timeout_seconds:
        print("Timeout:           %d seconds" % args.timeout_seconds)

    print("")

    retryer = Retryer(
        command=args.command,
        max_attempts=args.max_attempts,
        interval_seconds=args.interval_seconds,
        timeout_seconds=args.timeout_seconds)

    retryer.start()


if __name__ == "__main__":
    exit(main())
