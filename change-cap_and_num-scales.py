import string 
from mojo.drawingTools import *
from robofab.interface.all.dialogs import AskString
from robofab.interface.all.dialogs import AskYesNoCancel

f = CurrentFont()

uppercase = []
numerals = ['zero','one','two','three','four','five','six','seven','eight','nine']

for letter in string.uppercase:
    uppercase += letter

targetCapHeight = AskString("Enter your target height for caps and numerals:", "", "Target Cap Height")

targetCapHeight = int(float(targetCapHeight.upper()))
currentCapHeight = f.info.capHeight

def getNumHeight(numeralToCheckHeight):
    for g in f:
        if g.name == numeralToCheckHeight:
            for counter in g:
                currentNumHeight = counter.points[0].y
                print "currentNumHeight is ", currentNumHeight
                return currentNumHeight

targetNumHeight = targetCapHeight
currentNumHeight = getNumHeight("seven")

def scaleNums():
    question = "Is your num height " + str(currentNumHeight) + "?" + " If not, please enter it:"
    customNumHeight = AskString(question, currentNumHeight, "Current Numeral Height")
    customNumHeight = int(float(customNumHeight.upper()))
    
    yesNoQuestion = "This will scale all your numerals to " + str(targetNumHeight) + ". " + "Continue?"
    confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)
    print confirmScale
    numScale = targetNumHeight / customNumHeight
    if confirmScale == 1:
        for g in f:
            
            if customNumHeight != targetNumHeight:
                g.prepareUndo()
                if g.name in numerals:
                    g.selected = True
                    print "scaled ", g.name, " to ", targetNumHeight
                    g.scale(numScale)
                    g.width = g.width * numScale
                    g.update()
                g.performUndo()

def scaleCaps():
    capScale = targetCapHeight / currentCapHeight
    print capScale
    if currentCapHeight != targetCapHeight:
        yesNoQuestion = "This will scale all your caps to " + str(targetCapHeight) + ". " + "Continue?"
        confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)
        print confirmScale
        
        if confirmScale == 1:
            newCapHeight = int(float(f.info.capHeight * capScale))
            f.info.capHeight = newCapHeight
            for g in f:
                g.prepareUndo()
                if g.name in uppercase:
                    g.selected = True
                    g.scale(capScale)
                    g.width = g.width * capScale
                    g.update()
                    print "scaled ", g.name, " to ", newCapHeight
                g.performUndo()

capScale = targetNumHeight / targetCapHeight
print int(float(f.info.capHeight * capScale))
###### cue scaling ######
scaleCaps()
scaleNums()

###### to do: scale punctuation





