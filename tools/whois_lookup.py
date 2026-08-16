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

def WHOIS_Lookup():

    while True:

        print("""
        ==========================
             WHOIS Lookup
        ==========================

        B = Back
        E = Exit
        """)

        domain = input("Enter domain: ")

        if domain.lower() == "b" or domain.lower() == "back":
            return "back"

        if domain.lower() == "e" or domain.lower() == "exit":
            return "exit"

        try:

            print("\nLooking up WHOIS information...\n")

            information = whois.whois(domain)

            print("=" * 50)

            print("Domain:", information.domain_name)
            print("Registrar:", information.registrar)
            print("Creation Date:", information.creation_date)
            print("Expiration Date:", information.expiration_date)
            print("Updated Date:", information.updated_date)
            print("Status:", information.status)
            print("Name Servers:", information.name_servers)

            print("=" * 50)

        except Exception as e:

            print("\nWHOIS lookup failed.")
            print("Error:", e)
