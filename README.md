# 📚 Books to Scrape – Automated Data Pipeline & Interactive Dashboard

Deployed link: https://books-scraper-project.onrender.com 

Note: Periods of inactivity will result in slower loading for about 1 min

This project automates the entire process of scraping book listings from [Books to Scrape](http://books.toscrape.com/), cleaning the data, and visualizing it through an interactive dashboard powered by Streamlit and Plotly.

From data extraction to insight—all with a single script.

---

## 🚀 Features

- 🕷 **Scrapes real product data**: titles, prices, categories, ratings, availability, descriptions, UPCs, and more.
- 🧼 **Cleans & transforms data**:
  - Converts prices to floats
  - Converts ratings to numbers
  - Fills missing descriptions/categories with placeholders
- 🔄 **Automated Pipeline**: `run_all.py` triggers the Scrapy spider and cleans the data for use in the dashboard.
- 📊 **Interactive Streamlit Dashboard** with:
  - Price distribution by category (area chart)
  - Number of books by category
  - Ratings by category
  - Price of books by availability
  - Category selector for custom filtering

---

## 🧰 Tech Stack

| Tool           | Purpose                                   |
|----------------|-------------------------------------------|
| **Scrapy**     | Web scraping engine                       |
| **Python**     | Core scripting                            |
| **pandas**     | Data cleaning & processing                |
| **Streamlit**  | Interactive dashboard frontend            |
| **Plotly**     | Beautiful, interactive data visualizations|
| **Render**     | Deployment platform                       |

---

## Run the full pipeline
`python run_all.py`

## Launch the dashboard
`streamlit run streamlit_app.py`


