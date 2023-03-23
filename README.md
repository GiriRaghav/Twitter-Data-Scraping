# TWITTER DATA SCRAPING

This is a Python program that scrapes Twitter data based on a keyword or hashtag, date range and maximum number of tweets. 

The scraped data is then stored in a MongoDB database and displayed on a web app created using Streamlit. 

The scraped data can be downloaded in CSV or JSON format. 

The purpose of this code is to demonstrate how to scrape and store Twitter data using Python and MongoDB and display it on a web app using Streamlit.

## WORK FLOW

1.User enters a keyword or hashtag to search, start and end dates and maximum number of tweets to scrape.

2.User clicks "Scrape Data" button.

3.Program uses snscrape to scrape Twitter data based on the user's input.

4.Program stores the scraped data in MongoDB.

5.Program displays the scraped data in a pandas dataframe.

6.User can download the scraped data in CSV or JSON format.

## INSTALLATION

Install the necessary packages by running the following command.

Install pandas
```bash
  pip install pandas
```
Install snscrape
```bash
  pip install snscrape
```
Install streamlit
```bash
  pip install streamlit
```
Install pymongo
```bash
  pip install pymongo
```
    
## EXECUTION


1. Open a terminal or command prompt and navigate to the project directory.
   ```bash
    cd twitter_data_scraper
    ```
2. Run the program.
   ```bash
    streamlit run twitter_data_scraper.py
   ```
3. Enter the keyword or hashtag to search, start & end dates and maximum number of tweets to scrape.

4. Click "Scrape Data" button.

5. Wait for the program to finish scraping the data and store the data in MongoDB.

6. The scraped data will be displayed in a pandas dataframe.

7. User can download the scraped data in CSV or JSON format by clicking the corresponding download button.
