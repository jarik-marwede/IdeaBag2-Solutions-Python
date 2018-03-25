#!/usr/bin/env python3
"""A webscraper that scrapes all images and links from a website.

Title:
Page Scraper

Description:
Create an application which connects to a site
and pulls out all links, or images,
and saves them to a list.
For added complexity,
organize the indexed content and don't allow duplicates.
Have it put the results into an easily searchable index file.
"""
import urllib.request
import bs4 as bs


def get_html(url: str):
    """Return html code of the specified website."""
    html = urllib.request.urlopen(url).read()
    return html


def get_image_urls(source: str):
    """Return the urls of all images in the specified html code."""
    soup = bs.BeautifulSoup(source, "lxml")

    images = soup.find_all("img")
    urls = [image.get("src") for image in images]
    return list(set(urls))


def get_links(source: str):
    """Return the urls of all links in the specified html code."""
    soup = bs.BeautifulSoup(source, "lxml")

    links = soup.find_all("a")
    urls = [link.get("href") for link in links
            if link.get("href")
            and link.get("href") != "#"
            and link.get("href") != "/"]
    return list(set(urls))


def save_to_file(links: list, file_path: str):
    """Save the specified links to the specified file."""
    text = ""
    for index, link in enumerate(links):
        text += " ".join((str(index), link, "\n"))

    with open(file_path, "w") as file:
        file.write(text)


def _start():
    """Start the program interactively."""
    url = input("What url do you want to get images/links from? ")
    html = get_html(url)
    images = get_image_urls(html)
    links = get_links(html)
    print(" ".join(("Images: ", *images)))
    print(" ".join(("Links: ", *links)))
    file_path = input("What file do you want to save the links in? ")
    save_to_file(images + links, file_path)


if __name__ == "__main__":
    _start()