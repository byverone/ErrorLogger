"""This module is designed to create a log file and send an email in the event
    of an error occurring during the monitoring of a program.

Only creates a log file and email if an error occurs.

Parameters:
    sys.argv[1]: str
        path to the log directory of the program being moniterd.
    sys.argv[2:]: list
        list of commands to run the program being monitored.

Returns:
    Log file: file
        log file is dated and named log_YYYY-MM-DD-HH-MM.txt
        it is stored in the logs subdirectory of sys.argv[1].
    Email: email
        email is sent to the email addresses in the recipients list.

Example:
    # run error_logging.py
    python error_logging.py "D:/Examples/example1/logs"
        "D:/Examples/example1/venv/Scripts/python" "D:/Examples/example1/example1.py"
    """

# Standard Lib imports
import sys
from datetime import datetime
import subprocess
from typing import List, Tuple

# Custom Imports
import emailer


def run_command(command: List[str]) -> Tuple[str, str]:
    """This function runs a command and returns the stderr."""
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.stderr


def store_to_file(text: str, path: str) -> None:
    """Stores text to file at path."""
    with open(path, "w", encoding="UTF-8") as file_object:
        file_object.write(text)


if __name__ == "__main__":
    #  get python script's file path
    FILE_PATH = sys.argv[1]

    # run command if no error, exit
    error_text = run_command(sys.argv[2:])
    if error_text == "":
        sys.exit()

    # send email
    email_subject = f"Error Logged to {FILE_PATH}"
    recipients = ["username@example.com"]
    emailer.send_email(recipients, "errorlogger@example.com", email_subject, error_text)

    # log file name and path
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_date_name = f"log_{date}.txt"
    log_file_path = f"{FILE_PATH}\\{log_date_name}"  # \\logs
    # store log to file
    store_to_file(error_text, log_file_path)
