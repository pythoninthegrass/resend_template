#!/usr/bin/env python

import markdown
import resend
from decouple import config
from pathlib import Path
from textwrap import dedent

# env vars
resend_api_key = config("RESEND_API_KEY")
resend_from = config("RESEND_FROM", default="Acme <onboarding@resend.dev>")
resend_to = config("RESEND_TO", default="delivered@resend.dev")
resend_subject = config("RESEND_SUBJECT", default="Hello, world!")
markdown_file = config("MARKDOWN_FILE", default="EMAIL.md")
use_markdown_file = config("USE_MARKDOWN_FILE", default=False, cast=bool)

# email content
if use_markdown_file:
    print(f"Using {markdown_file} file")
    msg = Path(markdown_file).read_text()
else:
    print("Using hardcoded markdown")
    msg = dedent("""
    # Hello, world!

    This is a **test email** from [Resend](https://resend.com).

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    ./send_email.py
    ```
    """).lstrip()

html = markdown.markdown(msg, extensions=["fenced_code"])

resend.api_key = resend_api_key

params: resend.Emails.SendParams = {
    "from": resend_from,
    "to": [resend_to],
    "subject": resend_subject,
    "html": html,
}

# TODO: fix bare except
def main():
    try:
        email: resend.Email = resend.Emails.send(params)
        print("Email sent successfully!")
        print(email)
    except Exception as e:
        print("Error sending email:")
        print(e)

if __name__ == "__main__":
    main()
