import requests

sample = {
    'type': 'l',
    'air_temperature_k': 300.5,
    'process_temperature_k': 309.6,
    'rotational_speed_rpm': 1390,
    'torque_nm': 60,  # 48.4,
    'tool_wear_min': 194
}

url = 'http://13.215.200.18/predict'
response = requests.post(url=url, json=sample).json()

print(response)
