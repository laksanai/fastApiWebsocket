import websocket
import json

# create a JSON object
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# convert the JSON object to a string
json_data = json.dumps(data)

# create a WebSocket connection
ws = websocket.create_connection("ws://192.168.254.69:8008/ws/555666")

# send the JSON data to the server
ws.send(json_data)

# close the WebSocket connection
ws.close()
