News Headline Web Scraper (Python)

This project is a simple **Python script** that scrapes **news headlines** from a public website (BBC/NDTV/etc.) using **web scraping**.

The scraped headlines are saved into a `.txt` file called `headlines.txt`.



 What It Does

- Sends a **GET request** to the news website
- Parses the HTML using **BeautifulSoup**
- Finds all `<h3>` or `<h2>` tags (depending on the site)
- Extracts and saves the text inside them to a file



Project Files

 File                           
`task3.py`      Main scraper script             
`headlines.txt` Output file with scraped titles 
`README.md`    Project explanation (this file)  

