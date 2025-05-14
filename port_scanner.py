import socket

def scan_ports(target, ports=range(1, 1025)):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((target, port)) == 0:
                    open_ports.append(port)
        except Exception as e:
            print(f"[red]Error scanning port {port} on {target}: {e}[/red]")
    if not open_ports:
        print(f"[yellow]No open ports found on {target}.[/yellow]")
    return open_ports
