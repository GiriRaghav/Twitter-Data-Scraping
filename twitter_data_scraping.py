import pandas as pd
import snscrape.modules.twitter as sntwitter
import streamlit as st
from pymongo import MongoClient
import json


def get_tweets(keyword, start_date, end_date, max_tweets):
    # Creating an empty list to store the scraped data
    tweets_list = []

    # Using snscrape to scrape Twitter data based on the keyword or hashtag, date range and maximum number of tweets
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"{keyword} since:{start_date} until:{end_date}").get_items()):
        if i >= max_tweets:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.sourceLabel, tweet.likeCount])

    # Creating a pandas dataframe from the scraped data
    tweets_df = pd.DataFrame(tweets_list, columns=['DATE', 'ID', 'URL', 'TWEET CONTENT', 'USER', 'REPLY COUNT', 'RETWEET COUNT', 'LANGUAGE', 'SOURCE', 'LIKE COUNT'])

    return tweets_df


def store_data_to_mongodb(keyword, tweets_df):
    # Defining MongoDB connection parameters
    mongo_connection = "mongodb://localhost:27017/"
    mongo_db = "twitter_data"
    mongo_collection = "scraped_data"

    # Storing the scraped data into MongoDB
    client = MongoClient(mongo_connection)
    db = client[mongo_db]
    collection = db[mongo_collection]
    collection.insert_one({"Scraped Word": keyword, "Scraped Date": pd.Timestamp.now(), "Scraped Data": tweets_df.to_dict(orient="records")})


def download_data(tweets_df):
    # Providing options to download the scraped data in CSV and JSON formats
    csv = tweets_df.to_csv(index=False)
    json = tweets_df.to_json(orient="records")
    st.download_button("Download CSV :inbox_tray:", data=csv, file_name="twitter_data.csv", mime="text/csv")
    st.download_button("Download JSON :inbox_tray:", data=json, file_name="twitter_data.json", mime="application/json")


def main():
    # Defining Streamlit app title
    st.set_page_config(page_title="Twitter Data Scraping", page_icon=":unlock:")

    # Defining Streamlit app header
    st.title(":blue[TWITTER DATA SCRAPER] :unlock:")

    # Defining Streamlit app container
    with st.container():
        # To enter the keyword or hashtag to search
        keyword = st.text_input("Enter the keyword or hashtag to search: :hash:")

        # To enter the date range
        start_date = st.text_input("Enter the start date (YYYY-MM-DD): :date:")
        end_date = st.text_input("Enter the end date (YYYY-MM-DD): :date:")

        # To enter the maximum number of tweets to scrape
        max_tweets = st.number_input("Enter the maximum number of tweets to scrape: :1234:", min_value=0)

        # Defining Streamlit app main content
        if st.button("Scrape Data :unlock:"):
            tweets_df = get_tweets(keyword, start_date, end_date, max_tweets)
            st.write(tweets_df)
            store_data_to_mongodb(keyword, tweets_df)
            download_data(tweets_df)


if __name__ == "__main__":
    main()