from robofab.interface.all.dialogs import AskYesNoCancel

f = CurrentFont()

## get the glyphs you have selected as a list
glyphSelection = f.selection

# just to check that it's working
print glyphSelection

# yesNoQuestion = "This will scale *all* your glyphs in " + f + " by " + str(scaleBy) + ". " + "Continue?"
# confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)

def roundPoints():
    for g in f:
        g.prepareUndo()
        if g.name in glyphSelection:
            for contour in g:
                for seg in contour:
                    for point in seg:
                        print point.x, point.y
                        point.x = round(point.x)
                        point.y = round(point.y)    
                        print point.x, point.y
        g.performUndo()
                        
roundPoints()