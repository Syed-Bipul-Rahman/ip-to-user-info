import requests

def get_ip_details(ip_address):
    api_url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_ip_details(details):
    if details:
        print(f"IP Address: {details['ip']}")
        print(f"Hostname: {details.get('hostname', 'N/A')}")
        print(f"City: {details.get('city', 'N/A')}")
        print(f"Region: {details.get('region', 'N/A')}")
        print(f"Country: {details.get('country', 'N/A')}")
        print(f"Location: {details.get('loc', 'N/A')}")
        print(f"Organization: {details.get('org', 'N/A')}")
    else:
        print("Error fetching IP details.")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    ip_details = get_ip_details(ip_address)

    display_ip_details(ip_details)

    input("Press Enter to exit...")
