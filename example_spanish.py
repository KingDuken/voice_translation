from googletrans import Translator, constants
import speech_recognition as sr
r = sr.Recognizer()
t = Translator()
m = sr.Microphone()
with m as mic:
  r.adjust_for_ambient_noise(mic)
  print("Say something in English...")
  voice = r.listen(mic)
  print("Thank you for your input...")
  try:
    capture = r.recognize_google(voice) # By default, this will capture English words by the user. Changing arguments in "recognize_google" can change this.
    print("I think you said this: {}".format(capture))
  except Exception as e:
    print("Error: {}".format(e))
  output = translator.translate(capture, dest = "es") # This example uses "es" for Espanol, or Spanish. This can be changed.
  print("English: {} ===> Spanish: {}".format(output.origin, output.text))
