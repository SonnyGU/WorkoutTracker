# "Exercise Tracker"
<br />
</br>

## Overview

This project is an exercise tracker that uses the Nutritionix API to analyze physical activities described in natural language and logs the exercise data to a Google Sheet via the Sheety API. 
It's an excellent tool for anyone looking to automate the tracking of their daily exercise routines
<br />


## Features

- **Exercise Data Analysis**: Utilizes the Nutritionix API to interpret natural language inputs about exercises.
- **Automated Data Logging**: Automatically logs exercise details such as type, duration, and calories burned to a Google Sheet.
- **User Input**: Allows users to input their exercise activities in a conversational format.

## Technologies Used

- Python 
- Nutritionix API
- Sheety API
- Google Sheets

## Setup

To run this project, you must set up a few API keys and install the necessary Python packages.

### Prerequisites

- Python 3
- A Nutritionix API account and an API key
- A Sheety API account and an API key
- A Google Sheets document setup through Sheety

### Installation

1. **Clone the repository:** git clone https://github.com/SonnyGU/WorkoutTracker.git
2. **Navigate to the project directory:** cd exercise-tracker
3. **Install the required packages:** pip install requests

### Environment Variables
Set the following environment variables:

- **NUTRITIONIX_APP_ID:** Your Nutritionix app ID
- **NUTRITIONIX_APP_KEY:** Your Nutritionix app key
- **BEARER_AUTH:** Your Bearer token for Sheety

### Usage

Run the script and follow the on-screen prompt to enter your exercise details: python main.py

## Program walk-through

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/x9zSXqH.png" height="80%" width="80%" alt="Workout tracker Steps""/>
<br />
<br />
You'll be prompted to enter your workout:  <br/>
<img src="https://i.imgur.com/IpBfEih.png" height="50%" width="50%" alt="Workout tracker Steps""/>
<br />
<br /> 
The Parsed response from Nutritionix:    <br/>
<img src="https://i.imgur.com/OZ6O0Nx.png" height="70%" width="80%" alt="Workout tracker Steps""/>
<br />
<br /> 
The Parsed response from Sheety:    <br/>
<img src="https://i.imgur.com/pVniUv4.png" height="50%" width="50%" alt="Workout tracker Steps""/>
<br />
<br /> 
The Structured data is then added to Google sheets via Sheety:   <br/>
<img src="https://i.imgur.com/wLQZfTC.png" height="50%" width="50%" alt="Workout tracker Steps""/>
<br />
<br /> 
