import socket
import speech_recognition as sr

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # We're just using the default API key
        # To use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
        str = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if "Ride Time" in str:
        pass



















# Default size for receiving stuff on a socket
chunk_size = 128

r = sr.Recognizer()
m = sr.Microphone()

# we only need to calibrate once, before we start listening
with m as source:
    r.adjust_for_ambient_noise(source) 

while True:
    response = None
    #data = raw_input( "Send to server(type END to exit):" )

    # obtain audio from the microphone
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        data = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    data = data.upper()

    #create an INET, STREAMing socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        # Log something like server error?
        s = None
        break

    try:
        s.connect(('localhost',5800))
        s.sendall(data)
        # Wait for a response from the server so we don't
        # get input from the mic while the speaker is still
        # talking.
        response = s.recv(chunk_size)
    except socket.error as msg:
        # Log something like server error
        s.close()
        break

    # Close the socket. It's a one time use.
    s.close()

    # If we said END, break
    if data == "END":
        break

    # If our server is not ok or something, break
    if response is not None and response != 'OK':
        break

print "END OF CLIENT"
