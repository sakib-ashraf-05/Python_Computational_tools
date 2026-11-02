from bs4 import BeautifulSoup
import requests

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    
    # Add headers to mimic a legitimate browser visit
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Hacker News: {e}")
        return

    # Parse the page HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Hacker News stores headlines in anchor tags within elements matching the '.titleline' class
    headlines = soup.select(".titleline > a")

    print(f"Successfully scraped {len(headlines)} headlines from Hacker News:\n")
    print("-" * 70)

    for i, item in enumerate(headlines, start=1):
        title = item.get_text(strip=True)
        link = item.get("href")
        
        print(f"{i}. {title}")
        print(f"   Link: {link}\n")

if __name__ == "__main__":
    scrape_hackernews()