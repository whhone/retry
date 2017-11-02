# retry

Utility to retry a command until succeed.

## Usage
```
usage: retry.py [-h] [--max_attempts MAX_ATTEMPTS]
                [--timeout_seconds TIMEOUT_SECONDS]
                -- command

positional arguments:
  command               The command to be retried.

optional arguments:
  -h, --help            show this help message and exit
  --max_attempts MAX_ATTEMPTS
                        The maximum number of attempts before giving up.
  --timeout_seconds TIMEOUT_SECONDS
                        Timeout for each run in second.
```

## Examples
```
./retry.py --max_attempts=10 -- false
./retry.py --max_attempts=10 --timeout_seconds=5 -- sleep 10
```
