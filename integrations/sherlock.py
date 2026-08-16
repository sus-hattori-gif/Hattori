"""Future Sherlock external-process integration point."""

def Sherlock():
    while True:
        username=input("Enter username (B = back, E = exit): ").strip()
        if username.lower()=="b": return "back"
        if username.lower() in ("e","exit"): return "exit"
        print("Sherlock integration is not configured yet.")
