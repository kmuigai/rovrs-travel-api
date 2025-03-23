# Import required libraries
from pytrends.request import TrendReq
import pandas as pd

# Initialize Google Trends API
pytrends = TrendReq(hl='en-US', tz=360)

# Define a general travel-related keyword to track city popularity
keywords = ["travel"]

# Build payload for Google Trends
pytrends.build_payload(kw_list=keywords, timeframe='now 7-d', geo='US')

# Get interest by U.S. cities
city_trends = pytrends.interest_by_region(resolution="CITY")

# Sort by highest search interest
top_10_cities = city_trends.sort_values(by="travel", ascending=False).head(10)

# Save the top 10 cities to a CSV file
csv_filename = "top_10_us_travel_cities.csv"
top_10_cities.to_csv(csv_filename)

# Print results
print("📍 **Top 10 Most Searched U.S. Travel Cities on Google Trends:**")
print(top_10_cities)

print(f"\n✅ Data saved to {csv_filename}")
