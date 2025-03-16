import finnhub
import json
import os

# Initialize the Finnhub client with your API key
finnhub_client = finnhub.Client(api_key="cd5d3iqad3i5nc8nt3s0cd5d3iqad3i5nc8nt3sg")

# Request earnings calendar data within a valid date range
earnings_data = finnhub_client.earnings_calendar(_from="2025-02-18", to="2025-02-28", symbol="", international=False)

# Save the data to a JSON file
json_file_path = 'earnings_data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(earnings_data, json_file, indent=4)

os.startfile(json_file_path)

print("Earnings data has been saved to 'earnings_data.json'.")
