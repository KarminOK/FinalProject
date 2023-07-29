import requests
import pandas as pd


def data(nw_lat, nw_long, se_lat, se_long) :
    # Base url for Chicago Open Data Portal crime API; plus addin of date and location filters
    baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

    datebetw = "?$where=date between '2019-01-01T12:00:00' and '2019-07-16T14:00:00'"

    # syntax for below filter is  'within_box(location_col, nw_lat, nw_long, se_lat, se_long)'
    boxurl = 'within_box(location, %s, %s, %s, %s)' % (nw_lat, nw_long, se_lat, se_long)

    # Create the overall URL to interogate API with our data and location filters
    ourl = baseurl + datebetw + ' AND ' + boxurl

    text = requests.get(ourl).json()

    # create pandas dataframe dictionary container object
    df = pd.DataFrame(
        text, columns=['date', 'block', 'primary_type', 'description', 'location_description'])
    return df


