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


# Possible requests to server:
# LISTEN - server goes into listening mode
# STOP - quit out of listening mode without doing anything
# REPEAT - ask the person to repeat themselves
# TRAFFIC {name} - speaks traffic for a person
# MESSAGES {name} - speaks out messages for a person
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

        # Sanity check
        data = data.upper()

        # Split the words in the request
        request = data.split()

        # Error if our request isn't length of 1 or 2
        if len(request) != 1 or len(request) != 2:
            c.send('BAD REQUEST')
            c.close()
            continue

        command = request[0]
        name = request[1] if len(request) == 2 else None
        
        if command == "LISTEN":
            listening = True
            c.send('WAITING')
            c.close()
        
        if listening:
            if command == "QUIT":
                c.send('SHUTDOWN')
                c.close()
                break

            # Don't do anything
            if command == "STOP":
                pass
            elif command == "REPEAT":
                # Say something like "I did not understand you, repeat?"
                pass
            elif command = "TRAFFIC":
                names = ['ALAN', "ALLEN", 'COREY', 'PJ']
                # This slice of code should be replaced by a cal to a DB
                if name in names:
                    print "Traffic for {}".format(name)
                    speak_traffic(name)
                else:
                    # Say something here like "Dunno who the fuck that is"
                    pass
            elif command = "MESSAGES":
                pass
            # If we got here, we somehow got a bad request :(
            else:
                c.send('BAD REQUEST')
                c.close()
                continue

            # We're not listening anymore :)
            listening = False
            c.send('OK')
            c.close()

    print "Server has had enough of yo shit" 
    s.close()

if __name__ == '__main__':
    main()
