__author__ = 'aestrada'

# For our Bing API key
import config

import json
import requests

def make_request(origin , destination):
    "This returns a json of a request to Bing's Route API."

    # Options are including traffic and to give 3 routes
    # TODO: maybe give more options?
    payload = {'wp.0': origin, 'wp.1': destination,
               'key': config.key,
               'optmz': 'timeWithTraffic',
               'maxSolns': '3'}

    r = requests.get('http://dev.virtualearth.net/REST/V1/Routes', params=payload)

    # Error happened
    if r.status_code  != requests.codes.ok:
        r.raise_for_status()

    # Convert to error
    j = r.json()

    # Check to make sure that our credentials is good
    if j['statusDescription'] != "OK":
        raise ValueError

    return j

def parse_request(data):
    """
    Takes json response from the Bing Routes API and returns a dictionary of relevant
    information, e.g  route identifier, time took, mileage
    """

    num_routes = data['resourceSets'][0]['estimatedTotal']

    # Array of dictionaries to be returned
    routes = []

    # Start parsing the json file to build the route information
    for resource in data['resourceSets'][0]['resources']:

        # Time of travel without traffic
        time = resource['travelDuration']
        ride_time = {'hours': time/3600, 'minutes': (time % 3600)/60, 'seconds': (time % 3600 % 60)}

        # Time of travel with traffic
        time = resource['travelDurationTraffic']
        ride_time_traffic = {'hours': time/3600, 'minutes': (time % 3600)/60, 'seconds': (time % 3600 % 60)}

        route = {'time': ride_time,
                 'timeTraffic': ride_time_traffic,
                 'congestion': resource['trafficCongestion'],
                 'description': resource['routeLegs'][0]['description']}

        routes.append(route)

    return routes
