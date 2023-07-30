import matplotlib

from .data import data as d
import matplotlib.pyplot as plt
import pandas as pd
import uuid
import json

matplotlib.use('Agg')  # Set backend to Agg


def scatter(response, nw_lat, nw_long, se_lat, se_long):
    # Load data within the specified location
    df = d(nw_lat, nw_long, se_lat, se_long)
    
    # Extract the month from the 'date' column
    df['date'] = df['date'].apply(lambda s1: s1[5:7])
    
    # Group data by month and calculate the number of criminal records for each month
    s = df[['date']]
    crime_count = pd.DataFrame(s.groupby('date').size().sort_values(ascending=True).rename('counts'))
    
    # Calculate statistical outcomes
    average = crime_count.mean(axis=0)
    minimum = crime_count.min()
    maximum = crime_count.max()
    median = crime_count.median()
    std_deviation = crime_count.std()
    total_records = crime_count.sum()
    
    # Create the scatter plot
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    ax.set_xlabel("average, min, max, median, std dev, total")
    ax.set_ylabel('count')
    ax.set_title('Average, Minimum, Maximum, Median, Std Deviation, Total Criminal Records')
    ax.scatter(x=['average', 'min', 'max', 'median', 'std dev', 'total'], y=[average, minimum, maximum, median, std_deviation, total_records])
    fig.savefig(response)



def barh(response, nw_lat, nw_long, se_lat, se_long):
    # Load data within the specified location
    df = d(nw_lat, nw_long, se_lat, se_long)
    
    # Group data by location description and calculate the number of records for each location
    s = df[['location_description']]
    crime_count = pd.DataFrame(s.groupby('location_description').size().sort_values(ascending=True).rename('counts'))
    
    # Select the top 10 locations with the highest number of criminal records
    data = crime_count.iloc[-10:]
    
    # Create the horizontal bar chart
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    data.plot(kind='barh', ax=ax)
    fig.subplots_adjust(left=0.33, right=0.89)
    ax.set_title('Top 10 Locations with the Highest Number of Criminal Records')
    
    # Add statistical information to the plot
    for i, v in enumerate(data['counts']):
        ax.text(v, i, str(v), ha='left', va='center')
    
    fig.savefig(response)


def grid(response, nw_lat, nw_long, se_lat, se_long):
    # Load data within the specified location
    df = d(nw_lat, nw_long, se_lat, se_long)
    
    # Convert 'date' column to datetime type
    df['date'] = pd.to_datetime(df['date'])
    
    # Group data by month and calculate the number of criminal records for each month
    crime_count = df.resample('M', on='date').size().rename('counts')
    data = crime_count.reset_index()
    
    # Calculate average number of criminal records per day
    data['average'] = data['counts'] / 30
    
    # Create the line plot with grid
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    ax.plot(data['date'], data['counts'], label='Total Criminal Records', color="r")
    ax.plot(data['date'], data['average'], label='Average Criminal Records per Day', color="blue")
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left")
    ax.set_title('Total Monthly Criminal Records and Average Criminal Records per Day')
    
    # Set the x-axis tick labels to show only the months (e.g., "Jan", "Feb", etc.)
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b"))
    
    # Serialize the data for comparison
    serialized_data = data.to_json(orient='records')
    with open('data.json', 'w') as file:
        file.write(serialized_data)
    
    # Deserialize the data for comparison
    with open('data.json', 'r') as file:
        deserialized_data = json.load(file)
    
    print("Serialized Data:")
    print(json.dumps(deserialized_data, indent=2))
    
    # Perform data comparison (example: comparing last month's data with this month's data)
    last_month_data = deserialized_data[-2]  # Assuming data is sorted by date
    this_month_data = deserialized_data[-1]
    print("Comparison between Last Month and This Month:")
    print(f"Last Month - Date: {last_month_data['date']}, Counts: {last_month_data['counts']}")
    print(f"This Month - Date: {this_month_data['date']}, Counts: {this_month_data['counts']}")
    
    fig.savefig(response)



def pie(response, nw_lat, nw_long, se_lat, se_long):
    # Load data within the specified location
    df = d(nw_lat, nw_long, se_lat, se_long)
    
    # Group data by primary type of crime and calculate the number of records for each type
    s = df[['primary_type']]
    crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
    
    # Select the top 10 types of crimes with the highest number of records
    data = crime_count.iloc[-10:]
    
    # Create the pie chart
    fig = plt.figure(uuid.uuid1(), figsize=(10, 8))
    ax = fig.subplots()
    ax.pie(data['counts'], autopct='%1.1f%%', labels=data.index.values)
    ax.set_title('Top 10 Types of Crimes with the Highest Number of Records')
    
    # Add statistical information to the plot
    total_records = data['counts'].sum()
    ax.text(0.5, -0.1, f"Total Records: {total_records}", transform=ax.transAxes, ha='center')
    

    
    
    # Perform simple statistics and print the result
    crime_counts = df['primary_type'].value_counts().reset_index()
    crime_counts.columns = ['primary_type', 'counts']
    print(crime_counts)

    fig.savefig(response)

