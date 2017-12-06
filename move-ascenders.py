from robofab.interface.all.dialogs import AskYesNoCancel
from robofab.interface.all.dialogs import AskString

g = CurrentGlyph()
f = CurrentFont()


glyphsWithAscenders = ['b','d','f','h','k','l']

# targetAscender = 693
targetAscender = AskString("Please enter the ascender you would like:", "")
targetAscender = int(float(targetAscender))
currentAscender = f.info.ascender
moveAscenderBy = targetAscender - currentAscender

xHeightClearance = 50

def moveAscenders():
    yesNoQuestion = "This will move your ascender to " + str(targetAscender) + ". " + "Continue?"
    confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)
    print confirmScale
    if confirmScale == 1: 
        for g in f:
            g.prepareUndo()
            if g.name in glyphsWithAscenders:   
                g.selected = True
                for contour in g:
                    for seg in contour:
                        for point in seg:
                            if point.y > f.info.xHeight + xHeightClearance:
                                # print type(point.type), point.y
                                point.move((0, moveAscenderBy))
                                g.update()
                print "moved ascender of ", g.name, " by ", str(moveAscenderBy)
            g.performUndo()
        f.info.ascender = targetAscender

moveAscenders()