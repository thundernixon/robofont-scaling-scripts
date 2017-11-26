import string 
from mojo.drawingTools import *

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

targetCapHeight = 650
currentCapHeight = f.info.capHeight
capScale = targetCapHeight / currentCapHeight



# print capScale

def getNumHeight(numeralToCheckHeight):
    for g in f:
        if g.name == numeralToCheckHeight:
            for counter in g:
                # THIS ONLY WORKS IF YOUR TARGET NUMERAL HAS ITS FIRST POINT AT THE TOP
                currentNumHeight = counter.points[0].y
                print "currentNumHeight is ", currentNumHeight
                return currentNumHeight

targetNumHeight = targetCapHeight
currentNumHeight = getNumHeight("seven")
numScale = targetNumHeight / currentNumHeight

            
    # if g.name in numerals:
    #     print "yo", g.name
    #     print "yo"
# print "A".width

# for contour in A:
#     print contour

def scaleNums():
    for g in f:
        if currentNumHeight != targetNumHeight:
            if g.name in numerals:
                print "scaled ", g.name, " to ", targetNumHeight
                g.scale(numScale)
                g.width = g.width * numScale
                g.update()

def scaleCaps():
    for g in f:
        if currentCapHeight != targetCapHeight:
            if g.name in uppercase:
                print "scaled ", g.name, " to ", targetCapHeight
                g.scale(capScale)
                g.width = g.width * capScale
                g.update()
            f.info.capHeight = f.info.capHeight * capScale

###### cue scaling ######
scaleCaps()
scaleNums()
    # if currentNumHeight != targetNumHeight:


# numeralScale = .91



