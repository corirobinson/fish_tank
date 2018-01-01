

def setup():
    size(1000,1000)
    background(24, 163, 222)
    fishcirlcle=(500,500,100,50)
    fishtri=(540,500,600,460,600,540)  
    fish(100,200)
    fish(200,300)
    for i in range(50):
        fish(random (0,1000),random(0,1000))

def fish(x,y):
      noStroke()
      fill(random(255),random(255),random(255))
      ellipse(x,y,100,40)
      triangle(x+50,y,x+50+15,y-30,x+50+15,y+30)
