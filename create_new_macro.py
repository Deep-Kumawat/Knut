# cli of knut
# imports------------------------------
import time
import pyautogui
import keyboard
import pickle
import subprocess
import sys
# end of imports-----------------------

# -------------------initializations-----------------------------------------------------------
listOfActions = []
# ------------------------------------------------------------------------------
print("Welcome to Knut. Here, you can map a macro to click a button(and more!)")
# choices to make new macro or make a new one.
# userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\n --> "))
def createNewMacro():
    userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Create new macros\n--> "))
    while True:
        if userChoiceToMakeNewMacrosOrUseExisting == 0:  # 0 to exit
            return -1
        elif userChoiceToMakeNewMacrosOrUseExisting == 1:  # 1 to create new macros
            print("press the key to which you want to map the action and then press the escape key:")
            time.sleep(0.5)#it was registering enter without this delay
            inputMacroKey = keyboard.record(until='esc')
            # print(inputMacroKey)
            inputMacroKey = str(inputMacroKey[0])
            inputMacroKey = inputMacroKey[14:-6]
            print("Your selected macro key was --> ", inputMacroKey)
            pickle.dump(inputMacroKey, open("inputMacroKey.dat", "wb"))
            newMacroActionType_UserInput = int(input(
                "Enter the number corresponding to the choice: \n0. Go Back\n1. Mouse Single Click\n2. Mouse Double Click\n3. Mouse Drag\n4. Key Press\n5. Text\n6. Key Combination\n7. Terminal Command\n--> "))
            if newMacroActionType_UserInput == 0:
                userChoiceToMakeNewMacrosOrUseExisting = int(input(
                    "\nYou got back\n\nEnter the number corresponding to the choice: \n0. Exit\n1. Create new macros\n2. Use your created shortcuts\n--> "))
                continue
            if newMacroActionType_UserInput == 1:  # choice for single click
                input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                for i in range(1, input_delay+1):
                    print("tik tik", i)
                    time.sleep(1)
                listForMouseSingleClick = ["MouseSingleClick", pyautogui.position().x, pyautogui.position().y]
                listOfActions.append(listForMouseSingleClick)
                continue
            elif newMacroActionType_UserInput == 2:# Choice For Double Click
                #here goes the code for double click
                input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                for i in range(1, input_delay+1):
                    print("tik tik", i)
                    time.sleep(1)
                listForMouseDoubleClick = ["MouseDoubleClick", pyautogui.position().x, pyautogui.position().y]
                listOfActions.append(listForMouseDoubleClick)
                continue
            elif newMacroActionType_UserInput == 3:#for mouse drag
                input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the START position of the mouse drag:- "))
                for i in range(1, input_delay+1):
                    print("tik tik", i)
                    time.sleep(1)
                XstartPositionForDrag = pyautogui.position().x
                YstartPositionForDrag = pyautogui.position().y
                input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the END position of the mouse drag:- "))
                XendPositionForDrag = pyautogui.position().x
                YendPositionForDrag = pyautogui.position().y
                for i in range(1, input_delay+1):
                    print("tik tik", i)
                    time.sleep(1)
                listForMouseDrag = ["MouseDrag", [XstartPositionForDrag, YstartPositionForDrag], [XendPositionForDrag, YendPositionForDrag]]
                listOfActions.append(listForMouseDrag)
                continue
            elif newMacroActionType_UserInput == 4: #For Keypress
                print("Press the key you want to be pressed with the macro(press escape after pressing the key)")
                time.sleep(1)
                actionKey = keyboard.record(until='esc')#its the key the user wants the program to press after he presses the macro key
                actionKey = str(actionKey[0])
                print(actionKey)
                actionKey = actionKey[14:-6]
                print("The key you pressed was --> ", actionKey)
                listForKeypresses = ["Keypress", actionKey]
                listOfActions.append(listForKeypresses)
                
            elif newMacroActionType_UserInput == 5: #for text
                actionText = input("Enter the text you want to be typed with the macro(press escape after pressing the key)\n--> ")
                listForText = ["Text", actionText]
                listOfActions.append(listForText)
                continue
            elif newMacroActionType_UserInput == 6: #for Key Combination
                actionKeyCombination = input("Enter the key combination/shortcut you want the macro to perform(Eg: ctrl,shift,alt,v)")
                actionKeyCombination = actionKeyCombination.split(',')
                listForKeyCombination = ["KeyCombination", actionKeyCombination]
                listOfActions.append(listForKeyCombination)
                continue                 
            elif newMacroActionType_UserInput == 7: #for terminal commands
                terminalCommand = input("Enter terminal command that you want to execute: ")
                listForKeyCombination = ["TerminalCommand", terminalCommand]
                listOfActions.append(listForKeyCombination)
                continue
            else:#for an invalid input
                print("\nInvalid input try again!\n")
                userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Create new macros\n--> "))
            pickle.dump(listOfActions, open("listOfAction.dat", "wb"))
        elif userChoiceToMakeNewMacrosOrUseExisting == 2: # Use existing macros
            return 0
        userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter your choice:\n0. Exit\n1. Add more actions to this macro key"))