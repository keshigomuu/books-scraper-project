import subprocess
import os
import time

print("🕷️ Starting data extraction using Scrapy...")
subprocess.run(["scrapy", "crawl", "books", "-o", "cleaned_books.json"])
print("Scraping complete and data cleaned.\n")

print("Launching Streamlit Dashboard...")
streamlit_script_path = os.path.join(os.getcwd(), "streamlit_app.py")
subprocess.run(["streamlit", "run", streamlit_script_path])
