import requests
import pandas as pd
import os


# Function to handle API calls and save data to CSV
def fetch_and_save_data(api_name, url, querystring=None, folder="nba_datasets", filename=None):
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


# Define the folder where NBA datasets will be stored
nba_folder = "nba_datasets"

# 1. NBA Play-by-Play
fetch_and_save_data(
    api_name="NBA Play-by-Play",
    url="https://sports-information.p.rapidapi.com/nba/play-by-play/401283399",
    filename="nba_play_by_play",
    folder=nba_folder
)

# 2. NBA Team Schedule
fetch_and_save_data(
    api_name="NBA Team Schedule",
    url="https://sports-information.p.rapidapi.com/nba/schedule-team",
    querystring={"season": "2021", "teamId": "16"},
    filename="nba_team_schedule",
    folder=nba_folder
)

# 3. NBA Injuries
fetch_and_save_data(
    api_name="NBA Injuries",
    url="https://sports-information.p.rapidapi.com/nba/injuries",
    filename="nba_injuries",
    folder=nba_folder
)

# 4. NBA Team Statistics
fetch_and_save_data(
    api_name="NBA Team Statistics",
    url="https://sports-information.p.rapidapi.com/nba/team-statistics",
    querystring={"teamId": "16"},
    filename="nba_team_statistics",
    folder=nba_folder
)

# 5. NBA Player Statistics
fetch_and_save_data(
    api_name="NBA Player Statistics",
    url="https://sports-information.p.rapidapi.com/nba/player-statistics",
    querystring={"playerId": "6478"},
    filename="nba_player_statistics",
    folder=nba_folder
)

# 6. NBA Picks
fetch_and_save_data(
    api_name="NBA Picks",
    url="https://sports-information.p.rapidapi.com/nba/picks/401283399",
    filename="nba_picks",
    folder=nba_folder
)

# 7. NBA Team List
fetch_and_save_data(
    api_name="NBA Team List",
    url="https://sports-information.p.rapidapi.com/nba/team-list",
    filename="nba_team_list",
    folder=nba_folder
)
