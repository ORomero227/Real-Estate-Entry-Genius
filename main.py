# Oscar Romero Barbosa

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = ("https://docs.google.com/forms/d/e/1FAIpQLSdiyMLZHomzx195HlucIaoR5OLgDWEjjg-kdbcFGgEPyFbjNg/viewform?"
            "usp=sf_link")
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

# --------------- Scraping Data with BeautifulSoup -----------------------------

# Get html from the page
response = requests.get(url=ZILLOW_CLONE_URL)
response.raise_for_status()
zillow_clone_html = response.text

# Parse html with BeautifulSoup
soup = BeautifulSoup(zillow_clone_html, "html.parser")

# Getting the listings links
anchor_tags = soup.select(selector=".StyledPropertyCardDataArea-anchor")
listings_links = []
for link in anchor_tags:
    listings_links.append(link.get("href"))

# Getting the prices
spans_tags = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
listings_prices = []
for price in spans_tags:
    listings_prices.append(price.text[0:6])

# Getting the address
address_tags = soup.select(".StyledPropertyCardDataWrapper address")
listings_address = []
for address in address_tags:
    clean_address = (address.text.replace("\\", "")
                     .replace("|", "")
                     .replace("\n", "")
                     .strip())

    listings_address.append(clean_address)

# ------------------- Using Selenium ----------------
options = webdriver.EdgeOptions()
options.add_experimental_option(name="detach", value=True)

driver = webdriver.Edge(options=options)
driver.get(url=FORM_URL)

# Fill the form
for n in range(len(listings_address)):
    address_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]"
                                                  "/div/div[1]/input")
    price_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]"
                                                "/div/div[1]/input")
    link_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/"
                                               "div/div[1]/input")
    submit_btn = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    time.sleep(1)

    address_input.send_keys(listings_address[n])
    price_input.send_keys(listings_prices[n])
    link_input.send_keys(listings_links[n])

    submit_btn.click()
    driver.get(FORM_URL)

driver.quit()
