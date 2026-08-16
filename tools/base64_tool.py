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

def Base64_Tool():

    while True:

        print("""
        ========================
             Base64 Tool
        ========================

        1. Encode
        2. Decode

        B. Back
        E. Exit
        """)

        option = input("Enter your option: ")

        if option.lower() == "b":
            return "back"

        if option.lower() == "e" or option.lower() == "exit":
            return "exit"

        # Encode
        if option == "1":

            text = input("Enter text: ")

            encoded = base64.b64encode(
                text.encode("utf-8")
            ).decode("utf-8")

            print("\nEncoded:")
            print(encoded)

        # Decode
        elif option == "2":

            text = input("Enter Base64: ")

            try:
                decoded = base64.b64decode(
                    text
                ).decode("utf-8")

                print("\nDecoded:")
                print(decoded)

            except Exception:
                print("\nInvalid Base64!")
