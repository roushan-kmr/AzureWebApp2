import network
import urequests
import time
import json

# Replace with your network credentials
WIFI_SSID = "RKTP-LINK-IOT"
WIFI_PASSWORD = "Plm#235461"

# Replace with the API endpoint URL
API_URL = "http://192.168.29.136:5000/todos/1"

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

def get_data_from_api(url):
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)
    data = get_data_from_api(API_URL)
    if data:
        print("Data received:", data)
        # Process the data as needed