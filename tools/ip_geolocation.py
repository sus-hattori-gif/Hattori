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

def IP_Geolocation():

    while True:

        print("""
        ==========================
          IP Geolocation
        ==========================

        Enter an IP address
        Enter ME to find your public IP

        B = Back
        E = Exit
        """)

        IP = input("Enter IP: ")

        if IP.lower() == "b" or IP.lower() == "back":
            return "back"

        if IP.lower() == "e" or IP.lower() == "exit":
            return "exit"

        try:

            # Find user's public IP
            if IP.lower() == "me":

                response = urllib.request.urlopen(
                    "https://api.ipify.org",
                    timeout=5
                )

                IP = response.read().decode()

                print("\nYour Public IP:", IP)

            # API URL
            URL = (
                "http://ip-api.com/json/"
                + IP
                + "?fields="
                "status,message,country,regionName,"
                "city,zip,lat,lon,timezone,isp,org,as"
            )

            response = urllib.request.urlopen(
                URL,
                timeout=5
            )

            data = json.loads(
                response.read().decode()
            )

            # Check API response
            if data.get("status") != "success":

                print(
                    "\nLookup failed:",
                    data.get("message", "Unknown error")
                )

                continue

            print("\n")
            print("=" * 45)
            print("           IP GEOLOCATION")
            print("=" * 45)

            print("IP:", IP)
            print("Country:", data.get("country"))
            print("Region:", data.get("regionName"))
            print("City:", data.get("city"))
            print("ZIP:", data.get("zip"))
            print("Latitude:", data.get("lat"))
            print("Longitude:", data.get("lon"))
            print("Timezone:", data.get("timezone"))
            print("ISP:", data.get("isp"))
            print("Organization:", data.get("org"))
            print("AS:", data.get("as"))

            print("=" * 45)

        except urllib.error.HTTPError as e:

            print("\nHTTP Error:", e.code)

        except urllib.error.URLError:

            print("\nCould not connect to the geolocation service.")

        except json.JSONDecodeError:

            print("\nInvalid response from the API.")

        except Exception as e:

            print("\nError:", e)
