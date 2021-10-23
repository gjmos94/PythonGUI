import tkinter as tk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import itertools as ite
from itertools import combinations as com


def listCombo(targetVal, bDict): # parameters for target Value and Dictionary with invoice#(keys) and amounts(values)

    aDict = {}  # Dict to hold Values with alphabetized letters
    dictChar = "A"
    for values in bDict:    # loop will create a key with the char Val "A" along with the first value
        aDict[dictChar] = bDict[values] # loop will continue adding 1 to Char to get the next letter
        dictChar = chr(ord(dictChar)+1)
    newLoopCount = len(aDict)   # secondary counter for combinations loop
    # example desired value to find in combinations
    print(aDict)
    comboMaker(aDict, newLoopCount, targetVal, bDict) # first iteration of function called for combination of all values

    while newLoopCount > 2:     # Will keep doing combinations of elements down to 2
        newLoopCount = newLoopCount - 1 # newLoop counter decreases to keep lowering number of elements for combinations
        comboMaker(aDict, newLoopCount, targetVal, bDict)
        # continues loop for function with the updated number of elements


def comboMaker(someDict, newLoop,targetVal2, secondDict):

    #print(newLoop)  # prints number of elements for combinations
    res = ite.combinations(someDict, newLoop)   #calls for combinations of key values in dictionary with N
    allCombos = list(res)   # puts Combinations object into a list
    secondLength = len(allCombos)   #second length for inner loop

    #print(len(allCombos))

    for i in range(len(allCombos)): # will repeat until i reaches allCombos size
        if secondLength > 0:        # if second length is met, we exit the loop to continue with the next combo
            count = 2  # counter for string chars limit
            checker = 0  # value that will hold the added value of combo to check with target value
            keyStr = str(allCombos[i])  # makes Key value used to add from dictionary value
            while count < len(keyStr):  #counter for char positions. this will make sure to go though all the combo string  ex. ("A","B","C")
                newCount=0
                checker = checker + someDict[keyStr[count]] # adds the value of the Key str with
                count = count + 5  # fixed count to find Chars for Key values in string
            if checker == targetVal2:  # if target val is found, print
                print("Found it!!!")
                print(checker)
                print(allCombos[i])         # prints combination with Alphabet dictionary
                count = 2                   #second counter to check char of combinations
                checkerReset = 0                 #second checker to use with each combination
                finalChecker = 0
                groupCheck = newLoop
                while count < len(keyStr):  # counter for char positions. this will make sure to go though all the combo string  ex. ("A","B","C")
                    checkerReset = checkerReset + someDict[keyStr[count]]  # adds the value of the Key str with
                    newCount = 0
                    finalChecker= checkerReset
                    for value in secondDict:
                        if finalChecker <= targetVal2:
                            if someDict[keyStr[count]] == secondDict[value]:        # checks for same value in original dict
                                if groupCheck != 0:
                                    print(list(secondDict.keys())[newCount])
                                    finalChecker = finalChecker + secondDict[value]
                                    groupCheck = groupCheck - 1
                            newCount = newCount + 1
                    count = count + 5
            secondLength = secondLength - 1 # decrease to continue loop
    allCombos.clear()   # clear for next package

invoiceTeller = []
testDict = {"INV-056566": 5, "INV-056565": 6, "INV-056381": 2, "INV-054079": 4.4, "INV-053791": 8, "INV-5": 4, "INV-6": 4, "INV-7": 4, "INV-8": 69, "INV-9": 1, "INV-10": 4}
listCombo(78, testDict)
