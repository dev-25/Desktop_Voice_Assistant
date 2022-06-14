import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import pywhatkit
import pyjokes
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print('Good Morning!!')

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print('Good Afternoon!!')

    else:
        speak("Good Evening!")
        print('Good Evening!!')

    speak("Please tell me how may I help you sir")
    print('Please tell me how may I help you sir..')


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    # while True:
    a =1
    if a == 1:
        query = takeCommand().lower()

        while 'thank you' not in query:
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia of ", "")
                query = query.replace(" ", "_")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak('opening youtube')


            elif "weather" in query:

                # api_key = "&appid=06c921750b9a82d8f5d1294e1586276f"
                # base_url = "https://api.openweathermap.org/data/2.5/weather?q="
                speak(" City name ")
                print("City name : ")
                city_name = takeCommand()
                # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                api = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=06c921750b9a82d8f5d1294e1586276f"
                response = requests.get(api)
                x = response.json()

                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"] - 273.15
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in celsius unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                        current_pressure) + "\n humidity (in percentage) = " + str(
                        current_humidiy) + "\n description = " + str(weather_description))

                else:
                    speak(" City Not Found ")

            elif 'open google' in query:
                webbrowser.open("google.com")
                speak('opening google')

            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
                speak('opening facebook')

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                speak('opening stackoverflow')

            elif 'open' in query:
                web = query.replace('open', '')
                zx = (web+".com")
                # webb = zx.replace('%20', '')
                # webbrowser.open(webb)
                webbrowser.open(zx)
                speak('opening'+ web)

            elif 'joke' in query:
                a = pyjokes.get_joke()
                print(a)
                speak(a)

            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing ' + song + 'in youtube')
                pywhatkit.playonyt(song)

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(f"Sir, the time is {strTime}")

            query = takeCommand().lower()

        speak('have a nice day Sir')
        print('Have a nice day, Sir!!')
        a=2