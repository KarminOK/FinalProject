import matplotlib

from .data import data as d
import matplotlib.pyplot as plt
import pandas as pd
import uuid

matplotlib.use('Agg')  # 设置后端为Agg


def scatter(response, nw_lat, nw_long, se_lat, se_long):
    df = d(nw_lat, nw_long, se_lat, se_long)
    df['date'] = df['date'].apply(lambda s1: s1[5:7])
    s = df[['date']]
    crime_count = pd.DataFrame(s.groupby('date').size().sort_values(ascending=True).rename('counts'))
    average = crime_count.mean(axis=0)
    min = crime_count.min()
    max = crime_count.max()
    median = crime_count.median()
    std = crime_count.std()
    sum = crime_count.sum()
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    ax.set_xlabel("average,min,max,median,std,sum")
    ax.set_ylabel('count')
    ax.set_title('average,min,max,median,std,sum  criminal records')
    ax.scatter(x=['average', 'min', 'max', 'median', 'std', 'sum'], y=[average, min, max, median, std, sum])
    fig.savefig(response)
    # fig.close()


def barh(response, nw_lat, nw_long, se_lat, se_long):
    df = d(nw_lat, nw_long, se_lat, se_long)
    s = df[['location_description']]
    crime_count = pd.DataFrame(s.groupby('location_description').size().sort_values(ascending=True).rename('counts'))
    data = crime_count.iloc[-10:]
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    data.plot(kind='barh', ax=ax)
    fig.subplots_adjust(left=0.33, right=0.89)
    ax.set_title('TOP10 location')
    fig.savefig(response)
    # plt.close()


def grid(response, nw_lat, nw_long, se_lat, se_long):
    df = d(nw_lat, nw_long, se_lat, se_long)
    df['date'] = df['date'].apply(lambda s1: s1[5:7])
    s = df[['date']]
    crime_count = pd.DataFrame(s.groupby('date').size().sort_values(ascending=True).rename('counts'))
    data = crime_count.iloc[:]
    average = data.apply(lambda s1: s1/30)
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    ax.plot(data.index.values, data['counts'], label='Total criminal records', color="r")
    ax.plot(data.index.values, average, label='average criminal records', color="blue")
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left")
    ax.set_title('Total monthly criminal records')
    fig.savefig(response)
    # plt.close()


def pie(response, nw_lat, nw_long, se_lat, se_long):
    df = d(nw_lat, nw_long, se_lat, se_long)
    s = df[['primary_type']]
    crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    data = crime_count.iloc[-10:]
    ax.pie(data['counts'], autopct='%1.1f%%', labels=data.index.values)
    ax.set_title('TOP10 crimes')
    fig.savefig(response)
    # plt.close()
