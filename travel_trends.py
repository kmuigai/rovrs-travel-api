# Import required libraries
from pytrends.request import TrendReq
import pandas as pd

# Initialize Google Trends API
pytrends = TrendReq(hl='en-US', tz=360)

# Define trending travel-related searches
keywords = ["best places to travel", "trending destinations", "hidden travel gems"]

# Fetch Google Trends data for the past 7 days
pytrends.build_payload(kw_list=keywords, timeframe='now 7-d', geo='US')

# Get interest over time
trend_data = pytrends.interest_over_time()

# Remove 'isPartial' column if it exists
if 'isPartial' in trend_data.columns:
    trend_data = trend_data.drop(columns=['isPartial'])

# Save the results to a CSV file
csv_filename = "travel_trends_data.csv"
trend_data.to_csv(csv_filename)

# Print confirmation message
print(f"Trending travel data saved successfully to {csv_filename}!")
