f = CurrentFont()

sel = []

for g in f:
    for contour in g:
        for seg in contour:
            for point in seg:
                if point.y > f.info.ascender + 200:
                    if g.name not in sel:
                        sel.append(g.name)

print sel

f.selection = sel