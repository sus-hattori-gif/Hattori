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

def Banner_Grabber():

    while True:

        print("""
        ==========================
            Banner Grabbing
        ==========================

        B = Back
        E = Exit
        """)

        host = input("Enter host: ")

        if host.lower() == "b" or host.lower() == "back":
            return "back"

        if host.lower() == "e" or host.lower() == "exit":
            return "exit"

        try:
            port = int(input("Enter port: "))

        except ValueError:
            print("\nInvalid port!")
            continue

        if port < 1 or port > 65535:
            print("\nPort must be between 1 and 65535.")
            continue

        sock = None

        try:

            # -------------------------
            # HTTPS
            # -------------------------

            if port == 443:

                raw_socket = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                raw_socket.settimeout(5)

                start = time.time()

                raw_socket.connect((host, port))

                context = ssl.create_default_context()

                sock = context.wrap_socket(
                    raw_socket,
                    server_hostname=host
                )

                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: Hattori/1.0\r\n"
                    f"Connection: close\r\n"
                    f"\r\n"
                )

                sock.sendall(request.encode())

            # -------------------------
            # HTTP
            # -------------------------

            elif port == 80:

                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                sock.settimeout(5)

                start = time.time()

                sock.connect((host, port))

                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: Hattori/1.0\r\n"
                    f"Connection: close\r\n"
                    f"\r\n"
                )

                sock.sendall(request.encode())

            # -------------------------
            # Other TCP services
            # -------------------------

            else:

                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                sock.settimeout(5)

                start = time.time()

                sock.connect((host, port))

            # -------------------------
            # Receive response
            # -------------------------

            response = b""

            while True:

                try:
                    data = sock.recv(4096)

                    if not data:
                        break

                    response += data

                    if len(response) >= 16384:
                        break

                except socket.timeout:
                    break

            end = time.time()

            # -------------------------
            # Display results
            # -------------------------

            print("\n" + "=" * 50)

            print("Host:", host)
            print("Port:", port)
            print("Status: OPEN")

            print(
                f"Response time: "
                f"{(end - start) * 1000:.2f} ms"
            )

            print("=" * 50)

            if response:

                print("\nServer Response:\n")

                print(
                    response.decode(
                        "utf-8",
                        errors="replace"
                    )
                )

            else:

                print("\nNo banner or response received.")

            print("\n" + "=" * 50)

        except socket.timeout:

            print("\nConnection timed out.")

        except ConnectionRefusedError:

            print("\nConnection refused.")

        except socket.gaierror:

            print("\nCould not resolve host.")

        except ssl.SSLError as e:

            print("\nSSL/TLS error:", e)

        except OSError as e:

            print("\nConnection error:", e)

        finally:

            if sock is not None:

                try:
                    sock.close()

                except Exception:
                    pass
