import webbrowser
import wikipedia
while True:
    n= input("Hi, please input the word that you want to search")
    if n:
        a = input("press enter to show it here, press w to show it on the browser.")
        if a == 'w':
            webbrowser.open("http://wikipedia.org/wiki/{0}".format(n))
        else:
            try:
                print(wikipedia.page(n).content)
            except wikipedia.exceptions.DisambiguationError:
                print("be more specific")
            except wikipedia.exceptions.PageError:
                print("page was not found:(")
