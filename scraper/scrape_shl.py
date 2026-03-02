import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.shl.com"
CATALOG_BASE = "https://www.shl.com/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_links_from_page(start):
    url = f"{CATALOG_BASE}?start={start}"
    print(f"Fetching catalog page: {url}")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/products/product-catalog/view/" in href:
            full_url = BASE_URL + href
            links.append(full_url)

    return list(set(links))


def scrape_product(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

   
    try:
        name = soup.find("h1").text.strip()
    except:
        name = ""

    description_tag = soup.find("meta", {"name": "description"})
    description = description_tag["content"] if description_tag else ""


    test_type = ""
    duration = ""
    remote_support = ""
    adaptive_support = ""


    info_blocks = soup.find_all("p")

    for block in info_blocks:
        text = block.get_text(strip=True)

        # Test Type
        if "Test Type" in text:
            span = block.find("span")
            if span:
                test_type = span.get_text(strip=True)

        # Duration
        if "Approximate Completion Time" in text:
            duration = text.replace(
                "Approximate Completion Time in minutes =", ""
            ).strip()

        # Remote Support
        if "Remote Testing" in text:
            span = block.find("span")
            if span:
                remote_support = span.get_text(strip=True)

        # Adaptive Support
        if "Adaptive Support" in text:
            span = block.find("span")
            if span:
                adaptive_support = span.get_text(strip=True)

    return {
        "name": name,
        "url": url,
        "description": description,
        "test_type": test_type,
        "duration": duration,
        "remote_support": remote_support,
        "adaptive_support": adaptive_support
    }


def main():
    all_links = set()

    # Pagination
    for start in range(0, 500, 12):
        links = get_links_from_page(start)

        if not links:
            break

        all_links.update(links)
        time.sleep(1)

    print("Total unique product links found:", len(all_links))

    assessments = []

    for i, link in enumerate(all_links):
        try:
            print(f"Scraping {i+1}/{len(all_links)}")
            data = scrape_product(link)
            assessments.append(data)
            time.sleep(1)
        except Exception as e:
            print("Error scraping:", link)
            continue

    print("Total assessments scraped:", len(assessments))

    with open("data/assessments.json", "w", encoding="utf-8") as f:
        json.dump(assessments, f, indent=4)

    print("Saved to data/assessments.json")


if __name__ == "__main__":
    main()