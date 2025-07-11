import pyttsx3
import requests
from bot import ipadress
engine = pyttsx3.init()

#engine.setProperty("rate", 100)
engine.setProperty("volume", 1)

voices = engine.getProperty("voices")

#for index, voice in enumerate(voices):
#    print(f"Voz {index}: {voice.name}: {voice.languages}")

engine.setProperty("voice", voices[0].id)


def dato_random():
    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data("text", "no se pudo obtener la informacion")
    else:
        return "La pagina no pasó una respuesta correcta intentalo mas tarde"


#def localizame():
#    url = f'http://ipwho.is/{ipadress}'
#    response = requests.get(url)
#
#
#    
#    if response.status_code == 200:
#        data = response.json()
#        return data("country")
#    else:
#        return "La pagina no pasó una respuesta correcta intentalo mas tarde"
#    
#    