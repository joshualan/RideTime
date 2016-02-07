import pyttsx

# Initialize the voice engine
engine = pyttsx.init()

# Set the rate of talking to 120 words per minute
engine.setProperty('rate', 150)

# Try to find a 'Murican voice. If there are no such
# patriotic voices, any English ones will do. Otherwise,
# use the default. 
voices = engine.getProperty('voices')
english_voice = None
for voice in voices:
    if 'english-us' in voice.name:
        english_voice = voice
    elif english_voice is None and 'english' in voice.name:
        english_voice = voice

if english_voice:
    engine.setProperty('voice', english_voice.id)
                      
def say(speeches):
    """
    Send a string to be said to the speech engine and wait
    for it to finish.
    """
    for s in speeches:
        engine.say(s)

    engine.runAndWait()

def set_rate(rate):
    "Set the words per minute rate for the engine."
    engine.setProperty('rate', rate)
