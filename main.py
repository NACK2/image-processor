# CMPT 120 D300 Yet Another Image Processer
# Author: Nicholas Kang 301452347
# Date: November 28, 2021

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
  "Q: Quit",
  "O: Open Image",
  "S: Save Current Image",
  "R: Reload Original Image"
  ]

# list of basic operation options
basic = [
  "1: Apply Red Filter",
  "2: Apply Green Filter",
  "3: Apply Blue Filter",
  "4: Apply Sepia Filter",
  "5: Apply Warm Filter",
  "6: Apply Cold Filter",
  "7: Switch to Advanced Functions"
]

# list of advanced operation options
advanced = [
  "1: Rotate Left",
  "2: Rotate Right",
  "3: Double Size",
  "4: Half Size",
  "5: Locate Fish",
  "6: Switch to Basic Functions"
]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
  """
  Input:  state - a dictionary containing the state values of the application
  Returns: a list of strings, each element represets a line in the interface
  """
  menuString = ["Welcome to CMPT 120 Image Processer!"]
  menuString.append("") # an empty line
  menuString.append("Choose the following options:")
  menuString.append("") # an empty line
  menuString += system
  menuString.append("") # an empty line

  # build the list differently depending on the mode attribute
  if state["mode"] == "basic":
    menuString.append("--Basic Mode--")
    menuString += basic
    menuString.append("")
    menuString.append("Enter your choice (Q/O/S/R or 1-7...)")
  elif state["mode"] == "advanced":
    menuString.append("--Advanced Mode--")
    menuString += advanced
    menuString.append("")
    menuString.append("Enter your choice (Q/O/S/R or 1-6...)")
  else:
    menuString.append("Error: Unknown mode!")

  return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
  """
  Input:  state - a dictionary containing the state values of the application
          img - the 2d array of RGB values to be operated on
  Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
  """
  userInput = state["lastUserInput"].upper()
  # handle the system functionalities
  if userInput.isalpha(): # check if the input is an alphabet
    print("Log: Doing system functionalities " + userInput)

    if userInput == "Q": # this case actually won't happen, it's here as an example
      print("Log: Quitting...\n")

    elif userInput == "O":
      print("Log: Opening an Image...\n")
      tkinter.Tk().withdraw()
      openFilename = tkinter.filedialog.askopenfilename()

      # lastOpenFilename dictionary key will store the file we just opened
      # this will be used later when user wants to reload the image back to its original
      state["lastOpenFilename"] = openFilename
      
      # assigning current image to become the image the user opened
      img = cmpt120imageProjHelper.getImage(openFilename) 

      # To get the file name of the image for the caption, I split the openFilename text into a 
      # list whenever there was a "/", because the file name was located at the end of the 
      # openFilename text, right after the last "/", so I just grabbed the last element
      captionTitle = openFilename.split("/")[-1]

      # displays the interface (the image, the title, and the options)
      cmpt120imageProjHelper.showInterface(img, captionTitle, generateMenu(state))

    elif userInput == "S":
      print("Log: Saving Image...\n")

      # getting the user to save current image with a name of their choice
      tkinter.Tk().withdraw()
      saveFilename = tkinter.filedialog.asksaveasfilename()
      cmpt120imageProjHelper.saveImage(img, saveFilename)

      # we saved the original image file into state["lastOpenFilename"] when the user 
      # first opened the image, so we can use that here to reassign the caption title
      openFilename = state["lastOpenFilename"]
      captionTitle = openFilename.split("/")[-1]
      cmpt120imageProjHelper.showInterface(img, captionTitle, generateMenu(state))

    elif userInput == "R":
      print("Log: Reloading Original Image...\n")

      # we saved the original image file into state["lastOpenFilename"] when the user 
      # first opened the image, so we can use that here now to reload the image back to original
      openFilename = state["lastOpenFilename"]
      img = cmpt120imageProjHelper.getImage(openFilename) 

      captionTitle = openFilename.split("/")[-1]
      cmpt120imageProjHelper.showInterface(img, captionTitle, generateMenu(state))

    else: # unrecognized user input
        print("ERROR: Unrecognized user input: " + userInput + "\n")

  elif userInput.isdigit(): # has to be a digit for manipulation options
    print("Log: Doing manipulation functionalities " + userInput)
    if state["mode"] == "basic":

      # This is to ensure that the "Log: Performing " statement only occurs when the 
      # input number is a valid choice
      if int(userInput)-1 in range(len(basic)):

        # States which basic manipulation is being applied based off user input
        print("Log: Performing " + basic[int(userInput)-1] + "\n")

      else: 
        print("ERROR: Unrecognized user input: " + userInput + "\n")

      if userInput == "1":
        # Calls the applyRedFilter function from module, puts red filter on our image
        img = cmpt120imageManip.applyRedFilter(img)

        # Displays filtered image with interface
        cmpt120imageProjHelper.showInterface(img, "Apply Red Filter", generateMenu(state))

      elif userInput == "2":
        img = cmpt120imageManip.applyGreenFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Green Filter", generateMenu(state))

      elif userInput == "3": 
        img = cmpt120imageManip.applyBlueFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Blue Filter", generateMenu(state))

      elif userInput == "4": 
        img = cmpt120imageManip.applySepiaFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Sepia Filter", generateMenu(state))  

      elif userInput == "5":
        img = cmpt120imageManip.applyWarmFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Warm Filter", generateMenu(state))

      elif userInput == "6":
        img = cmpt120imageManip.applyColdFilter(img)
        cmpt120imageProjHelper.showInterface(img, "Apply Cold Filter", generateMenu(state))
            
      elif userInput == "7":
        state["mode"] = "advanced"

        # For when user switches modes, to ensure the interface changes too
        openFilename = state["lastOpenFilename"]
        captionTitle = openFilename.split("/")[-1]        
        cmpt120imageProjHelper.showInterface(img, captionTitle, generateMenu(state))
      
    elif state["mode"] == "advanced":

      # This is to ensure that the "Log: Performing " statement only occurs when the 
      # input number is a valid choice
      if int(userInput)-1 in range(len(advanced)):

        # States which advanced manipulation is being applied based off user input
        print("Log: Performing " + advanced[int(userInput)-1] + "\n")

      else: 
        print("ERROR: Unrecognized user input: " + userInput + "\n")

      if userInput == "1":

        # Calls the rotateLeft function from module, rotates our image left
        img = cmpt120imageManip.rotateLeft(img)
        
        # Displays manipulated image with interface
        cmpt120imageProjHelper.showInterface(img, "Rotate Left", generateMenu(state))

      elif userInput == "2":
        img = cmpt120imageManip.rotateRight(img)
        cmpt120imageProjHelper.showInterface(img, "Rotate Right", generateMenu(state))
      
      elif userInput == "3":
        img = cmpt120imageManip.doubleSize(img)
        cmpt120imageProjHelper.showInterface(img, "Double Size", generateMenu(state))

      elif userInput == "4":
        img = cmpt120imageManip.halfSize(img)
        cmpt120imageProjHelper.showInterface(img, "Half Size", generateMenu(state))

      elif userInput == "5":
        img = cmpt120imageManip.locateFish(img)
        cmpt120imageProjHelper.showInterface(img, "Locate Fish", generateMenu(state))

      elif userInput == "6":
        state["mode"] = "basic"
        
        # For when user switches modes, to ensure the interface changes too
        openFilename = state["lastOpenFilename"]
        captionTitle = openFilename.split("/")[-1]
        cmpt120imageProjHelper.showInterface(img, captionTitle, generateMenu(state))

  return img

# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
  "mode": "basic",
  "lastOpenFilename": "",
  "lastSaveFilename": "",
  "lastUserInput": ""
}

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) 

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
  ### use the pygame event handling system ###
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      appStateValues["lastUserInput"] = pygame.key.name(event.key)
      # prepare to quit the loop if user inputs "q" or "Q"
      if appStateValues["lastUserInput"].upper() == "Q":
        keepRunning = False
      # otherwise let the helper function handle the input
      else:
        currentImg = handleUserInput(appStateValues, currentImg)
    elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
      keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")