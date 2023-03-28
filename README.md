# ErrorLogger

This Python module monitors a program and creates a log file and sends an email in the event of an error. The log file is saved in the specified log directory and is named with a timestamp. The email is sent to the recipients list. This module will only create a log file and send an email if an error occurs. The module requires the path to the log directory of the program being monitored and the commands required to run the program.

## Returns
* Log file: file
* log file is dated and named log_YYYY-MM-DD-HH-MM.txt it is stored in the logs subdirectory of sys.argv[1].
* Email: email
* email is sent to the email addresses in the recipients list.

## How To Use

1. Create a **emailer.env** file With the following Variables
  * **EMAIL_SENDER** : "sender@example.com"
  * **EMAIL_PASSWORD** : "Password"

* Parameters:
  * sys.argv[1]: str
  * path to the log directory of the program being moniterd.
  * sys.argv[2:]: list
  * list of commands to run the program being monitored.

* Examples:
  * python error_logging.py sys.argv[1] sys.argv[2:]
  * python error_logging.py "D:/Examples/example1/logs" "D:/Examples/example1/venv/Scripts/python" "D:/Examples/example1/example1.py"

## Future Features

* Generate a bugtracker ticket on Github, Zoho, etc. (Most will require api use)
* Create a bash and Ps1 scripts to manage the error_logger.py
* Track statistics about the underlying program being ran (time, ramUsage, etc.) store either in logs or sqllite.
