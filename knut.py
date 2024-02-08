# Notes From Deep
# We need to save the macros, so that a user doesnt need to create a new macro every single time.
################
# Notes From Zaid
################

# cli of oneClickSolution
# imports------------------------------
import time
import pyautogui
import keyboard
import pickle
# end of imports-----------------------
# i want to some how store the action in a list or something

# -------------------initializations-----------------------------------------------------------
listOfActions = []
# ------------------------------------------------------------------------------
print("Welcome to OCS. Here, you can map a macro to click a button(and more!)")
# choices to make new macro or make a new one.
userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))
while userChoiceToMakeNewMacrosOrUseExisting != 0:
    if userChoiceToMakeNewMacrosOrUseExisting == 0:  # 0 to exit
        exit()
    elif userChoiceToMakeNewMacrosOrUseExisting == 1:  # 1 to use already created shortcuts
        # print("\nwe are working on this bit...\n")
        inputMacroKey = pickle.load(open("inputMacroKeyStoringFile.dat", "rb"))
        print("waiting for the macro key to be pressed...")
        keyboard.wait(inputMacroKey)
        listOfActions = pickle.load(open("listOfActionStoringFile.dat", "rb"))
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
            # elif i[0] == "KeyCombination":
            #     print(i)
            #     for key in i[1]:
            #         pyautogui.keyDown(key)
            #     for key in range(-1, -len(i[1])):
            #         pyautogui.keyUp(key)
            #     continue
            #hotkey method
            elif i[0] == "KeyCombination":
                if len(i[1]) == 2:
                    pyautogui.hotkey(i[1][0], i[1][1])
                elif len(i[1]) == 3:
                    pyautogui.hotkey(i[1][0], i[1][1], i[1][2])
                elif len(i[1]) == 4:
                    pyautogui.hotkey(i[1][0], i[1][1], i[1][2], i[1][3])
                else:
                    print("Are you sure you added the correct key combination? This feature only works with a combination containing 2-4 keys.")
                # pyautogui.hotkey(i[1])
    elif userChoiceToMakeNewMacrosOrUseExisting == 2:  # 2 to create new macros
        print("press the key to which you want to map the action and then press the escape key:")
        time.sleep(0.5)#it was registering enter without this delay
        inputMacroKey = keyboard.record(until='esc')
        print(inputMacroKey)
        inputMacroKey = str(inputMacroKey[0])
        inputMacroKey = inputMacroKey[14:-6]
        print("Your selected macro key was --->", inputMacroKey)
        pickle.dump(inputMacroKey, open("inputMacroKeyStoringFile.dat", "wb"))
        while True:  # asking the user what action he/she wants to execute. 0 to exit
            newMacroActionType_UserInput = int(input(
                "Enter the number corresponding to the choice: \n0. Go Back\n1. Mouse Single Click\n2. Mouse Double Click\n3. Mouse Drag\n4. Key Press\n5. Text\n6. Key Combination\nYour Input ---> "))
                #1. Mouse Single Click
                #2. Mouse Double Click
                #3. Mouse Drag
                #4. Key Press
                #5. Text
                #6. Key Combination
            if newMacroActionType_UserInput == 0:
                userChoiceToMakeNewMacrosOrUseExisting = int(input(
                    "\nYou got back\n\nEnter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))
                break
            while newMacroActionType_UserInput != 0:
                if newMacroActionType_UserInput == 1:  # choice for single click
                    input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                    for i in range(1, input_delay+1):
                        print("tik tik", i)
                        time.sleep(1)
                    listForMouseSingleClick = ["MouseSingleClick", pyautogui.position().x, pyautogui.position().y]
                    listOfActions.append(listForMouseSingleClick)
                    break
                elif newMacroActionType_UserInput == 2:# Choice For Double Click
                    #here goes the code for double click
                    input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                    for i in range(1, input_delay+1):
                        print("tik tik", i)
                        time.sleep(1)
                    listForMouseDoubleClick = ["MouseDoubleClick", pyautogui.position().x, pyautogui.position().y]
                    listOfActions.append(listForMouseDoubleClick)
                    break
                elif newMacroActionType_UserInput == 3:#for mouse drag
                    # print("This is for mouse drag which, isnt completed yet.")
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
                    break
                elif newMacroActionType_UserInput == 4:#For Keypress
                    print("Press the key you want to be pressed with the macro(press escape after pressing the key)")
                    time.sleep(1)
                    actionKey = keyboard.record(until='esc')#its the key the user wants the program to press after he presses the macro key
                    actionKey = str(actionKey[0])
                    print(actionKey)
                    actionKey = actionKey[14:-6]
                    print("The key you pressed was --->", actionKey)
                    listForKeypresses = ["Keypress", actionKey]
                    listOfActions.append(listForKeypresses)
                elif newMacroActionType_UserInput == 5:#for text
                    actionText = input("Enter the text you want to be typed with the macro(press escape after pressing the key)\nYour Input --->")
                    listForText = ["Text", actionText]
                    listOfActions.append(listForText)
                elif newMacroActionType_UserInput == 6:#for Key Combination
                    actionKeyCombination = input("Enter the key combination/shortcut you want the macro to perform(Eg: ctrl,shift,alt,v)")
                    actionKeyCombination = actionKeyCombination.split(',')
                    listForKeyCombination = ["KeyCombination", actionKeyCombination]
                    listOfActions.append(listForKeyCombination)                    
                break
        pickle.dump(listOfActions, open("listOfActionStoringFile.dat", "wb"))
    else:#for an invalid input
        print("\nInvalid input try again!\n")
        userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))
