import requests
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def data(nw_lat, nw_long, se_lat, se_long):
    # Base url for Chicago Open Data Portal crime API; plus adding date and location filters
    baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

    datebetw = "?$where=date between '2019-01-01T12:00:00' and '2019-07-16T14:00:00'"

    # syntax for below filter is 'within_box(location_col, nw_lat, nw_long, se_lat, se_long)'
    boxurl = 'within_box(location, %s, %s, %s, %s)' % (nw_lat, nw_long, se_lat, se_long)

    # Create the overall URL to interrogate API with our data and location filters
    ourl = baseurl + datebetw + ' AND ' + boxurl

    # Get data from API and parse it as JSON
    response = requests.get(ourl)
    if response.status_code == 200:
        data_json = response.json()
    else:
        raise Exception("Failed to fetch data from the API.")

    # Print the complete first record in JSON style
    print(json.dumps(data_json[0], indent=2))

    # Create a pandas DataFrame with the fetched data
    df = pd.DataFrame(data_json, columns=['date', 'block', 'primary_type', 'description', 'location_description'])

    # Additional Machine Learning/AI/DL/NLP-related code for text classification
    # Preprocess data for text classification
    df['processed_description'] = df['description'].apply(lambda x: x.lower())

    # Prepare data for training
    X = df['processed_description']
    y = df['primary_type']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Use TfidfVectorizer to convert text data to numerical features
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    # Train a logistic regression model for text classification
    model = LogisticRegression(max_iter=500)
    model.fit(X_train_vectorized, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_vectorized)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    return df
