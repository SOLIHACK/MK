import requests

def find_vulnerabilities(target, shodan_api_key="YOUR_SHODAN_API_KEY"):
    vulnerabilities = []
    try:
        url = f"https://api.shodan.io/shodan/host/{target}?key={shodan_api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            vulnerabilities = data.get("vulns", [])
    except Exception:
        pass
    return vulnerabilities
