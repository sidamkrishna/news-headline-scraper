import requests
from bs4 import BeautifulSoup

url = "https://www.ndtv.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    print("📡 Sending request...")
    response = requests.get(url, headers=headers)
    print("🔵 Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2")
    print(f"📰 Found {len(headlines)} headlines")
    for h in headlines[:5]:
     print("📰", h.get_text(strip=True))


    with open("headlines.txt", "w", encoding="utf-8") as file:
        for h in headlines:
            title = h.get_text(strip=True)
            if title:
                file.write(title + "\n")

    print("✅ Headlines saved to headlines.txt")

except requests.exceptions.RequestException as e:
    print("⚠️ Error fetching the page:", e)
