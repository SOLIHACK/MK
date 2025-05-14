import socket

def find_subdomains(domain, wordlist_file="subdomains.txt"):
    subdomains = []
    try:
        with open(wordlist_file, "r") as file:
            words = file.read().splitlines()
            for word in words:
                subdomain = f"{word}.{domain}"
                try:
                    socket.gethostbyname(subdomain)
                    subdomains.append(subdomain)
                except socket.gaierror:
                    pass
    except FileNotFoundError:
        print("[red]Wordlist file not found! Please ensure 'subdomains.txt' exists.[/red]")
    if not subdomains:
        print("[yellow]No subdomains were found. Ensure your wordlist is correct.[/yellow]")
    return subdomains
