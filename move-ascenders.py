from robofab.interface.all.dialogs import AskYesNoCancel

# g = CurrentGlyph()
f = CurrentFont()

glyphsWithAscenders = ['b','d','f','h','k','l']

targetAscender = 693
currentAscender = f.info.ascender
moveAscenderBy = targetAscender - currentAscender

xHeightClearance = 50

def moveAscenders():
    yesNoQuestion = "This will move your ascender to " + str(targetAscender) + ". " + "Continue?"
    confirmScale = AskYesNoCancel(yesNoQuestion ,title='Just Checking...', default=0)
    print confirmScale
    if confirmScale == 1: 
        for g in f:
            if g.name in glyphsWithAscenders:   
                for contour in g:
                    for seg in contour:
                        for point in seg:
                            if point.y > f.info.xHeight + xHeightClearance:
                                # print type(point.type), point.y
                                point.move((0, moveAscenderBy))
                                g.update()
                print "moved ascender of ", g.name, " by ", str(moveAscenderBy)

    f.info.ascender = targetAscender

moveAscenders()