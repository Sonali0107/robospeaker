import pyttsx3
while True:
    text = input("Enter the text to speak")
    if text == 'q' :
        break
    sound = pyttsx3.init()
    sound.say(text)
    sound.runAndWait()









