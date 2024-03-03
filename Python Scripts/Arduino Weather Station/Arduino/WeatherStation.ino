#include <Arduino_MKRIoTCarrier.h>
#include <WiFiNINA.h>
#include <ThingSpeak.h>

#define WIFI_SSID "WIFI Name"
#define WIFI_PASS "WIFI Password"

MKRIoTCarrier carrier;
float temperature;
float humidity;
float pressure;

// ThingSpeak Channel Settings
unsigned long channelID = Channel ID; // Replace with your ThingSpeak Channel ID
const char *apiKey = "Write API Key"; // Replace with your ThingSpeak Write API Key

WiFiClient client; // Declare WiFiClient object

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    Serial.println("Waiting for Serial connection...");
  }

  Serial.println("Serial connected!");

  delay(1500);
  CARRIER_CASE = false;
  carrier.begin();

  // Connect to Wi-Fi
  Serial.print("Connecting to WiFi...");
  if (WiFi.begin(WIFI_SSID, WIFI_PASS) != WL_CONNECTED) {
    Serial.println("Failed to connect to WiFi!");
    while (1) delay(1);
  }
  Serial.println("Connected to WiFi!");
}

void loop() {
  temperature = carrier.Env.readTemperature();
  humidity = carrier.Env.readHumidity();
  pressure = carrier.Pressure.readPressure();

  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println(" °C");

  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("Pressure = ");
  Serial.print(pressure);
  Serial.println(" hPa");

  // Update ThingSpeak
  ThingSpeak.begin(client); // Initialize ThingSpeak with WiFiClient object
  ThingSpeak.setField(1, temperature);
  ThingSpeak.setField(2, humidity);
  ThingSpeak.setField(3, pressure);

  // Send data to ThingSpeak
  int httpCode = ThingSpeak.writeFields(channelID, apiKey);
  Serial.print("HTTP response code: ");
  Serial.println(httpCode);

  if (httpCode == 200) {
    Serial.println("Data sent to ThingSpeak successfully!");
  } else {
    Serial.print("Error sending data to ThingSpeak! HTTP error code: ");
    Serial.println(httpCode);
    Serial.print("ThingSpeak response: ");
    Serial.println(ThingSpeak.getLastReadStatus());
  }

  delay(15000);  // Delay for 15 seconds before sending next update
}
