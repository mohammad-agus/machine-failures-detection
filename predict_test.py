import requests

condition = {
    'type': 'l',
    'air_temperature_k': 300.5,
    'process_temperature_k': 309.6,
    'rotational_speed_rpm': 1390,
    'torque_nm': 120,  # 48.4,
    'tool_wear_min': 194,
    'machine_failure': 0
}

url = 'http://0.0.0.0:9696/predict'
response = requests.post(url=url, json=condition).json()

print(response)
