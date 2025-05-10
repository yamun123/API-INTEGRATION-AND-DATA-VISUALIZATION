import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for Seaborn
sns.set(style="whitegrid")

# Replace with your actual OpenWeatherMap API key
API_KEY = 'abc123def456ghi789jkl012mno345pq'  # Replace with your actual API key
CITY = 'Salem,IN'


# Build API URL
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Check for errors in response
if 'list' not in data:
    print(" Error in API response:")
    print(data)
    exit()

# Parse the necessary data
dates = []
temperatures = []
humidities = []

for item in data['list']:
    dates.append(datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S'))
    temperatures.append(item['main']['temp'])
    humidities.append(item['main']['humidity'])

# Plotting
plt.figure(figsize=(14, 6))

# Temperature Plot
plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temperatures, color='orange')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Humidity Plot
plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidities, color='blue')
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

