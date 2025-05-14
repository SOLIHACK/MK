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
        print("[red]Wordlist file not found![/red]")
    return subdomains
