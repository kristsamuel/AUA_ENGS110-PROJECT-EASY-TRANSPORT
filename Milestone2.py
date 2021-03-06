import json

from math import radians, cos, sin, asin, sqrt

def loadAvailableTransportation():
    with open("all_transport.json") as file_data:
        TransportInform = json.load(file_data)
        return TransportInform

def chooseTransportType(transportation):
    print("Available Transportation Fields are:")
    for key in transportation:
        print("----", key, end=", ----, \n")

    userSelectedField = ""

    while userSelectedField not in transportation.keys() :
        userSelectedField = input("\nPlease select a transportation field from the list above")
        if userSelectedField in transportation.keys():
            currentField = transportation[userSelectedField]

            print("Available Transportation Types for ", userSelectedField, " are: ")
            for key in currentField:
                print("----",   key, end=", -----, \n")

            userSelectedType = input("\nPlease select a transportation type from the list above")
            if userSelectedType in transportation[userSelectedField].keys():
                return userSelectedField, userSelectedType

        else:
            print("the field is wrong.")

def getTransportInformation(transportation, transportField, transportType):
    return transportation[transportField][transportType]

def loadAvailableLocations():
    with open("all_locations.json") as file_data:
        LocationInform = json.load(file_data)
        return LocationInform

def chooseInitialLocation(placeCoordinates):
    print("Available Locations:")
    for key in placeCoordinates:
        print("----", key, end=",----, \n ")

    initialSelectedCountry = ""
    initialSelectedCity = ""

    while initialSelectedCountry not in placeCoordinates.keys() :
        initialSelectedCountry = input("\nPlease select your Country from the list above")
        if initialSelectedCountry in placeCoordinates.keys():
            print("Available Cities:")
            for key in placeCoordinates[initialSelectedCountry]:
                print("----", key, end=", ----, \n")
            while initialSelectedCity not in placeCoordinates[initialSelectedCountry].keys():
                initialSelectedCity = input("\nPlease select your City from the list above")
                if initialSelectedCity in placeCoordinates[initialSelectedCountry].keys():
                    currentPlace = placeCoordinates[initialSelectedCountry][initialSelectedCity]
                    print("Available Places for ", initialSelectedCity, " are: ")
                    for key in currentPlace:
                        print("----", key, end=", ----, \n")
                    initialSelectedPlace = input("\nPlease select your Place from the list above")
                    return initialSelectedCountry, initialSelectedCity, initialSelectedPlace
                else:
                    print("your city is wrong")
        else:
            print("your country is wrong")

def getLocationInformation(location, country , city, place):
    return location[country][city][place]

def chooseFinalLocation(placeCoordinates):
    print("Available Locations:")
    for key in placeCoordinates:
        print("----", key, end=", ----, \n ")

    FinalSelectedCountry = ""
    FinalSelectedCity = ""

    while FinalSelectedCountry not in placeCoordinates.keys() :
        FinalSelectedCountry = input("\nChoose your desired Country to travel from the list above")
        if FinalSelectedCountry in placeCoordinates.keys():
            print("Available Cities:")
            for key in placeCoordinates[FinalSelectedCountry]:
                print("----", key, end=", ----, \n")
            while FinalSelectedCity not in placeCoordinates[FinalSelectedCountry].keys():
                FinalSelectedCity = input("\nChoose your desired City to travel from the list above")
                if FinalSelectedCity in placeCoordinates[FinalSelectedCountry].keys():
                    currentPlace = placeCoordinates[FinalSelectedCountry][FinalSelectedCity]
                    print("Available Places for", FinalSelectedCity, "are:")
                    for key in currentPlace:
                        print("----", key, end=", ----, \n")
                    FinalSelectedPlace = input("\nChoose your desired Place to travel from the list above")
                    return FinalSelectedCountry, FinalSelectedCity, FinalSelectedPlace
                else:
                    print("your desired city is wrong")
        else:
            print("your desired country is wrong")

def getDistance(InitialLatitude, InitialLongitude, FinalLatitude, FinalLongitude):

    InitialLong = radians(InitialLongitude)
    FinalLong = radians(FinalLongitude)
    InitialLat = radians(InitialLatitude)
    FinalLat = radians(FinalLatitude)
    differenceLongitude = FinalLong - InitialLong
    differenceLatitude = FinalLat - InitialLat
    a = sin(differenceLatitude / 2) ** 2 + cos(InitialLat) * cos(FinalLat) * sin(differenceLongitude / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return (c * r)

def main():
    availableTrasportation = loadAvailableTransportation()
    userTransportField, userTransportType = chooseTransportType(availableTrasportation)
    transportInfo = getTransportInformation(availableTrasportation, userTransportField, userTransportType)
    print(json.dumps(transportInfo, indent=4))
    availableLocations = loadAvailableLocations()
    initialCountry, initialCity, initialPlace = chooseInitialLocation(availableLocations)
    FinalCountry, FinalCity, FinalPlace = chooseFinalLocation(availableLocations)
    initiallocationInfo = getLocationInformation(availableLocations, initialCountry, initialCity, initialPlace)
    FinallocationInfo = getLocationInformation(availableLocations, FinalCountry, FinalCity, FinalPlace)
    distance = getDistance(initiallocationInfo["latitude"], initiallocationInfo["longitude"],
                           FinallocationInfo["latitude"], FinallocationInfo["longitude"])
    print(distance, "K.M")

main()
