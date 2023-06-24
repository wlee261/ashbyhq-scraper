import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

SITE_URLS = [
    'https://jobs.ashbyhq.com/docker',
    'https://jobs.ashbyhq.com/quora',
    'https://jobs.ashbyhq.com/linear',
    'https://jobs.ashbyhq.com/multiverse',
    'https://jobs.ashbyhq.com/notion',
    'https://jobs.ashbyhq.com/duolingo',
    'https://jobs.ashbyhq.com/retool',
    'https://jobs.ashbyhq.com/reddit',
    'https://jobs.ashbyhq.com/replit',
    'https://jobs.ashbyhq.com/vanmoof',
]

for URL in SITE_URLS:
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Set path to your ChromeDriver executable
    webdriver_service = Service(r"C:\Users\yodal\Downloads\chromedriver_win32")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(
        service=webdriver_service, options=chrome_options)

    # Navigate to the website
    driver.get(URL)

    print('Fetching from: ', URL, '\n\n')

    # Wait for the page to load (adjust the sleep time as needed)
    time.sleep(2)

    # Get the updated HTML content after the page has loaded
    html = driver.page_source

    # Close the browser
    driver.quit()

    # Process the HTML using BeautifulSoup or any other library
    soup = BeautifulSoup(html, 'html.parser')

    departments = soup.find_all(
        'span', class_='ashby-department-heading-level')
    job_listings_by_department = soup.find_all(
        'div', class_='ashby-job-posting-brief-list')

    for department, job_listings_container in zip(departments, job_listings_by_department):
        print('Department: ', department.text, ':')
        job_listings = job_listings_container.find_all(
            'a', class_='_container_j2da7_1')
        for job_listing in job_listings:
            href = job_listing['href']
            print('Href:', href)

            h3_element = job_listing.find('h3')
            if h3_element:
                print('Job title: ', h3_element.text)
        print('\n\n')
