'''
Created on Jan 23, 2018

@author: dobreandragos
'''

from Tests.ChiSquare import *
from Tests.RankSum import *


def printMenu():
    print("\n Menu: \n")
    print("1. Chi-Square")
    print("0. Exit")


def run():
    stop = False

    while stop == False:
        printMenu()

        try:
            option = int(input("Option: "))
        except ValueError:
            print("The inserted value is not a number")
            continue

        if option == 1:
            handleChiSq()
        if option == 2:
            handleRankSum()


# Handling functions

def readArrayOfFloats(message):
    values = raw_input(message).split()
    values = [float(list_item) for list_item in values]

    return values


def handleChiSq():
    currentValues = readArrayOfFloats("Current values separated by ' ': ")
    expectedValues = readArrayOfFloats("Expected values separated by ' ': ")

    aRDegree = float(raw_input("Accept/reject degree: "))

    chisq, criticalPoint, accepted = chi_compute(currentValues, expectedValues, aRDegree)

    print("\n    ChiSq value: " + str(chisq) + " critical point: " + str(criticalPoint) + " accepted: " + str(accepted))


def handleRankSum():
    groupA = readArrayOfFloats("GroupA separated by ' ': ")
    groupB = readArrayOfFloats("GroupB separated by ' ': ")
    print(ranksums(groupA, groupB))


run()
