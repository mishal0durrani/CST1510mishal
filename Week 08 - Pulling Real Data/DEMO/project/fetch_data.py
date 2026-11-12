"""
fetch_data.py - Week 8: get data from an API and save it as DATA/raw.csv.

Run it:  python fetch_data.py
"""

from pathlib import Path

import pandas as pd
import requests

# ---- Settings: the only part you change for your own data ------------------

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
PARAMS = {"format": "geojson", "minmagnitude": 2.5, "limit": 500, "orderby": "time"}
RECORDS_KEY = "features"          # the key that holds the list of records (None if the reply is already a list)

RENAME = {                        # ugly column name -> short column name
    "properties_mag": "mag",
    "properties_place": "place",
    "properties_time": "time",
    "properties_magType": "mag_type",
    "properties_sig": "significance",
    "properties_tsunami": "tsunami",
}
KEEP = ["time", "place", "mag", "mag_type", "depth_km", "significance", "tsunami"]   # the columns you want
MUST_HAVE = ["mag"]               # drop any row that is empty in these columns

RAW_FILE = Path(__file__).parent / "DATA" / "raw.csv"

# ---- The functions ------------------------------------------------------------


def get_data(url, params):
    """Ask the API for data. Returns the JSON reply, or None if something went wrong."""
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()          # turns 404, 500 ... into an error
        return response.json()
    except requests.RequestException as error:
        print("Could not get the data:", error)
        return None


def make_table(data, records_key):
    """Turn the JSON reply into a pandas table."""
    records = data[records_key] if records_key else data
    return pd.json_normalize(records, sep="_")      # nested {"a": {"b": 1}} becomes column a_b


def tidy_data(df):
    """Rename, keep and clean the columns."""
    df = df.rename(columns=RENAME)

    # Earthquakes only: the coordinates arrive as a list [longitude, latitude, depth]
    df["depth_km"] = df["geometry_coordinates"].apply(lambda coords: coords[2])
    df["time"] = pd.to_datetime(df["time"], unit="ms").dt.strftime("%Y-%m-%d %H:%M:%S")

    df = df[KEEP]
    df = df.dropna(subset=MUST_HAVE)
    return df


def save_data(df, path):
    """Save the table as a CSV file."""
    path.parent.mkdir(exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved {len(df)} rows to {path}")


if __name__ == "__main__":
    data = get_data(URL, PARAMS)
    if data is not None:
        table = make_table(data, RECORDS_KEY)
        table = tidy_data(table)
        print(table.head())
        save_data(table, RAW_FILE)
