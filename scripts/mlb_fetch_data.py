import requests
import pandas as pd
import os


# Function to handle API calls and save data to CSV
def fetch_and_save_data(api_name, url, querystring=None, folder="mlb_datasets", filename=None):
    headers = {
        # "x-rapidapi-key": "replace api key here",
        # "x-rapidapi-host": "sports-information.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Convert the data to a Pandas DataFrame
        df = pd.json_normalize(data)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Save the data to a CSV file
        filepath = os.path.join(folder, f"{filename}.csv")
        df.to_csv(filepath, index=False)
        print(f"{api_name} data saved to {filepath}\n")
    else:
        print(f"Error fetching {api_name}: {response.status_code}")
        print(response.text)


# Define the folder where MLB datasets will be stored
mlb_folder = "mlb_datasets"

# 1. MLB Picks
fetch_and_save_data(
    api_name="MLB Picks",
    url="https://sports-information.p.rapidapi.com/mlb/picks/401472105",
    filename="mlb_picks",
    folder=mlb_folder
)

# 2. MLB Player Statistics
fetch_and_save_data(
    api_name="MLB Player Statistics",
    url="https://sports-information.p.rapidapi.com/mlb/player-statistic",
    querystring={"playerId": "42403"},
    filename="mlb_player_statistics",
    folder=mlb_folder
)

# 3. MLB Team List
fetch_and_save_data(
    api_name="MLB Team List",
    url="https://sports-information.p.rapidapi.com/mlb/team-list",
    filename="mlb_team_list",
    folder=mlb_folder
)

# 4. MLB Schedule
fetch_and_save_data(
    api_name="MLB Schedule",
    url="https://sports-information.p.rapidapi.com/mlb/schedule",
    querystring={"year": "2020", "month": "10", "day": "12"},
    filename="mlb_schedule",
    folder=mlb_folder
)

# 5. MLB Play-by-Play
fetch_and_save_data(
    api_name="MLB Play-by-Play",
    url="https://sports-information.p.rapidapi.com/mlb/play-by-play/401472105",
    filename="mlb_play_by_play",
    folder=mlb_folder
)

# 6. MLB Summary
fetch_and_save_data(
    api_name="MLB Summary",
    url="https://sports-information.p.rapidapi.com/mlb/summary/401472105",
    filename="mlb_summary",
    folder=mlb_folder
)

# 7. MLB Team Roster
fetch_and_save_data(
    api_name="MLB Team Roster",
    url="https://sports-information.p.rapidapi.com/mlb/team-roster",
    querystring={"teamId": "16", "season": "2023"},
    filename="mlb_team_roster",
    folder=mlb_folder
)
