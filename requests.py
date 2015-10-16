__author__ = 'aestrada'

import re
import config
import urllib2
import json

def makeRequest(origin , destination):
    "This returns a json of a request to Bing's Route API."

    # Remove all commas
    rx  =  '[,]'

    origin = re.sub(rx, '', origin)
    destination = re.sub(rx, '', destination)

    # Replace all spaces with +
    rx  = '[ ]'

    origin = re.sub(rx, '+', origin)
    destination = re.sub(rx, '+', destination)

    # Options are including traffic and to give 3 routes
    # TODO: maybe give more options?
    flags = '&optmz=timeWithTraffic&maxSolns=3'

    url = ''.join(['http://dev.virtualearth.net/REST/V1/Routes?wp.0=',origin,flags,'&wp.1=',destination,'&key=',config.key])

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError, e:
        print "There was an error in making the request: {}".format(e)
        return None

    j = json.load(response)

    # Check to make sure that our credentials is good
    if j['statusDescription'] != "OK":
        print "The request was invalid."
        return None

    return j

def parseRequest(data):
    """
    Takes json response from the Bing Routes API and returns a dictionary of relevant
    information, e.g  route identifier, time took, mileage
    """

    numRoutes = data['resourceSets'][0]['estimatedTotal']

    # Array of dictionaries to be returned
    routes = []

    legsInfo = []

    # Start parsing the json file to build the route information
    for resource in data['resourceSets'][0]['resources']:

        # Time of travel without traffic
        time = resource['travelDuration']
        rideTime = {'hours': time/3600, 'minutes': (time % 3600)/60, 'seconds': (time % 3600 % 60)}

        # Time of travel with traffic
        time = resource['travelDurationTraffic']
        rideTimeTraffic = {'hours': time/3600, 'minutes': (time % 3600)/60, 'seconds': (time % 3600 % 60)}

        route = {'time': rideTime,
                 'timeTraffic': rideTimeTraffic,
                 'congestion': resource['trafficCongestion'],
                 'description': resource['routeLegs'][0]['description']}

        routes.append(route)

        # I'M AN IDIOT AND THIS IS ALL USELESS
        # # Sort the legs of each route according to travel distance to help
        # # figure out the unique identifying leg of each route
        # legs = resource['routeLegs'][0]['itineraryItems']
        # legs = sorted(legs, key=lambda leg: leg['travelDistance'], reverse=True)
        #
        # for leg in legs:
        #     print leg['travelDistance']
        #     for detail in leg['details']:
        #         if 'names' in detail:
        #             route['longestLeg'] = detail['names'][0]
        #             break
        #     if 'travelDistance' in route:
        #         break
        #
        # print route['longestLeg']
        #
        # legsInfo.append(legs)
