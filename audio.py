from gtts import gTTS
import pygame

class Audio:

    def play(self, sound):
        pygame.init()
        pygame.mixer.init()
        sfx = pygame.mixer.Sound(sound)
        pygame.mixer.Sound.play(sfx)
        pygame.time.delay(int(sfx.get_length() * 1000))

        pygame.quit()

    def gen_sound(self, text: str, file_name: str = "default.mp3", play_sound: bool = True):
        tts = gTTS(text=text, lang='pt-br')
        tts.save(file_name)

        if play_sound:
            self.play(file_name)

    def get_audio_input(self, recognizer, source, listen_timeout: int):
        audio = recognizer.listen(source, listen_timeout)
        return recognizer.recognize_google(audio, language="pt-BR")