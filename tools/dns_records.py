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

def DNS_Record_Enumerator():

    while True:

        domain = input(
            "Enter domain (B = back, E = exit): "
        ).strip()

        if domain.lower() == "b":
            return "back"

        if domain.lower() == "e" or domain.lower() == "exit":
            return "exit"

        if not domain:
            print("Domain cannot be empty.")
            continue

        print("\n==============================")
        print("      DNS RECORD ENUMERATOR")
        print("==============================")
        print("Domain:", domain)

        record_types = [
            "A",
            "AAAA",
            "MX",
            "NS",
            "CNAME",
            "TXT"
        ]

        for record_type in record_types:

            print(f"\n{record_type} Records:")

            try:

                answers = dns.resolver.resolve(
                    domain,
                    record_type
                )

                for answer in answers:
                    print(" ", answer)

            except dns.resolver.NoAnswer:

                print("  No records found.")

            except dns.resolver.NXDOMAIN:

                print("  Domain does not exist.")
                break

            except dns.resolver.NoNameservers:

                print("  No nameservers available.")

            except dns.exception.Timeout:

                print("  DNS query timed out.")

            except Exception as error:

                print("  Error:", error)
