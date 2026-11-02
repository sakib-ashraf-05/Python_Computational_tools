from bs4 import BeautifulSoup
import csv
import requests

def scrape_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    books_data = []

    print("Scraping product data from books.toscrape.com...")

    # The site contains 50 pages of books
    for page in range(1, 51):
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("article", class_="product_pod")

        for product in products:
            # Extract book title
            title = product.find("h3").find("a")["title"]

            # Extract price
            price = product.find("p", class_="price_color").get_text(strip=True)

            # Extract stock availability
            availability = product.find("p", class_="instock availability").get_text(strip=True)

            # Extract star rating
            star_classes = product.find("p", class_="star-rating")["class"]
            rating = [c for c in star_classes if c != "star-rating"][0]

            books_data.append({
                "Title": title,
                "Price": price,
                "Availability": availability,
                "Rating": rating
            })

    # Save data to a CSV file
    csv_filename = "books_catalog.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Title", "Price", "Availability", "Rating"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(books_data)

    print(f"Successfully scraped {len(books_data)} books and saved them to {csv_filename}")

if __name__ == "__main__":
    scrape_books()