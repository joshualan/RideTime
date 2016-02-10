import bing
import sys
import speech
import socket

# Default size for receiving stuff on a socket
chunk_size = 128

# TODO: Be able to change shit according to name
def speak_traffic(name):
    """
    Given a name, speak the traffic information configured 
    for that person.
    """
    with open('addresses.txt', 'r') as f:
        addresses = f.readlines()

    origin = addresses[0]
    destination = addresses[1]

    request = bing.make_request(origin, destination)

    if request is None:
        return None

    # Produces a list of dictionaries that contain info of each route
    routes = bing.parse_traffic_data(request)

    # Prepare strings for speech synthesis.
    # TODO: add levels of verbosity
    traffic_strings = []
    for route in routes:
        str = "{} will take ".format(route['description'])

        # Convert the time with traffic to a string
        hours = minutes = 0
        traffic = route['time_traffic'] 
        if traffic['hours'] > 0:
            hours = traffic['hours']
            str += "{} hours, ".format(hours)

        if traffic['minutes'] > 0:
            minutes = traffic['minutes']
            str += "{} minutes, ".format(minutes)

        # Note the normal time
        str += "normally {} minutes.".format(delay)

        traffic_strings.append(str)
    
    # Preach the spoken word sir!
    speech.say(traffic_strings)

def speak_confirmation():
    "Confirms that the app is in listening mode."
    speech.say('Ride Time is listening.')

def main():
    # Create an INET, STREAM-ing socket for our server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        s = None
        sys.exit(1)
    
    try:
        s.bind(('localhost', 5800))
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        sys.exit(1)

    listening = False

    # Starting the server!
    while True:
        c, addr = s.accept()

        data = c.recv(chunk_size)
        
        if data == "END":
            c.send('SHUTDOWN')
            c.close()
            break


        


        names = ['ALAN', "ALLEN", 'COREY', 'PJ']
        l = [name for name in names if "TRAFFIC FOR {}".format(name) in data]
        if len(l) == 1:
            print "Traffic for {}".format(l[0])
            speak_traffic(l[0])

        elif len(l) > 1:
            speech.say("Ambiguous request.")

        elif data:
            print "Server receives {} from {}:{}!".format(data, addr[0], addr[1])
            # speak_traffic("ALAN")
            
        c.send('OK')
        c.close()

    print "Server has had enough of yo shit" 
    s.close()

if __name__ == '__main__':
    main()
