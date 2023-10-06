from events import *
from events import Event
import speech_recognition as sr

from audio import Audio

class Assistent:
    _event_list: EventList
    _audio: Audio
    _listen_timeout: int

    def __init__(self, listen_timeout: int = 5):
        self._event_list = EventList()
        self._audio = Audio()
        self._listen_timeout = listen_timeout

    def add_event(self, recognizer, source):
        while(True):
            self._audio.gen_sound("Criando um novo evento!")
            self._audio.gen_sound("Informe o Título do Evento após o BIP:")
            self._audio.gen_sound("BIP")

            title = self._audio.get_audio_input(recognizer, source, self._listen_timeout)

            self._audio.gen_sound("Descreva o Evento após o BIP:")
            self._audio.gen_sound("BIP")
            description = self._audio.get_audio_input(recognizer, source, self._listen_timeout)
            
            self._audio.gen_sound("Informe a data do evento após o BIP:")
            self._audio.gen_sound("BIP")
            date = self._audio.get_audio_input(recognizer, source, self._listen_timeout)

            event = Event(title, description, date)
            print(event.toString())
            
            self._audio.gen_sound(event.toString() + ". Confirmar?")
            response = self._audio.get_audio_input(recognizer, source, self._listen_timeout)
            
            if "sim" in response.lower():
                self._event_list.add_event(event)
                break

        self._audio.gen_sound("Evento cadastrado!")

    def show_events(self):
        events = self._event_list.show_events()

        self._audio.gen_sound(events)

    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            while(True):
                self._audio.gen_sound("Me diga o que você precisa.", play_sound=True)

                try:
                    prompt = self._audio.get_audio_input(recognizer, source, self._listen_timeout)

                    print("prompt: ", prompt.lower())
                    if prompt == "tchau":
                        break
                    
                    elif "novo" in prompt.lower() and "evento" in prompt.lower():
                        self.add_event(recognizer, source)
                    elif(prompt == "eventos"):
                        self.show_events()
                    else:
                        self._audio.gen_sound("Você disse: " + prompt, play_sound=True)
                except sr.UnknownValueError:
                    self._audio.gen_sound("Não foi possível entender o áudio.", play_sound=True)
                except sr.RequestError as e:
                    self._audio.gen_sound("Erro na requisição para o serviço de reconhecimento de voz:" + str(e), play_sound=True)