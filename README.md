# Python Web Scraping and Django Web Application

## Project Overview

This project demonstrates web scraping using Python, data storage using CSV and SQLite,
and data presentation using a simple Django web application.

Quotes are scraped from https://quotes.toscrape.com with pagination support, stored
persistently, and displayed on a web page.

---

## Features

- Scrapes quotes from 10 pages using pagination
- Extracts:
  - Quote text
  - Author name
  - Tags
  - Author profile URL
- Stores data in:
  - CSV file
  - SQLite database (duplicate-safe)
- Displays scraped data using Django
- Clean and modular project structure

---

## Tech Stack

- Python
- Pandas
- SQLite
- Django

---

## Setup & Run Instructions

### Prerequisites

- Python 3.8 or higher
- pip
- SQLite (included with Python)

Verify installation:

python3 --version
pip --version

---

### 1. Clone or Extract the Project
```
git clone <repository-url>
cd quotes_scraper


### 2. Create and Activate Virtual Environment

python3 -m venv venv

Linux / macOS:
source venv/bin/activate

Windows:
venv\Scripts\activate



### 3. Install Dependencies

pip install -r requirements.txt


## Run Web Scraper

python scraper/scrape_quotes.py

Generated files:
data/quotes.csv
data/quotes.db


## Run Django Web Application

cd webapp
python3 manage.py migrate
python3 manage.py runserver

Open:
http://127.0.0.1:8000/

```

