import string 
from mojo.drawingTools import *
from robofab.interface.all.dialogs import AskString
from robofab.interface.all.dialogs import AskYesNoCancel

f = CurrentFont()
# print f
# print f.path
# print f.info.xHeight

glyphs = []
uppercase = []
numerals = ['zero','one','two','three','four','five','six','seven','eight','nine']

for letter in string.uppercase:
    uppercase += letter
    
# for numeral in string.digits:
#     numerals += numeral

# print numerals

targetCapHeight = AskString("Enter your target height for caps and numerals:", "", "Target Cap Height")

targetCapHeight = int(float(targetCapHeight.upper()))
# targetCapHeight = 650
currentCapHeight = f.info.capHeight
# capScale = targetCapHeight / currentCapHeight



# print capScale

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
    # print help(customNumHeight)
    customNumHeight = int(float(customNumHeight.upper()))
    
    yesNoQuestion = "This will scale all your numerals to " + str(targetNumHeight) + ". " + "Continue?"
    confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)
    print confirmScale
    numScale = targetNumHeight / customNumHeight
    if confirmScale == 1:
        for g in f:
            if customNumHeight != targetNumHeight:
                if g.name in numerals:
                    print "scaled ", g.name, " to ", targetNumHeight
                    g.scale(numScale)
                    g.width = g.width * numScale
                    g.update()

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
                if g.name in uppercase:
                    g.scale(capScale)
                    g.width = g.width * capScale
                    g.update()
                    print "scaled ", g.name, " to ", newCapHeight
            

capScale = targetNumHeight / targetCapHeight
print int(float(f.info.capHeight * capScale))
###### cue scaling ######
scaleCaps()
scaleNums()

###### to do: scale punctuation





