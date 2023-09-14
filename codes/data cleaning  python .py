import numpy as np
import pandas as pd 
prices = pd.read_csv('data/airbnb_price.csv')
reviews = pd.read_csv('data/airbnb_last_review.tsv',delimiter='\t')
room_types = pd.read_excel ('data/airbnb_room_type.xlsx')
prices['price'] = prices['price'].str.strip('dollars')
prices['price'] = prices['price'].astype('int')

prices.drop(prices[prices['price'] == 0].index,inplace = True)
prices.drop(prices[prices['price'] > 2000].index,inplace = True)
avg_price = prices['price'].mean()
average_price_per_month = prices['price'].mean() * (365/12) 
difference = average_price_per_month - 3100  
room_types['room_type'] = room_types['room_type'].str.lower()

reviews['last_review'] = pd.to_datetime(reviews['last_review']).dt.date
first_reviewed = reviews['last_review'].min()
last_reviewed = reviews['last_review'].max()
room_frequencies = room_types['room_type'].value_counts()
merged_rooms = pd.merge(prices,room_types,how='outer', on='listing_id').merge(reviews,how='outer', on = 'listing_id')
merged_rooms.duplicated(subset = 'listing_id',keep = False)

merged_rooms3 = merged_rooms.dropna()

merged_rooms3["borough"] = merged_rooms3["nbhood_full"].str.partition(",")[0]
boroughs = merged_rooms3.groupby("borough")["price"].agg(["sum", "mean", "median", "count"])
boroughs = boroughs.round(2).sort_values("mean", ascending=False)
binss = [0,69,175,350 ,np.inf]
labell = ['Budget','Average','Expensive','Extravagant']
merged_rooms3 ['price_range'] = pd.cut(merged_rooms3 ['price'], labels= labell, bins = binss )
prices_by_borough = merged_rooms3.groupby(["borough", "price_range"])["price_range"].count()

solution = {'avg_price': avg_price,
           'average_price_per_month': average_price_per_month,
           'difference': difference,
           'room_frequencies': room_frequencies,
           'first_reviewed': first_reviewed,
           'last_reviewed': last_reviewed,
            'prices_by_borough': prices_by_borough
           }
print (solution)