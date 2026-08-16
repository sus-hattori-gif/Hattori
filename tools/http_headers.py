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

def HTTP_Headers_Analyzer():

    while True:

        print("""
        ==============================
          HTTP Headers Analyzer
        ==============================

        Enter a URL

        B = Back
        E = Exit
        """)

        url = input("Enter URL: ").strip()

        if url.lower() == "b" or url.lower() == "back":
            return "back"

        if url.lower() == "e" or url.lower() == "exit":
            return "exit"

        # Add scheme if user did not enter one
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        try:

            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Hattori/1.0"
                }
            )

            response = urllib.request.urlopen(
                request,
                timeout=7
            )

            print("\n")
            print("=" * 60)
            print("             HTTP HEADERS")
            print("=" * 60)

            print("URL:", response.geturl())
            print("Status Code:", response.status)
            print("Reason:", response.reason)

            print("\n--- Response Headers ---")

            for name, value in response.getheaders():

                print(f"{name}: {value}")

            print("\n--- Security Headers ---")

            security_headers = {
                "strict-transport-security":
                    "Strict-Transport-Security",

                "content-security-policy":
                    "Content-Security-Policy",

                "x-content-type-options":
                    "X-Content-Type-Options",

                "x-frame-options":
                    "X-Frame-Options",

                "referrer-policy":
                    "Referrer-Policy",

                "permissions-policy":
                    "Permissions-Policy"
            }

            received_headers = {
                name.lower(): value
                for name, value in response.getheaders()
            }

            for key, display_name in security_headers.items():

                if key in received_headers:

                    print(
                        f"[+] {display_name}: "
                        f"{received_headers[key]}"
                    )

                else:

                    print(
                        f"[-] {display_name}: Not present"
                    )

            print("=" * 60)

            response.close()

        except urllib.error.HTTPError as e:

            print("\nHTTP Error:", e.code)
            print("Reason:", e.reason)

            print("\n--- Response Headers ---")

            for name, value in e.headers.items():

                print(f"{name}: {value}")

        except urllib.error.URLError as e:

            print("\nCould not connect to the URL.")
            print("Reason:", e.reason)

        except TimeoutError:

            print("\nConnection timed out.")

        except ValueError:

            print("\nInvalid URL.")

        except Exception as e:

            print("\nError:", e)
