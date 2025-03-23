from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)
keywords = ["best places to travel", "trending destinations", "hidden travel gems"]
pytrends.build_payload(kw_list=keywords, timeframe='now 7-d', geo='US')

trend_data = pytrends.interest_over_time()
print(trend_data)
