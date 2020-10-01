import requests, json
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError

print("Let's look at the weather today!")
ZIPCODE = input("Enter zipcode: ")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
URL = BASE_URL + "zip=" + ZIPCODE + ",us&appid=" + "98629f50c06f233ce10f89323ae5167c" + "&units=imperial"

def getValidInput():
    print("Let's try it again!")
    ZIPCODE = input("Enter zipcode: ")

def validateZipcode():
    if not (ZIPCODE.isdigit()):
        print("Invalid entry.")
        getValidInput()
    elif len(ZIPCODE) != 5:
        print("Invalid entry.")
        getValidInput()

def anotherSearch():
    print("Would you like another search? (yes or no) ")
    another_search = input()
    if (another_search == "yes" or another_search == "y"):
        nextSearch()
    elif (another_search == "no" or another_search == "n"):
        print("Thank you! Have a great day!")
    else:
        nextSearch()

def getWeather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "zip=" + ZIPCODE + ",us&appid=" + "98629f50c06f233ce10f89323ae5167c" + "&units=imperial"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data ["main"]
        sys = data["sys"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        country = sys["country"]
        try:
            r = requests.get(URL)
        except ConnectionError:
            print("An error occured. Please re-run this module to try again.")
        else:
            print(f"{ZIPCODE:-^30}")
            print(f"Temperature: {temperature}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"{country:-^30}")
        finally:
            anotherSearch()

def nextSearch():
    print("Let's try it again!")
    next_zipcode = str(input("Enter next zipcode: "))
    if not(next_zipcode.isdigit()):
        print("Oh, no! Invalid entry. Let's try it again!")
        getNextWeather()
    elif len(next_zipcode) != 5:
        print("Oh, no! Invalid entry. Let's try it again!")
        getNextWeather()
    NEXT_URL = BASE_URL + "zip=" + next_zipcode + ",us&appid=" + "98629f50c06f233ce10f89323ae5167c" + "&units=imperial"
    response = requests.get(NEXT_URL)
    if response.status_code == 200:
        data = response.json()
        main = data ["main"]
        sys = data["sys"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        country = sys["country"]
        try:
            r = requests.get(URL)
        except ConnectionError:
            print("An error occured. Please re-run this module to try again.")
        except NewConnectionError:
            print("An error occured. Please re-run this module to try again.")
        else:
            print(f"{next_zipcode:-^30}")
            print(f"Temperature: {temperature}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"{country:-^30}")
        finally:
            anotherSearch()

def getNextWeather():
    next_zipcode = str(input("Enter next zipcode: "))
    NEXT_URL = BASE_URL + "zip=" + next_zipcode + ",us&appid=" + "98629f50c06f233ce10f89323ae5167c" + "&units=imperial"
    response = requests.get(NEXT_URL)
    if response.status_code == 200:
        data = response.json()
        main = data ["main"]
        sys = data["sys"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        country = sys["country"]
        try:
            r = requests.get(URL)
        except ConnectionError:
            print("An error occured. Please re-run this module to try again.")
        except NewConnectionError:
            print("An error occured. Please re-run this module to try again.")
        else:
            print(f"{next_zipcode:-^30}")
            print(f"Temperature: {temperature}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"{country:-^30}")
        finally:
            anotherSearch()

validateZipcode()
getWeather()