from subdomain_scanner import find_subdomains
from port_scanner import scan_ports
from vulnerability_scanner import find_vulnerabilities
from rich.console import Console
from rich.prompt import Prompt
from datetime import datetime

console = Console()

def main():
    console.print("[bold magenta]=== Ultimate Network Scanner ===[/bold magenta]")
    domain = Prompt.ask("[cyan]Enter the domain to scan (e.g., example.com)[/cyan]")
    start_time = datetime.now()

    # Étape 1 : Recherche des sous-domaines
    console.print("\n[bold yellow]Step 1: Discovering Subdomains[/bold yellow]")
    subdomains = find_subdomains(domain)

    # Étape 2 : Scan des ports sur chaque sous-domaine
    console.print("\n[bold yellow]Step 2: Scanning Ports[/bold yellow]")
    scan_results = {}
    for subdomain in subdomains:
        ports = scan_ports(subdomain)
        scan_results[subdomain] = ports

    # Étape 3 : Recherche de vulnérabilités
    console.print("\n[bold yellow]Step 3: Finding Vulnerabilities[/bold yellow]")
    for subdomain in subdomains:
        vulnerabilities = find_vulnerabilities(subdomain)
        scan_results[subdomain]["vulnerabilities"] = vulnerabilities

    # Résumé et sauvegarde des résultats
    console.print("\n[bold green]Scan Completed![/bold green]")
    end_time = datetime.now()
    console.print(f"[cyan]Total time taken: {end_time - start_time}[/cyan]")

    with open("scan_results.txt", "w") as file:
        file.write("=== Scan Results ===\n")
        for subdomain, data in scan_results.items():
            file.write(f"\nSubdomain: {subdomain}\n")
            file.write(f"Open Ports: {', '.join(map(str, data['ports']))}\n")
            file.write(f"Vulnerabilities: {', '.join(data['vulnerabilities'])}\n")

if __name__ == "__main__":
    main()
