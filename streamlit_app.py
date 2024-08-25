import streamlit as st
import pandas as pd
import math
from dateutil.parser import parse
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/tracker2.csv'
    df = pd.read_csv(DATA_FILENAME)
    df["Maand"] = df["Date"].apply(lambda x: parse(x))
    
    return df
# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''
tracker_df = get_gdp_data()
import datetime
print(tracker_df.columns())

min_value = tracker_df['Maand'].min()
max_value = tracker_df['Maand'].max()

from_year, to_year = st.slider(
    'Which months are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

''
''

# Filter the data
filtered_tracker_df = tracker_df[
     (tracker_df['Maand'] <= to_year)
    & (from_year <= tracker_df['Maand'])
]

st.header('Channelization BSR over time', divider='gray')

''

st.line_chart(
    filtered_tracker_df,
    x='Maand',
    y='BSR_hoog',
)

''
''


first_year = tracker_df[tracker_df['Maand'] == from_year]
last_year = tracker_df[tracker_df['Maand'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''
