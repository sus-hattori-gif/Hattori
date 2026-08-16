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

def Port_Scanner():

    while True:

        host = input("Enter host (B = back, E = exit): ")

        if host.lower() == "b":
            return "back"

        if host.lower() == "e" or host.lower() == "exit":
            return "exit"

        try:
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))

            if start_port < 1 or end_port > 65535:
                print("Ports must be between 1 and 65535.")
                continue

            if start_port > end_port:
                print("Start port must be smaller than end port.")
                continue

            ip = socket.gethostbyname(host)

            print(f"\nScanning {host} ({ip})...")
            print("-" * 40)

            for port in range(start_port, end_port + 1):

                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                sock.settimeout(0.5)

                result = sock.connect_ex((ip, port))

                if result == 0:

                    try:
                        service = socket.getservbyport(
                            port,
                            "tcp"
                        )

                    except OSError:
                        service = "Unknown"

                    print(
                        f"{port:<6} OPEN     {service}"
                    )

                sock.close()

            print("-" * 40)
            print("Scan finished.")

        except ValueError:

            print("Please enter valid numbers.")

        except socket.gaierror:

            print("Could not resolve host.")

        except Exception as e:

            print("Error:", e)
