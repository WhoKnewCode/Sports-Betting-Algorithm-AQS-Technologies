import requests
import pandas as pd
import os


# Function to handle API calls and save data to CSV
def fetch_and_save_data(api_name, url, querystring=None, folder="nfl_datasets", filename=None):
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


# Define the folder where NFL datasets will be stored
nfl_folder = "nfl_datasets"

# 1. NFL Player Statistics
fetch_and_save_data(
    api_name="NFL Player Statistics",
    url="https://sports-information.p.rapidapi.com/nfl/player-statistic",
    querystring={"playerId": "3125116"},
    filename="nfl_player_statistics",
    folder=nfl_folder
)

# 2. NFL Team Statistics
fetch_and_save_data(
    api_name="NFL Team Statistics",
    url="https://sports-information.p.rapidapi.com/nfl/team-statistic",
    querystring={"teamId": "14"},
    filename="nfl_team_statistics",
    folder=nfl_folder
)

# 3. NFL Injuries
fetch_and_save_data(
    api_name="NFL Injuries",
    url="https://sports-information.p.rapidapi.com/nfl/injuries",
    filename="nfl_injuries",
    folder=nfl_folder
)

# 4. NFL Team Schedule
fetch_and_save_data(
    api_name="NFL Team Schedule",
    url="https://sports-information.p.rapidapi.com/nfl/schedule-team",
    querystring={"teamId": "14"},
    filename="nfl_team_schedule",
    folder=nfl_folder
)

# 5. NFL Team List
fetch_and_save_data(
    api_name="NFL Team List",
    url="https://sports-information.p.rapidapi.com/nfl/team-list",
    filename="nfl_team_list",
    folder=nfl_folder
)

# 6. NFL Picks
fetch_and_save_data(
    api_name="NFL Picks",
    url="https://sports-information.p.rapidapi.com/nfl/picks/401220403",
    filename="nfl_picks",
    folder=nfl_folder
)

# 7. NFL Play-by-Play
fetch_and_save_data(
    api_name="NFL Play-by-Play",
    url="https://sports-information.p.rapidapi.com/nfl/play-by-play/401220403",
    filename="nfl_play_by_play",
    folder=nfl_folder
)
