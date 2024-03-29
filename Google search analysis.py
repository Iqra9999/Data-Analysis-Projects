#Google Trends provides an API that can be used to analyze the daily searches on Google. 
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#I'll analyze Google search trends related to "Machine Learning" queries in this context.
trends.build_payload(kw_list=["Machine Learning"])
data = trends.interest_by_region()
data = data.sort_values(by="Machine Learning", ascending=False)
data = data.head(10)
print(data)

#Visualizing the above data using bar chart.
data.reset_index().plot(x="geoName", 
                        y="Machine Learning", 
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()

