import pandas as pd
import numpy as np
import plotly
import plotly.express as px

from movie_rec.recsys import svd,create_utility_matrix

import sematic

@sematic.func
def load_data() -> pd.DataFrame:
    """
    Load CSV file into a DataFrame.
    """
    column_names = ['user_id', 'item_id', 'rating', 'timestamp']
    data= pd.read_csv('movie_rec/ml-100k/u.data', sep='\t', names=column_names)  
    return data

@sematic.func
def ratings_hist_fun(data: pd.DataFrame) -> plotly.graph_objs.Figure:
    ratings= pd.DataFrame(data.groupby('item_id')['rating'].mean())
    fig = px.histogram(ratings['rating'], x="rating")
    return fig

@sematic.func
def train_split(data: pd.DataFrame) -> pd.DataFrame:
    data['user_id'] = data['user_id'].astype('str')
    data['item_id'] = data['item_id'].astype('str')
    users = data['user_id'].unique() #list of all users
    movies = data['item_id'].unique() #list of all movies
    test = pd.DataFrame(columns=data.columns)
    train = pd.DataFrame(columns=data.columns)
    test_ratio = 0.2 #fraction of data to be used as test set.
    for u in users:
        temp = data[data['user_id'] == u]
        n = len(temp)
        test_size = int(test_ratio*n)
        temp = temp.sort_values('timestamp').reset_index()
        temp.drop('index', axis=1, inplace=True)
        dummy_train = temp.iloc[:n-1-test_size]
        train = pd.concat([train, dummy_train])
    return train
    #print("Number of users", len(users))
    #print("Number of movies", len(movies))
    #print(data.head())

@sematic.func
def test_split(data: pd.DataFrame) -> pd.DataFrame:
    data['user_id'] = data['user_id'].astype('str')
    data['item_id'] = data['item_id'].astype('str')
    users = data['user_id'].unique() #list of all users
    movies = data['item_id'].unique() #list of all movies
    test = pd.DataFrame(columns=data.columns)
    train = pd.DataFrame(columns=data.columns)
    test_ratio = 0.2 #fraction of data to be used as test set.
    for u in users:
        temp = data[data['user_id'] == u]
        n = len(temp)
        test_size = int(test_ratio*n)
        temp = temp.sort_values('timestamp').reset_index()
        temp.drop('index', axis=1, inplace=True)
        dummy_test = temp.iloc[n-1-test_size:]
        test = pd.concat([test, dummy_test])
    return test
    #print("Number of users", len(users))
    #print("Number of movies", len(movies))
    #print(data.head())


def rmse(true, pred):
    # this will be used towards the end
    x = true - pred
    return sum([xi*xi for xi in x])/len(x)

@sematic.func
def train_rmse(train: pd.DataFrame, test: pd.DataFrame, f : int) -> float:
# to test the performance over a different number of features
    utilMat, users_index, items_index = create_utility_matrix(train)
    svdout = svd(utilMat, k=f)
    pred = [] #to store the predicted ratings
    for _,row in test.iterrows():
        user = row['user_id']
        item = row['item_id']
        u_index = users_index[user]
        if item in items_index:
            i_index = items_index[item]
            pred_rating = svdout[u_index, i_index]
        else:
            pred_rating = np.mean(svdout[u_index, :])
        pred.append(pred_rating)
    return rmse(test['rating'], pred)


