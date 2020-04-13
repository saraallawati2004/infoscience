c = 0
f = 0

def setup():
    global c, f
    for c in range(0, 101, 1):
        print (c), ("C are"), (f), ("F")
        f = 1.8*c + 32
        
delay(100)
    
