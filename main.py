import os
import requests
from datetime import datetime

# Load sensitive data from environment variables
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
BEARER_AUTH = os.getenv("BEARER_AUTH")

# API endpoints for Nutritionix and Sheety
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/7fe796b00789ab35642be56f51df98a0/workoutTracking/workouts"

# Input query from the user about their exercise and physical details
query = input("What exercise did you do today?\n ")


# Headers for the Nutritionix API request, including authentication details
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

# Parameters for the Nutritionix API request, including user's physical details and the exercise query
params = {
    "query": query,
    "gender": "male",
    "weight_kg": 46.6,
    "height_cm": 177.8,
    "age": 30
}

# Headers for the Sheety API request, including the Bearer token for authentication
bearer_headers = {
    "Authorization": "Bearer " + BEARER_AUTH
}

# POST request to Nutritionix API to analyze the exercise data
response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
response.raise_for_status()

# Parsing the response from Nutritionix to get the exercise data
results = response.json()
print(results) # Printing the results for verification


# <-------------------------- Posting to Sheety -------------------------->

# Getting today's date and time
todays_date = datetime.now().strftime("%d/%m/%Y")
todays_time = datetime.now().strftime("%X")

# Loop through each exercise in the results (if multiple)
for exercise in results["exercises"]:
    # Structure the data to be added to the Google Sheet via Sheety
    add_to_sheet = {
        "workout": {
            "date": todays_date,                  # Today's date
            "time": todays_time,                  # Current time
            "exercise": exercise["name"].title(), # Exercise name
            "duration": exercise['duration_min'], # Duration in minutes
            "calories": exercise["nf_calories"]   # Calories burned
        }
    }
    # POST request to Sheety to add the exercise data to the Google Sheet
    google_response = requests.post(url=sheety_endpoint, json=add_to_sheet, headers=bearer_headers)
    print(google_response.text) # Printing the response from Sheety for verification


