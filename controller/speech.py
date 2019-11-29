#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3

# pyttsx3 initialization
engine = pyttsx3.init()
engine.setProperty('rate', 200)    # Speed percent (can go over 100)
engine.setProperty('volume', 1)  # Volume 0-1

run_program = True
r = sr.Recognizer()

########
def say_it(sentence):
    # print(sentence)
    engine.say(sentence)



####### debug
# dt = getWebAppResponse("12435")
# sayOrderContentOutLoud(dt)
####### debug


def buildAndVerifyFeedback(googleTextResponse1, googleTextResponse2, googleTextResponse3):


def getApplicationResponse(googleTextResponse):
    wordArray = googleTextResponse.split()

    if "quit" in wordArray or "stop" in wordArray:
        print("terminating application. See you next time!")
        engine.say("terminating application. See you next time!")
        engine.runAndWait()
        return "QUIT_APP"

    if "hello" in wordArray or "greetings" in wordArray:
        engine.say("Hello there!")
        engine.runAndWait()
        return "Hello there!"

    engine.say("I'm listening...")
    engine.runAndWait()
    return "I'm listening..."

def createFeedbackCourse(course):
    with sr.Microphone() as source:
        while True:
            print("asking for course feedback")
            engine.say("What did you think of '" + course + "'")
            engine.runAndWait()
            audio = r.listen(source)
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                googleOrderResponse = r.recognize_google(audio)
                print("verifying feedback")
                engine.say("You said '" + googleOrderResponse + "'")
                engine.runAndWait()

                feedbackCourse = getApplicationResponse(googleOrderResponse)

                print(feedbackCourse)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                engine.say("Google Speech Recognition could not understand audio")
                engine.runAndWait()
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
                engine.runAndWait()

            print("asking for teacher feedback")
            engine.say("What did you think of  the '" + course + "' teacher")
            engine.runAndWait()
            audio = r.listen(source)
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                googleOrderResponse = r.recognize_google(audio)
                print("verifying feedback")
                engine.say("You said '" + googleOrderResponse + "'")
                engine.runAndWait()

                feedbackTeacher = getApplicationResponse(googleOrderResponse)

                print(feedbackTeacher)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                engine.say("Google Speech Recognition could not understand audio")
                engine.runAndWait()
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
                engine.runAndWait()

            print("asking for test feedback")
            engine.say("What did you think of  the '" + course + "' test")
            engine.runAndWait()
            audio = r.listen(source)
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                googleOrderResponse = r.recognize_google(audio)
                print("verifying feedback")
                engine.say("You said '" + googleOrderResponse + "'")
                engine.runAndWait()

                feedbackTest = getApplicationResponse(googleOrderResponse)

                print(feedbackTest)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                engine.say("Google Speech Recognition could not understand audio")
                engine.runAndWait()
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
                engine.runAndWait()
