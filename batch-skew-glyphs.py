# import the robofab dialog to ask user for a value
from robofab.interface.all.dialogs import AskString
# import the robofab dialog to confirm yes/no/cancel
from robofab.interface.all.dialogs import AskYesNoCancel

# grab current font
f = CurrentFont()

## get the glyphs you have selected as a list
glyphSelection = f.selection

# just to check that it's working
print glyphSelection

# Allow user to set a skew value
skewValue = AskString("Please enter the horizontal skew you want:", "")
# make the entered skew value a float (number with a decimal), because you need to for the skew function
skewValue = float(skewValue)

# get the font name for the upcoming dialog box
fontName = f.info.familyName + " " + f.info.styleName

# set up a skewing function
def skewSelection():
    # set up the question for a yes/no/cancel
    yesNoQuestion = "This will horizontall skew *all* your selected glyphs in " + fontName + " by " + str(skewValue) + " degrees. You should have a backup before any batch operation. " + "Continue?"
    # double check with the user before doing anything crazy
    confirmSkew = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)
    # if the user answers "yes", proceed
    if confirmSkew == 1:
        ## loop through font
        for g in f:
            # set up "undo" for every glyph changed
            g.prepareUndo()
            ## compare each glyph name to list of selected glyph names, and only edit if they are in the list
            if g.name in glyphSelection:
                # skew every selected glyph with the value the user has entered
                g.skew(skewValue)
            # undo, if the user asks to in the font view while glyphs are selected
            g.performUndo()

# cue the skewing function
skewSelection()