import matplotlib

from .data import data as d
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use('Agg')  # 设置后端为Agg


def scatter(response, nw_lat, nw_long, se_lat, se_long):
    df = d(nw_lat, nw_long, se_lat, se_long)
    df['date'] = df['date'].apply(lambda s1: s1[5:7])
    s = df[['date']] #  get a series from data frame
    crime_count = pd.DataFrame(s.groupby('date').size().sort_values(ascending=True).rename('counts'))
    average = crime_count.mean(axis=0)
    min = crime_count.min()
    max = crime_count.max()
    median = crime_count.median()
    std = crime_count.std()
    sum = crime_count.sum()
    plt.figure(figsize=(10, 8), dpi=80)
    plt.xlabel("average,min,max,median,std,sum")
    plt.ylabel('count')
    plt.title('average,min,max,median.std.sum  criminal records')
    plt.scatter(x=['average','min','max','median','std','sum'], y=[average,min,max,median,std,sum])
    #plt.show()
    plt.savefig(response)


def barh(response, nw_lat,nw_long,se_lat,se_long) :
    df=d(nw_lat,nw_long,se_lat,se_long)

    s = df[['location_description']] #  get a series from data frame
    #print(s)
    crime_count = pd.DataFrame(s.groupby('location_description').size().sort_values(ascending=True).rename('counts'))
    data=crime_count.iloc[-10:] # retrieving select rows by loc method
    #print(data[::-1])
    plt.figure(figsize=(10,8),dpi=80)
    data.plot(kind='barh')
    plt.subplots_adjust(left=0.33, right=0.89)
    # Show graphic
    #plt.show()
    plt.title('TOP10 location_description')
    plt.savefig(response)


def grid(response, nw_lat,nw_long,se_lat,se_long) :
    df=d(nw_lat,nw_long,se_lat,se_long)
    df['date']=df['date'].apply(lambda s:s[5:7])
    s = df[['date']] #  get a series from data frame
    crime_count = pd.DataFrame(s.groupby('date').size().sort_values(ascending=True).rename('counts'))
    data=crime_count.iloc[:] # retrieving select rows by loc method
    average=data.apply(lambda s:s/30)
    plt.figure(figsize=(10,8),dpi=80)
    plt.plot(data.index.values, data['counts'], label='Total criminal records',color="r")
    plt.plot(data.index.values, average, label='average criminal records',color="blue")
    plt.grid(alpha=0.2)
    plt.legend(loc="upper left")
    plt.title('Total monthly criminal records')
    #plt.show()
    plt.savefig(response)


def pie(response, nw_lat, nw_long, se_lat, se_long) :
    df=d(nw_lat, nw_long, se_lat, se_long)
    s = df[['primary_type']] #  get a series from data frame
    crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
    #Get TOP10 crimes
    plt.figure(figsize=(10, 8), dpi=80)
    data=crime_count.iloc[-10:] # retrieving select rows by loc method
    plt.pie(data['counts'], autopct='%1.1f%%', labels=data.index.values)
    plt.title('TOP10 crimes')
    #plt.show()
    plt.savefig(response)

