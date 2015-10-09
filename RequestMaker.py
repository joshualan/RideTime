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
    flags = '&optmz=timeWithTraffic&maxSolns=3'

    url = ''.join(['http://dev.virtualearth.net/REST/V1/Routes?wp.0=',origin,flags,'&wp.1=',destination,'&key=',config.key])

    response = urllib2.urlopen(url)
    return json.load(response)

