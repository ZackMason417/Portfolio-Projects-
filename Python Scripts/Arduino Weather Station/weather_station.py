import serial
import mysql.connector

# MySQL Configuration
mysql_host = 'localhost'
mysql_user = 'user'
mysql_password = 'Password'
mysql_db = 'MySQL DB'

def read_data_from_serial(ser):
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        print("Received:", data)  # Add this line for debugging
        data_list = data.split(",")
        if len(data_list) == 3:
            return {
                "temperature": data_list[0],
                "humidity": data_list[1],
                "pressure": data_list[2]
            }
    return None

def save_to_mysql(data):
    try:
        conn = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_db
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO weather (temperature, humidity, pressure) VALUES (%s, %s, %s)", (data['temperature'], data['humidity'], data['pressure']))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data saved to MySQL!")
    except Exception as e:
        print("Error saving data to MySQL:", e)

def receive_data():
    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change '/dev/ttyUSB0' to your Arduino's serial port

    while True:
        data = read_data_from_serial(ser)
        if data:
            print("Temperature:", data['temperature'], "°C")
            print("Humidity:", data['humidity'], "%")
            print("Pressure:", data['pressure'], "hPa")
            save_to_mysql(data)

if __name__ == "__main__":
    receive_data()
