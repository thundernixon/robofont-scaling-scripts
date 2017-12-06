from robofab.interface.all.dialogs import AskYesNoCancel

f = CurrentFont()

currentHeight = f.info.ascender + abs(f.info.descender)

targetHeight = 1000

scaleBy = targetHeight / currentHeight

print scaleBy

# yesNoQuestion = "This will scale *all* your glyphs in " + f + " by " + str(scaleBy) + ". " + "Continue?"
# confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)

def roundPoints():
    for g in f:
        for contour in g:
            for seg in contour:
                for point in seg:
                    print point.x, point.y
                    # point.x = round(point.x)
                    # point.y = round(point.y)                    
roundPoints()