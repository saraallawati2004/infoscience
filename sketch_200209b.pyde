x = 0
y = 0
x2 = 0
y2 = 0

def setup():
    size(1000, 1000)
    background(255)
    textAlign(CENTER, CENTER)

def draw():
    print("")
    
def mouseClicked():
    global x2, y2, x, y
    x2 = x
    y2 = y
    x = mouseX
    y = mouseY
    r = random(10,100)
    myred = random(0,255)
    myblue = random(0,255)
    mygreen = random(0,255)
    fill (myred, mygreen, myblue)
    
    line(x2, y2, x, y)
    circle(x, y, r)
    fill (0)
    textSize(r/3)
    text("RICO", x, y)
    
    print(x, y)
    
    
