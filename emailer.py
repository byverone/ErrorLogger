"""This module is used to send emails using the smtplib module."""

# Standard Lib imports
import smtplib
import os
from typing import List
from email.message import EmailMessage

# 3rd Party Imports
from dotenv import load_dotenv

# loads the environment variables
load_dotenv(r"Path\to\emailer.env")

def send_email(
    toaddress: List[str] | str, fromaddress: str, subject: str, body: str
) -> None:
    """This function is used to send emails using the smtplib module.

    Args:
        toaddress: A list of email addresses to send the email to.
        fromaddress: The email address of the sender.
        subject: The subject of the email.
        body: The body of the email.

    Returns:
        None
    """

    # gets the email credentials from the environment variables
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    smtp_server = "smtp.office365.com"
    port = 587

    # creates the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = fromaddress
    msg["To"] = ", ".join(toaddress) if isinstance(toaddress, list) else toaddress

    # starts the smtp server and closes it after sending the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.close()
