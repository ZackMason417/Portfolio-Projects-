# Arduino Weather Station with ThingSpeak Integration

This project is an Arduino-based weather station that collects temperature, humidity, and pressure data using an Arduino board with an MKRIoTCarrier and sends this data to ThingSpeak for real-time monitoring and visualization. This allows you to monitor weather conditions remotely.

## Features

- Real-time Weather Data: The weather station collects temperature, humidity, and pressure data.
- ThingSpeak Integration: Sends the data to ThingSpeak for real-time monitoring and visualization.

## Components Used

- Arduino MKR WiFi 1010 with MKRIoTCarrier (Integrated DHT Sensor for temperature and humidity, BMP280 Sensor for pressure)
- WiFi Connection for Internet Connectivity

## Installation

### Arduino Setup:

1. Upload the provided Arduino sketch (`weather_station.ino`) to your Arduino board.

### ThingSpeak Setup:

1. Create a ThingSpeak account at [ThingSpeak.com](https://thingspeak.com/).
2. Create a new channel and note the Channel ID and Write API Key.

### Python Script Setup:

1. Install the required Python libraries:
2. Modify the `weather_station_data.py` script with your ThingSpeak Channel ID and Write API Key.
3. Connect your Arduino board to your computer.

### Run the Python Script:

1. Execute the Python script `weather_station_data.py` to start collecting and sending data to ThingSpeak.

### Visualization:

1. Access your ThingSpeak channel to visualize the live weather data.

## Usage

1. Power on the Arduino Weather Station.
2. Monitor the serial monitor for real-time data readings.
3. Access your ThingSpeak channel to view live weather data.

## Future Upgrades (Possible Additions)

- MySQL Database Integration: Store the collected data in a MySQL database for historical analysis.
- Additional Sensors: Explore adding more sensors for advanced weather monitoring.
- Display Interface: Incorporate an LCD display for local data visualization.

## Contributions

Contributions to improve the project are welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ZackMason417/Portfolio-Projects-/blob/main/Python%20Scripts/Arduino%20Weather%20Station/License.txt) file for details.
