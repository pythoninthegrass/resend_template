# resend_template

This is a template for sending emails with [Resend](https://resend.com).

Instead of hardcoding emails as inline HTML, you can use a Markdown file to customize the email content.

It extends environment variables to read from both the `.env` file and the command line.

## Minimum Requirements

* [python 3.11+](https://www.python.org/downloads/)

## Recommended Requirements

* [devbox](https://www.jetpack.io/devbox/docs/quickstart/)
* [asdf](https://asdf-vm.com/)
* [poetry](https://python-poetry.org/docs/)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Setup

* Create [DNS records](https://resend.com/docs/dashboard/domains/introduction) for your domain to work with Resend.

## Usage

* Fill out `.env` with your Resend API key and from, to, and subject fields.
  * To use a custom DNS domain, fill out `RESEND_FROM`:
    ```
    RESEND_FROM='First Last <user@custom_domain>'
    ```
* Either edit the docstring for `msg` in `send_email.py` or use the `MARKDOWN_FILE` environment variable to specify a markdown file, then set `USE_MARKDOWN_FILE` to `True`.
  * For the latter, fill out `EMAIL.md` with your email content. 
* Then run via

    ```bash
    ./send_email.py
    ```

* Once finished, deactivate the virtual environment via

    ```bash
    deactivate
    ```
