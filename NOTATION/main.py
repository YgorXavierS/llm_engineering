import requests

def main():
    dada = requests.get("https://www.google.com/")
    print(dada.text)


main()