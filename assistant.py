
#this change i am doing for git version controlling	

# Follow for more : @divstech

import speech_recognition as sr
import pyttsx3
import wikipedia

def speak(string):
	engine = pyttsx3.init()
	engine.say(string)
	engine.runAndWait()

def uservoice():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak Now ...")
		audio = r.listen(source)
		query = r.recognize_google(audio)
	return query

def useroutput():
	query = uservoice().lower()
	print(f"User Input is : {query}")
	results = wikipedia.summary(query,sentences=3)
	print(results)
	speak("Wikipedia's Answer :")
	speak(results)

speak("Hello Sir, How can I help you ?")
speak("What you want to search ?")
useroutput() 