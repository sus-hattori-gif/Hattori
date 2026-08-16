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

OUTPUT_DIR = "outputs"

def _safe_filename(name):
    return "".join(c if c.isalnum() or c in "_-" else "_" for c in name)


def Save_Output(tool_name, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(OUTPUT_DIR, f"{_safe_filename(tool_name)}_{timestamp}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\nOutput saved successfully: {path}")


def _output_files():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    return sorted((f for f in os.listdir(OUTPUT_DIR) if os.path.isfile(os.path.join(OUTPUT_DIR, f))), reverse=True)


def View_Outputs():
    files = _output_files()
    if not files:
        print("\nNo saved outputs.")
        return
    print("\n==============================\n       SAVED OUTPUTS\n==============================")
    for i, name in enumerate(files, 1): print(f"{i}. {name}")
    choice = input("\nEnter number to view (B = back): ")
    if choice.lower() == "b": return
    try:
        i = int(choice) - 1
        if i < 0 or i >= len(files): raise ValueError
        with open(os.path.join(OUTPUT_DIR, files[i]), "r", encoding="utf-8") as f: content = f.read()
        print("\n" + "=" * 60 + "\n" + content + "\n" + "=" * 60)
    except (ValueError, OSError): print("Invalid option or file could not be opened.")


def Search_Outputs():
    files = _output_files()
    if not files: print("\nNo saved outputs."); return
    keyword = input("\nEnter search text (B = back): ")
    if keyword.lower() == "b": return
    found = False
    for name in files:
        try:
            with open(os.path.join(OUTPUT_DIR, name), "r", encoding="utf-8") as f: content = f.read()
            if keyword.lower() in name.lower() or keyword.lower() in content.lower(): print(f"[+] {name}"); found = True
        except OSError: pass
    if not found: print("No matching outputs found.")


def Delete_Output():
    files = _output_files()
    if not files: print("\nNo saved outputs."); return
    for i, name in enumerate(files, 1): print(f"{i}. {name}")
    choice = input("\nEnter number to delete (B = back): ")
    if choice.lower() == "b": return
    try:
        i = int(choice) - 1
        if i < 0 or i >= len(files): raise ValueError
        if input(f'Delete "{files[i]}"? (Y/N): ').lower() == "y":
            os.remove(os.path.join(OUTPUT_DIR, files[i])); print("Output deleted.")
    except (ValueError, OSError): print("Invalid option or file could not be deleted.")


def Rename_Output():
    files = _output_files()
    if not files: print("\nNo saved outputs."); return
    for i, name in enumerate(files, 1): print(f"{i}. {name}")
    choice = input("\nEnter number to rename (B = back): ")
    if choice.lower() == "b": return
    try:
        i = int(choice) - 1
        if i < 0 or i >= len(files): raise ValueError
        new_name = input("Enter new filename: ").strip()
        if not new_name: return
        if not new_name.lower().endswith(".txt"): new_name += ".txt"
        new_path = os.path.join(OUTPUT_DIR, new_name)
        if os.path.exists(new_path): print("A file with that name already exists."); return
        os.rename(os.path.join(OUTPUT_DIR, files[i]), new_path); print("Output renamed successfully.")
    except (ValueError, OSError): print("Invalid option or file could not be renamed.")


def Export_Output():
    files = _output_files()
    if not files: print("\nNo saved outputs."); return
    for i, name in enumerate(files, 1): print(f"{i}. {name}")
    choice = input("\nEnter number to export (B = back): ")
    if choice.lower() == "b": return
    try:
        i = int(choice) - 1
        if i < 0 or i >= len(files): raise ValueError
        destination = input("Enter destination path: ").strip()
        if not destination: return
        if os.path.isdir(destination): destination = os.path.join(destination, files[i])
        parent = os.path.dirname(destination)
        if parent: os.makedirs(parent, exist_ok=True)
        with open(os.path.join(OUTPUT_DIR, files[i]), "r", encoding="utf-8") as src: content = src.read()
        with open(destination, "w", encoding="utf-8") as dst: dst.write(content)
        print(f"Output exported successfully: {destination}")
    except (ValueError, OSError): print("Could not export output.")


def Output_Manager_Menu():
    while True:
        print("""
==============================
        OUTPUT MANAGER
==============================

1. View saved outputs
2. Search outputs
3. Delete output
4. Rename output
5. Export output

B. Back
E. Exit
""")
        choice = input("Enter your option: ")
        if choice == "1": View_Outputs()
        elif choice == "2": Search_Outputs()
        elif choice == "3": Delete_Output()
        elif choice == "4": Rename_Output()
        elif choice == "5": Export_Output()
        elif choice.lower() == "b": return "back"
        elif choice.lower() in ("e", "exit"): return "exit"
        else: print("Invalid option!")


class _Tee(io.StringIO):
    def __init__(self, original): super().__init__(); self.original = original
    def write(self, text): self.original.write(text); self.original.flush(); return super().write(text)
    def flush(self): self.original.flush(); super().flush()


def Run_Tool(tool_name, tool_function):
    buffer = _Tee(sys.stdout)
    try:
        with redirect_stdout(buffer): result = tool_function()
    finally:
        output = buffer.getvalue()
    if output.strip():
        print("\n==============================\n          SAVE OUTPUT\n==============================")
        if input("Save this tool output? (Y/N): ").lower() == "y": Save_Output(tool_name, output)
    return result
