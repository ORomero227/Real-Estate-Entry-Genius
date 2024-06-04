# Real Estate Entry Genius

This Python project leverages web scraping and web automation techniques to extract real estate listing information and automatically populate a Google Forms with the gathered data.

## Features
- **Web Scraping**: Uses `BeautifulSoup` to scrape data from a Zillow clone website.
- **Web Automation**: Employs `Selenium` to automate data entry into a Google Form.
- **Data Extraction**: Collects links, prices, and addresses of real estate properties.
- **Form Filling**: Automatically fills out form fields with the extracted information.

## How It Works
1. The script retrieves the HTML of the real estate listings page.
2. It extracts the links, prices, and addresses of the listed properties.
3. Using `Selenium`, it opens a Google Form and fills it with the scraped data.
4. Submits the form and repeats the process for all listings.

## Setup
To run this project, you'll need to set up the necessary credentials for the Zillow clone and Google Forms, and install the required Python libraries listed in `requirements.txt`.

## Contributions
Contributions are welcome! If you have suggestions or improvements, please feel free to fork the repo and submit a pull request.

---

 Real Estate Entry Genius is an efficient tool for real estate professionals and enthusiasts, streamlining the process of data collection and entry. It's also an excellent example of practical application of programming skills in web scraping and automation.
