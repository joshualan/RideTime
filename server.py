import bing
import sys
import speech
import socket

# TODO: Be able to change shit according to name
def speak_traffic(name):

    with open('addresses.txt', 'r') as f:
        addresses = f.readlines()

    origin = addresses[0]
    destination = addresses[1]

    request = bing.make_request(origin, destination)

    if request is None:
        sys.exit()

    # Produces a list of dictionaries that contain info of each route
    routes = bing.parse_traffic_data(request)

    # Prepare strings for speech synthesis.
    # TODO: add levels of verbosity
    traffic_strings = []
    for i, route in enumerate(routes):
        str = ""
    
        if i == 0:
            str += "{} is the fastest route and ".format(route['description'])
        else:
            str += "{} ".format(route['description'])

        str += " will take "

        # Convert the time with traffic to a string
        hours = minutes = 0
        traffic = route['time_traffic'] 
        if traffic['hours'] > 0:
            hours = traffic['hours']
            str += "{} hours, ".format(hours)

        if traffic['minutes'] > 0:
            minutes = traffic['minutes']
            str += "{} minutes, ".format(minutes)

        delay = ((hours * 60 + minutes) - 
                 (route['time']['hours'] * 60 + route['time']['minutes']))

        # Add a delay
        if delay > 0:
            str += "with {} minutes delay.".format(delay)
        else:
            str += "with no delay."

        traffic_strings.append(str)
    
    # Preach the spoken word sir!
    # for s in traffic_strings:
    #    speech.add_speech(s)

    speech.say(traffic_strings)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('localhost', 12345))

    s.listen(1)

    c, addr = s.accept()

    speak_traffic("ALAN")

    s.close()



if __name__ == '__main__':
    main()
