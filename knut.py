import subprocess
import time
import pyautogui
import keyboard
import pickle
from create_new_macro import createNewMacro

listOfActions = []

try:
    inputMacroKey = pickle.load(open("inputMacroKey.dat", "rb"))
except:
    print("You have no saved shortkeys!")
    makeANewMacroOrNo = input("Make a new macro (y/n)").lower()
    if(makeANewMacroOrNo == "n"):
        exit()
    elif(makeANewMacroOrNo == "y"):
        exit_code = createNewMacro()
        if exit_code == -1:
            exit()
        elif exit_code == 0:
            inputMacroKey = pickle.load(open("inputMacroKey.dat", "rb"))
            print("hello from code 0")

userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice:\n0. Exit\n1. Use existing macros\n2. Create new macro\n--> "))
if(userChoiceToMakeNewMacrosOrUseExisting == 0):
    exit()
elif userChoiceToMakeNewMacrosOrUseExisting == 1:
    print("waiting for the macro key to be pressed...")
    keyboard.wait(inputMacroKey)
    listOfActions = pickle.load(open("listOfAction.dat", "rb"))
    for i in listOfActions:
        if i[0] == "MouseSingleClick":
            xCoordinateOfOriginalMousePosition = pyautogui.position().x
            yCoordinateOfOriginalMousePosition = pyautogui.position().y
            pyautogui.click(i[1], i[2])
            pyautogui.moveTo(xCoordinateOfOriginalMousePosition, yCoordinateOfOriginalMousePosition)
        elif i[0] == "MouseDoubleClick":
            xCoordinateOfOriginalMousePosition = pyautogui.position().x
            yCoordinateOfOriginalMousePosition = pyautogui.position().y
            pyautogui.doubleClick(i[1], i[2])
            pyautogui.moveTo(xCoordinateOfOriginalMousePosition, yCoordinateOfOriginalMousePosition)
        elif i[0] == "MouseDrag":
            pyautogui.moveTo(i[1][0], i[1][1])
            pyautogui.dragTo(i[2][0], i[2][1], button="left")
        elif i[0] == "Keypress":
            keyboard.press(i[1])
        elif i[0] == "Text":
            pyautogui.write(i[1])
        elif i[0] == "KeyCombination":
            if len(i[1]) == 2:
                pyautogui.hotkey(i[1][0], i[1][1])
            elif len(i[1]) == 3:
                pyautogui.hotkey(i[1][0], i[1][1], i[1][2])
            elif len(i[1]) == 4:
                pyautogui.hotkey(i[1][0], i[1][1], i[1][2], i[1][3])
            else:
                print("Are you sure you added the correct key combination? This feature only works with a combination containing [2-4] keys.")
        elif i[0] == "TerminalCommand":
            try:
                result = subprocess.run(i[1], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
                print("Output:", result.stdout)
                # Print the error, if any
                if result.stderr:
                    print("Error:", result.stderr)
                # Print the return code
                print("Return Code:", result.returncode)
            except Exception as e:
                print("An error occurred:", str(e))
elif userChoiceToMakeNewMacrosOrUseExisting == 2: # create new macro
    createNewMacro()
