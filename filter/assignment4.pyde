
def setup():
    size(400,400)
    global image1
    image1=loadImage("image2.jpg")
    image(image1,0,0,400,400)
    loadPixels()

def coloring(redAmount,blueAmount,greenAmount):
    for i in range(len(pixels)):
        pixels[i]= color(red(pixels[i])-redAmount,green(pixels[i])+greenAmount,blue(pixels[i])-blueAmount)
    updatePixels()

def threshold(area):
    for i in range(len(pixels)):
        if (red(pixels[i])+blue(pixels[i])+green(pixels[i]))/3>area:
            pixels[i]=color(250)
        elif (red(pixels[i])+blue(pixels[i])+green(pixels[i]))/3>(area/2):
            pixels[i]=color(200) 
        elif (red(pixels[i])+blue(pixels[i])+green(pixels[i]))/3>(area/3):
            pixels[i]=color(150)
        elif (red(pixels[i])+blue(pixels[i])+green(pixels[i]))/3>(area/4):
            pixels[i]=color(100)
        elif (red(pixels[i])+blue(pixels[i])+green(pixels[i]))/3>0:
            pixels[i]=color(50)
            
    updatePixels()
      
def keyPressed():
    if key=='1':     
        redTint=random(0,100)
        greenTint=random(0,100)
        blueTint=random(0,100)
        coloring(redTint,greenTint,blueTint)
    elif key=='2': 
        areaAmount=random(50,250)
        threshold(areaAmount)
    if key=='r':
        image1=loadImage("image2.jpg")
        image(image1,0,0,400,400)
        loadPixels()
    
def draw():        
    pass
    



        