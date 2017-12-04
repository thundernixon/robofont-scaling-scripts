from robofab.interface.all.dialogs import AskYesNoCancel

f = CurrentFont()

currentHeight = f.info.ascender + abs(f.info.descender)

targetHeight = 1000

scaleBy = targetHeight / currentHeight

print scaleBy

yesNoQuestion = "This will scale *all* your glyphs by " + str(scaleBy) + ". " + "Continue?"
confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)

def scaleGlyphsMetricsAndBlueValues():
    if confirmScale == 1:
        f.info.ascender = f.info.ascender * scaleBy
        f.info.descender = f.info.descender * scaleBy
        f.info.capHeight = f.info.capHeight * scaleBy
        f.info.xHeight = f.info.xHeight * scaleBy
        
        blues = f.info.postscriptBlueValues
        newBlues = [x * scaleBy for x in blues]
        f.info.postscriptBlueValues = newBlues
        for g in f:
            g.scale(scaleBy)
            g.width = g.width * scaleBy
            g.update()
