import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import random
from aiohttp_retry import RetryClient, ExponentialRetry


async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()


async def scrape_book_page(session, url):
    html = await fetch_page(session, url)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1", {"id": "bookTitle"}).text.strip()
    author = soup.find("a", {"class": "authorName"}).text.strip()
    rating = soup.find("span", {"itemprop": "ratingValue"}).text.strip()
    description = soup.find("div", {"id": "description"}).text.strip()
    isbn = soup.find("span", {"itemprop": "isbn"}).text.strip()

    return {
        "title": title,
        "author": author,
        "rating": rating,
        "description": description,
        "isbn": isbn,
    }


async def scrape_goodreads_popular_books(pages=5):
    base_url = "https://www.goodreads.com/book/popular_by_date/"
    books = []

    retry_options = ExponentialRetry(attempts=3)
    async with RetryClient(retry_options=retry_options) as session:
        for page in range(1, pages + 1):
            url = f"{base_url}{page}"
            html = await fetch_page(session, url)
            soup = BeautifulSoup(html, "html.parser")

            book_items = soup.find_all("tr", {"itemtype": "http://schema.org/Book"})

            book_urls = [
                item.find("a", {"class": "bookTitle"})["href"] for item in book_items
            ]
            tasks = [
                asyncio.create_task(
                    scrape_book_page(session, f"https://www.goodreads.com{url}")
                )
                for url in book_urls
            ]

            page_books = await asyncio.gather(*tasks)
            books.extend(page_books)

            print(f"Scraped page {page}")
            await asyncio.sleep(
                random.uniform(1, 3)
            )  # Be polite, add a delay between pages

    return pd.DataFrame(books)


# Run the scraper
df = asyncio.run(scrape_goodreads_popular_books())
print(df.head())

# Save to CSV
df.to_csv("goodreads_popular_books_detailed.csv", index=False)
