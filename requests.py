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

def parseRequest(j):
    """
    Takes json response from the Bing Routes API and returns a dictionary of relevant
    information, e.g  route identifier, time took, mileage
    """