from environment import get_values
import requests
import json

# { 'temperature' 'humidity 'battery' }
def send(data):
  envs = get_values()
  url = envs['GOOGOLE_SHEET_URL']
  json_data = json.dumps(data)
  result = requests.post(url, json_data, headers={'Content-Type': 'application/json'})
  return result.json()

if __name__ == '__main__':
  result = send({'temperature': 23.2, 'humidity': 55, 'battery': 99})
  print(result)
