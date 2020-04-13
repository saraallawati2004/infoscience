# definition of variables
x = [100,200]
y = [100,250]
h = [False, True] #false => infected 
wid = 220
Co = 0

def setup():
    size(500, 605)
    #append the random numbers into the list x and y
    for n in range(20):
        x.append(random(0, 500))
        y.append(random(0, 500))
        h.append(True) #All healthy
    
def distance (x1, x2, y1, y2):
    a = (x1 - x2)
    b = (y1 - y2)
    c = sqrt(a**2 + b**2)
    return c 
    
def draw():
    global x, y, wid1, wid2, Co, count
    background(255)
    strokeWeight(2)
    count = 0
    for i in range(len(h)):
        if h[i] == False:
            count += 1
            background(255)
            fill(50)
            text("Infected count:", 300, 540)
            text(count, 390, 540)
    

    
    Co += 1
    fill(50)
    text("simulation count:", 10, 520)
    text(Co, 110, 520)
    
    fill(255, 0, 0)
    count = count*10
    rect(30, 530, count, 30)
    
    fill(255)
    wid1 = wid - count
    rect(30, 570, wid1, 30)
    widCount = wid1/10
    fill(50)
    text("Healthy Count:", 300, 580)
    text(widCount, 390, 580)
    
    #create 1st individual
    for ind in range(len(x)):
        if h[ind] == True:
            fill(255) #healthy
        else:
            fill(255, 0, 0) #infected
               
        circle(x[ind], y[ind], 40)
        # Calculate the distance to each neighbor
        for nei in range(len(x)):
            if nei == ind:
                continue
            d = distance(x[ind], x[nei], y[ind], y[nei])
            if d < 40 and (h[nei] == False or h[ind] == False):
                #infectio happens
                h[ind] = False
                h[nei] = False

    for m in range(len(x)):
        x[m] = x[m] + random(-20, 20)
        y[m] = y[m] + random(-20, 20)
        
        #boudary conditions
        if x[m]>500: x[m] = 500
        if x[m]<0: x[m] = 0
        if y[m]>500: y[m] = 500
        if y[m]<0: y[m] = 0
    
    
    delay(50)
