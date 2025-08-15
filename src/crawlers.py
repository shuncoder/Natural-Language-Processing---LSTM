"""Data crawling utilities for Vietnamese news websites.
Functions for crawling articles from popular Vietnamese news sites:
- crawl_vnexpress(): Crawl VnExpress
- crawl_zingnews(): Crawl Zing News
- crawl_vietnamnet(): Crawl VietnamNet
- crawl_dantri(): Crawl Dan Tri
- crawl_laodong(): Crawl Lao Dong
- crawl_cafef(): Crawl CafeF
"""

import time
from typing import List, Dict
import requests
from bs4 import BeautifulSoup

def setup_crawler():
    """Setup common crawler settings."""
    return {"headers": {"User-Agent": "Mozilla/5.0"}}

def crawl_vnexpress(category_url: str, label: str, num_pages: int) -> List[Dict]:
    """Crawl articles from VnExpress.
    
    Args:
        category_url: URL of category to crawl (e.g., "https://vnexpress.net/thoi-su")
        label: Category label to assign
        num_pages: Number of pages to crawl
        
    Returns:
        List of dicts with keys: title, summary, label
    """
    articles = []
    headers = setup_crawler()["headers"]

    for page in range(1, num_pages + 1):
        url = f"{category_url}-p{page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("div.list-news-subfolder article"):
            title = item.select_one("h3.title-news a")
            summary = item.select_one("p.description a")

            if title and summary:
                articles.append({
                    "title": title.text.strip(),
                    "summary": summary.text.strip(),
                    "label": label
                })
        time.sleep(1)  # Be nice to servers

    return articles

def crawl_zingnews(category_url: str, label: str, num_pages: int) -> List[Dict]:
    """Crawl articles from Zing News.
    
    Args:
        category_url: URL of category to crawl (must end with 'trang1.html')
        label: Category label to assign
        num_pages: Number of pages to crawl
        
    Returns:
        List of dicts with keys: title, summary, label
    """
    articles = []
    headers = setup_crawler()["headers"]

    for page in range(1, num_pages + 1):
        url = category_url.replace("trang1.html", f"trang{page}.html")
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("article"):
            title = item.select_one("h3.article-title a")
            summary = item.select_one("p.article-summary")

            if title and summary:
                articles.append({
                    "title": title.text.strip(),
                    "summary": summary.text.strip(),
                    "label": label
                })
        time.sleep(1)

    return articles

def crawl_vietnamnet(category_url: str, label: str, num_pages: int) -> List[Dict]:
    """Crawl articles from VietnamNet.
    
    Args:
        category_url: Base URL of category to crawl
        label: Category label to assign
        num_pages: Number of pages to crawl
        
    Returns:
        List of dicts with keys: title, summary, label
    """
    articles = []
    headers = setup_crawler()["headers"]

    for page in range(1, num_pages + 1):
        url = f"{category_url}?p={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("div.horizontalPost"):
            title = item.select_one("h3.horizontalPost__main-title a")
            summary = item.select_one("div.horizontalPost__main-desc p")

            if title and summary:
                articles.append({
                    "title": title.text.strip(),
                    "summary": summary.text.strip(),
                    "label": label
                })
        time.sleep(1)

    return articles

def crawl_dantri(category_url: str, label: str, num_pages: int) -> List[Dict]:
    """Crawl articles from Dan Tri.
    
    Args:
        category_url: URL of category to crawl (must end with .htm)
        label: Category label to assign
        num_pages: Number of pages to crawl
        
    Returns:
        List of dicts with keys: title, summary, label
    """
    articles = []
    headers = setup_crawler()["headers"]

    for page in range(1, num_pages + 1):
        url = category_url.replace(".htm", f"/trang-{page}.htm")
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("article.article-item"):
            title = item.select_one("h3.article-title a")
            summary = item.select_one("div.article-excerpt")

            if title and summary:
                articles.append({
                    "title": title.text.strip(),
                    "summary": summary.text.strip(),
                    "label": label
                })
        time.sleep(1)

    return articles

def crawl_laodong(category_url: str, label: str, num_pages: int) -> List[Dict]:
    """Crawl articles from Lao Dong.
    
    Args:
        category_url: Base URL of category to crawl
        label: Category label to assign
        num_pages: Number of pages to crawl
        
    Returns:
        List of dicts with keys: title, summary, label
    """
    articles = []
    headers = setup_crawler()["headers"]

    for page in range(1, num_pages + 1):
        url = f"{category_url}?p={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("article.v4"):
            title = item.select_one("a.link-title h2")
            summary = item.select_one("div.chapeau")

            if title and summary:
                articles.append({
                    "title": title.text.strip(),
                    "summary": summary.text.strip(),
                    "label": label
                })
        time.sleep(1)

    return articles

def crawl_cafef(category_url: str, label: str, num_pages: int) -> List[Dict]:
    """Crawl articles from CafeF.
    
    Args:
        category_url: URL of category to crawl (must end with trang-1.html)
        label: Category label to assign
        num_pages: Number of pages to crawl
        
    Returns:
        List of dicts with keys: title, summary, label
    """
    articles = []
    headers = setup_crawler()["headers"]

    for page in range(1, num_pages + 1):
        url = category_url.replace("trang-1.html", f"trang-{page}.html")
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("div.tlitem"):
            title = item.select_one("h3 a")
            summary = item.select_one("p.sapo")

            if title and summary:
                articles.append({
                    "title": title.text.strip(),
                    "summary": summary.text.strip(),
                    "label": label
                })
        time.sleep(1)

    return articles
