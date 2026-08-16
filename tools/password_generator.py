import hashlib
import urllib.request
import urllib.error
import socket
import secrets
import string
import base64
import time
import ssl
import random
import whois
import json
import os
from datetime import datetime
from contextlib import redirect_stdout
import io
import sys
import dns.resolver
import socket
import ssl
import time

def password_generator():

    while True:

        print("""
        =========================
          Password Generator
        =========================

        B = Back
        E = Exit
        """)

        length_input = input(
            "Enter password length: "
        )

        if length_input.lower() == "b":
            return "back"

        if length_input.lower() == "e" or length_input.lower() == "exit":
            return "exit"

        try:
            length = int(length_input)

        except ValueError:
            print("Please enter a valid number!")
            continue

        uppercase = input(
            "Include uppercase letters? (y/n): "
        )

        lowercase = input(
            "Include lowercase letters? (y/n): "
        )

        numbers = input(
            "Include numbers? (y/n): "
        )

        symbols = input(
            "Include symbols? (y/n): "
        )

        characters = ""
        password = ""

        # Uppercase
        if uppercase.lower() == "y":
            characters += string.ascii_uppercase
            password += secrets.choice(
                string.ascii_uppercase
            )

        # Lowercase
        if lowercase.lower() == "y":
            characters += string.ascii_lowercase
            password += secrets.choice(
                string.ascii_lowercase
            )

        # Numbers
        if numbers.lower() == "y":
            characters += string.digits
            password += secrets.choice(
                string.digits
            )

        # Symbols
        if symbols.lower() == "y":
            characters += string.punctuation
            password += secrets.choice(
                string.punctuation
            )

        # No character type selected
        if characters == "":
            print(
                "\nYou must select at least one "
                "character type!"
            )
            continue

        # Password too short
        if length < len(password):
            print(
                f"\nPassword length must be at least "
                f"{len(password)}!"
            )
            continue

        # Complete password
        for i in range(length - len(password)):
            password += secrets.choice(characters)

        # Shuffle password
        password = list(password)

        secrets.SystemRandom().shuffle(password)

        password = "".join(password)

        print("\nGenerated password:")
        print(password)
        print()
