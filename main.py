import bing
import pyttsx
import sys


with open('addresses.txt', 'r') as f:
    addresses = f.readlines()

origin = addresses[0]
destination = addresses[1]

request = bing.make_request(origin, destination)

if request is None:
    sys.exit()

#print request['resourceSets'][0]['estimatedTotal']

info = bing.parse_request(request)

print info

engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')

#for voice in voices:
#    print "Using voice:", repr(voice)
#    engine.setProperty('voice', voice.id)
#    engine.say("Hi there, how's you ?")

#    engine.say("Hi there Alan. I am Ride Time.")

#    engine.say("Sunday Monday Tuesday Wednesday Thursday Friday Saturday")
#    engine.say("Violet Indigo Blue Green Yellow Orange Red")
#    engine.say("Apple Banana Cherry Date Guava")
#engine.runAndWait()

voices = engine.getProperty('voices')
for voice in voices:
    print "Using voice:", repr(voice)
    print voice.age, voice.gender, voice.languages, voice.name

#    engine.setProperty('voice', voice.id)
#    engine.say("Hi there, how're you ?")
#engine.runAndWait()
