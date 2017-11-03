import subprocess
import time


class Retryer(object):

    def __init__(self, command, max_attempts=1024, interval_seconds=1, timeout_seconds=None):
        self.command = command
        self.max_attempts = max_attempts
        self.interval_seconds = interval_seconds
        self.timeout_seconds = timeout_seconds
        self.attempt = 0

    def start(self):
        while self.attempt < self.max_attempts:
            print("========== Attempt %d Start ==========" % self.attempt)
            print("Running: " + ' '.join(self.command))
            print("STDOUT: ")

            completed_process = self.run_command_once()

            print("========== Attempt %d Finished ==========" % self.attempt)
            print("Return code: %d" % completed_process.returncode)
            print("")

            if completed_process.returncode != 0:
                self.attempt += 1
                time.sleep(self.interval_seconds)
            else:
                break

    def run_command_once(self) -> subprocess.CompletedProcess:
        """Runs the command once."""
        return subprocess.run(
            args=self.command,
            timeout=self.timeout_seconds,
        )
