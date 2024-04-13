def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    return (x, y, w, h)

def getCircle(x1, y1, x2, y2):
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2
    
    return (x + y) ** 0.5

def getSquare(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    side = max(abs(x1 - x2), abs(y1 - y2))
    return (x, y, side, side)

def getRightTriangle(x1, y1, x2, y2):
    points = [(x1, y1), (x1, y2), (x2, y2)]
    return points

def getEquilateralTriangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    side = max(abs(x1 - x2), abs(y1 - y2))
    points = [(x, y + side), ((x + x + side) // 2, y), (x + side, y + side)]
    return points  

def getRhombus(x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    points = [(x, y1), (x + width // 2, y), (x, y2), (x - width // 2, y)]
    return points