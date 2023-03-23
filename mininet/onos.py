import requests

# Set the controller IP address and port number
controller_ip = '192.168.1.1'
controller_port = '8181'

# Set the source and destination MAC addresses
src_mac = '00:00:00:00:00:01'
dst_mac = '00:00:00:00:00:02'

# Define the ONOS REST API endpoint for intents
intents_url = f'http://{controller_ip}:{controller_port}/onos/v1/intents'

# Define the JSON data for the intent
intent_data = {
    'type': 'HostToHostIntent',
    'appId': 'org.onosproject.cli',
    'one': {
        'type': 'Host',
        'mac': src_mac
    },
    'two': {
        'type': 'Host',
        'mac': dst_mac
    }
}

# Set the authentication credentials
username = 'your_username'
password = 'your_password'

# Create the authorization header
auth_header = f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}'

# Send a POST request to create the intent
response = requests.post(intents_url, json=intent_data, headers={'Authorization': auth_header})

# Print the response status code
print(f'Response code: {response.status_code}')
