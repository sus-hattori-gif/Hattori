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

def Ping():

    while True:

        host = input("Enter host (B = back, E = exit): ")

        if host.lower() == "b":
            return "back"

        if host.lower() == "e" or host.lower() == "exit":
            return "exit"

        try:
            ip = socket.gethostbyname(host)

            start = time.time()

            connection = socket.create_connection(
                (ip, 80),
                timeout=3
            )

            end = time.time()

            connection.close()

            latency = (end - start) * 1000

            print("\nHost:", host)
            print("IP:", ip)
            print("Status: Reachable")
            print(f"Response time: {latency:.2f} ms")

        except socket.timeout:

            print("\nStatus: Timeout")

        except socket.error:

            print("\nStatus: Unreachable")
