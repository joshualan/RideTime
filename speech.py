import pyttsx

# Initialize the voice engine
engine = pyttsx.init()

# Set the rate of talking to 65 words per minute
engine.setPropery('rate', 65)

# Try to find a 'Murican voice. If there are no such
# patriotic voices, any English ones will do. Otherwise,
# use the default. 
voices = engine.getPropery('voices')
for voice in voices:
    if 'english-us' in voice.name:
        english_voice = voice
    elif english_voice is None && 'english' in voice.name:
        english_voice = voice

if english_voice:
    engine.setPropery('voice', english_voice.id
