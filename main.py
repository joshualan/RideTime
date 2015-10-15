from requests import makeRequest

import pyttsx
import sys

origin = "322.5 Western Ave, Cambridge MA"

destination = "14 Oak Park Drive, Bedford MA"

url = origin + destination

url = url.replace(" ", "+")
url = url.replace(",", "")

request = makeRequest(origin, destination)

if request is None:
    sys.exit()

print request['resourceSets'][0]['estimatedTotal']

#json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?origins=322.5+Western+Ave+Cambridge+MA&destinations=14+Oak+Park+Drive+Bedford+MA"))
#json.load(urllib2.urlopen(url))

# engine = pyttsx.init()
# engine.setProperty('rate', 70)
#
# voices = engine.getProperty('voices')
# for voice in voices:
#     print "Using voice:", repr(voice)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hi there, how's you ?")
#     engine.say("A B C D E F G H I J K L M")
#     engine.say("N O P Q R S T U V W X Y Z")
#     engine.say("0 1 2 3 4 5 6 7 8 9")
#     engine.say("Sunday Monday Tuesday Wednesday Thursday Friday Saturday")
#     engine.say("Violet Indigo Blue Green Yellow Orange Red")
#     engine.say("Apple Banana Cherry Date Guava")
# engine.runAndWait()