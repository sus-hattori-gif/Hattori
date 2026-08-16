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

def hasher():

    while True:

    
        text = input("Enter text :(B = back, E = exit): ")

        if text.lower() == "b":
            return "back"

        if text.lower() == "e" or text.lower() == "exit":
            return "exit"

        print("""
        Choose hash type:

        1. MD5
        2. SHA-1
        3. SHA-256
        4. SHA-512
        """)

        hash_type = input("Enter hash type: ")

        if hash_type == "1":
            hashed = hashlib.md5(text.encode()).hexdigest()

        elif hash_type == "2":
            hashed = hashlib.sha1(text.encode()).hexdigest()

        elif hash_type == "3":
            hashed = hashlib.sha256(text.encode()).hexdigest()

        elif hash_type == "4":
            hashed = hashlib.sha512(text.encode()).hexdigest()

        else:
            print("Invalid option!")
            continue

        print("\nHash:")
        print(hashed)
