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

def DNS_Lookup():

    while True:

        domain = input("Enter domain (B = back, E = exit): ")

        if domain.lower() == "b":
            return "back"

        if domain.lower() == "e" or domain.lower() == "exit":
            return "exit"

        try:

            hostname, aliases, addresses = socket.gethostbyname_ex(domain)

            print("\nHostname:", hostname)

            if aliases:
                print("Aliases:")
                for alias in aliases:
                    print(" -", alias)

            print("IP Addresses:")

            for address in addresses:
                print(" -", address)

        except socket.gaierror:

            print("\nCould not resolve domain.")
