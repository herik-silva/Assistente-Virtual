from gtts import gTTS
import pygame
from events import Event
import speech_recognition as sr

events = []

def play(sound):
    pygame.init()
    pygame.mixer.init()
    sfx = pygame.mixer.Sound(sound)
    pygame.mixer.Sound.play(sfx)
    pygame.time.delay(int(sfx.get_length() * 1000))

    pygame.quit()

def gen_sound(text: str, file_name: str = "default.mp3", play_sound: bool = True):
    tts = gTTS(text=text, lang='pt-br')
    tts.save(file_name)

    if play_sound:
        play(file_name)

def get_audio_input(source):
    audio = recognizer.listen(source)
    return recognizer.recognize_google(audio, language="pt-BR")

def add_event(source):
    while(True):
        gen_sound("Criando um novo evento!")
        gen_sound("Informe o Titulo do Evento após o BIP:")
        gen_sound("BIP")

        title = get_audio_input(source)

        gen_sound("Descreva o Evento após o BIP:")
        gen_sound("BIP")
        description = get_audio_input(source)
        
        gen_sound("Informe a data do evento após o BIP:")
        gen_sound("BIP")
        date = get_audio_input(source)

        event = Event(title, description, date)
        print(event.toString())
        
        gen_sound(event.toString() + ". Confirmar?")
        response = get_audio_input(source)
        
        if "sim" in response.lower():
            events.append(event)
            break
    gen_sound("Evento cadastrado!")

def show_events():
    str_event = ""

    for event in events:
        str_event += event.toString() + ". Próximo. "
        print(str_event)

    gen_sound(str_event, play_sound=True)


recognizer = sr.Recognizer()
gen_sound("Fala seu puto!", play_sound=True)

with sr.Microphone() as source:
    while(True):
        gen_sound("Me diga o que você precisa.", play_sound=True)
        audio = recognizer.listen(source)

        try:
            prompt = recognizer.recognize_google(audio, language="pt-BR")

            print("prompt: ", prompt.lower())
            if prompt == "tchau":
                break
            
            elif "novo" in prompt.lower() and "evento" in prompt.lower():
                add_event(source)
            elif(prompt == "eventos"):
                show_events()
            else:
                gen_sound("Você disse: " + prompt, play_sound=True)
        except sr.UnknownValueError:
            gen_sound("Não foi possível entender o áudio.", play_sound=True)
        except sr.RequestError as e:
            gen_sound("Erro na requisição para o serviço de reconhecimento de voz:" + str(e), play_sound=True)