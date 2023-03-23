from onosapi import ONOSAPI

# Set the controller IP address and port number
controller_ip = '192.168.1.1'
controller_port = '8181'

# Set the source and destination MAC addresses
src_mac = '00:00:00:00:00:01'
dst_mac = '00:00:00:00:00:02'

# Connect to the ONOS controller
api = ONOSAPI(controller_ip, controller_port)

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

# Create the intent using the ONOSAPI module
response = api.post('intents', data=intent_data)

# Print the response status code
print(f'Response code: {response.status_code}')
