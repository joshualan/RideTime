import json
import urllib2

from RequestMaker import makeRequest

origin = "322.5 Western Ave, Cambridge MA"

destination = "14 Oak Park Drive, Bedford MA"

url = origin + destination

url = url.replace(" ", "+")
url = url.replace(",", "")

#print url

makeRequest(origin, destination)


#json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?origins=322.5+Western+Ave+Cambridge+MA&destinations=14+Oak+Park+Drive+Bedford+MA"))
#json.load(urllib2.urlopen(url))
