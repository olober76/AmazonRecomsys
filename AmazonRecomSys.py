import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import math
import json
import time
import joblib
import seaborn as sns
import os
from surprise import KNNWithMeans
from surprise import Dataset
from surprise import accuracy
from surprise import Reader

from surprise.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from surprise.model_selection import cross_validate
from sklearn.neighbors import NearestNeighbors
import scipy.sparse
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import warnings; warnings.simplefilter('ignore')

for dirname, _, filenames in os.walk('./Dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


electronics_data=pd.read_csv("./Dataset/ratings_Electronics (1).csv",names=['userId', 'productId','Rating','timestamp'])

#Check for missing values

print('AMAZON RECOMENDATION PRODUCT SYSTEM \n')
print('=====================================================')
print('Number of missing values across columns: \n',electronics_data.isnull().sum())

#Dropping the Timestamp column

electronics_data.drop(['timestamp'], axis=1,inplace=True)

#Getting the new dataframe which contains users who has given 50 or more ratings

new_df=electronics_data.groupby("productId").filter(lambda x:x['Rating'].count() >=50)
new_df.head()
new_df.groupby('productId')['Rating'].mean()
no_of_ratings_per_product = new_df.groupby(by='productId')['Rating'].count().sort_values(ascending=False)
#Average rating of the product 

new_df.groupby('productId')['Rating'].mean()
#Total no of rating for product

new_df.groupby('productId')['Rating'].count().sort_values(ascending=False)
ratings_mean_count = pd.DataFrame(new_df.groupby('productId')['Rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(new_df.groupby('productId')['Rating'].count())
popular_products = pd.DataFrame(new_df.groupby('productId')['Rating'].count())
most_popular = popular_products.sort_values('Rating', ascending=False)




print('============================================ \n')
print('DATA PREPARATION AND MODELLING \n')
#Reading the dataset
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(new_df,reader)

#Splitting the dataset
trainset, testset = train_test_split(data, test_size=0.3,random_state=10)
#Splitting the dataset
trainset, testset = train_test_split(data, test_size=0.3,random_state=10)
algo = KNNWithMeans(k=5, sim_options={'name': 'pearson_baseline', 'user_based': False})
algo.fit(trainset)
# run the trained model against the testset
test_pred = algo.test(testset)

print('============================================ \n')
print('EVALUATION \n')

# get RMSE
print("Item-based Model : Test Set")
accuracy.rmse(test_pred, verbose=True)



# Get MAE
print("Item-based Model : Test Set")
accuracy.mae(test_pred, verbose=True)




# Perform cross-validation
results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)


# Perform cross-validation
results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
