def setup():
    size(1000, 1000)
    background(255, 255, 255)
    
    
    for c in range(500):
        centerX = random(100, 800)
        centerY = random(100, 800)
        CircleSize = 50
        
        # draw shadow
        noStroke()
        fill(15, 15, 15, 10)
        for i in range(30):
            circle(centerX, centerY, CircleSize - i*5)
        
        #draw circle
        stroke(30, 30, 30)
        fill(random(200, 255), random(50, 255), random(50, 255))
        circle(centerX - 25, centerY - 25, CircleSize)
   
    save("Programing 2020/CircleWihShadow")
        
