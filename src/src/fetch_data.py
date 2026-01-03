import requests

def fetch_drug_labels():
    url = "https://api.fda.gov/drug/label.json?limit=5"
    response = requests.get(url)
    data = response.json()
    return data.get("results", [])

if __name__ == "__main__":
    records = fetch_drug_labels()
    print("Number of drug labels fetched:", len(records))
