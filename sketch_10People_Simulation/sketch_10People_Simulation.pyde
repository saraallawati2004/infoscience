# definition of variables
x = [300, 200, 100, 400, 500, 150, 50, 250, 350, 450]
y = [300, 200, 100, 400, 500, 150, 50, 250, 350, 450]

def setup():
    size(500, 500)
    #append the random numbers into the list x and y
    
def draw():
    global x, y
    background(255)
    strokeWeight(2)
    
    #create 1st individual
    for i in range(10):
        circle(x[i], y[i], 40)
        x[i] = x[i] + random(-10, 10)
        y[i] = y[i] + random(-10, 10)
        
        #boudary conditions
        if x[i]>500:
            x[i] = 500
        if x[i]<0:
            x[i] = 0
        if y[i]>500:
            y[i] = 500
        if y[i]<0:
            y[i] = 0
    
    delay(100)
