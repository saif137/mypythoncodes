import pyglet
import time
from pyglet.window import Window, mouse, gl


platform = pyglet.window.get_platform()
# Get an instance of current display
display = platform.get_default_display()
screen = display.get_default_screen()


mygame = pyglet.window.Window(600, 710,
              resizable=False,  # Make sure it is not resizable
              caption="STACKS",  # Caption of window
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False  # For flicker-free animation
              )  # Calling base class constructor

# Background image use for game
bgimage = pyglet.resource.image('background.png')
playimage = pyglet.resource.image('play.png')
playpart=playimage.get_region(0,380,250,80)
playsprite = pyglet.sprite.Sprite(playpart, 180, 300)
playsprite.visible= True
quitimage = pyglet.resource.image('quit.png')
quitpart=quitimage.get_region(0,380,250,80)
quitsprite = pyglet.sprite.Sprite(quitpart, 180, 200)
quitsprite.visible= True
titleimage=pyglet.resource.image('title.png')
titlepart=titleimage.get_region(0,560,350,160)
titlesprite = pyglet.sprite.Sprite(titlepart, 140, 500)
titlesprite.visible=True



keyboard = pyglet.window.key.KeyStateHandler()
mygame.push_handlers(keyboard)


# Make sure that game approximately is placed as center of screen
# This will adjust for different resolution. Relative positioning
# Using resolution to center game window
mygame.set_location(screen.width // 2 - 200,screen.height//2 - 350)
lis=[]
bimage = pyglet.image.load("dots.png")
bpart=bimage.get_region(10,10,100,20)

lis.append(pyglet.sprite.Sprite(bpart, 20, 690))
lis.append(pyglet.sprite.Sprite(bpart, 20, 690))
lis[1].visible=False

overlabel = pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=48,
                             x=300, y=400,
                             anchor_x='center', anchor_y='center', color=(0, 255, 255, 255))


    
    



@mygame.event
def on_draw():
    
    mygame.clear()
    bgimage.blit(0,0)
    playsprite.draw()
    quitsprite.draw()
    titlesprite.draw()
    overlabel.draw()
    if playsprite.visible== False and quitsprite.visible== False and titlesprite.visible==False:
        for j in lis:
            j.draw()
        
       
    

@mygame.event
def on_mouse_press(x, y, button, modifiers):
    if button==mouse.LEFT:
        print( "Left button clicked on mouse at (" + str(x) + "," + str(y) + ")")
        if (x >=180 and x < 430) and (y >= 300 and y <= 380):
            print("play")
            playsprite.visible= False
            quitsprite.visible= False
            titlesprite.visible=False
            time.sleep(1)
        elif( x>=180 and x<430) and (y>= 200 and y<=280):
            print("Quit")
            
            
        
    
    
countx=[0,0]
county=[0,0]
flag= [True, True]
c = 0
score=0
i=1
#flag=True


def update(dt):
    global c
    global county
    global countx
    global score
    global i
    global flag

    if playsprite.visible== False and quitsprite.visible== False and titlesprite.visible==False:


        
    
        if c != 230:
            lis[0].x += 1
            lis[0].y -= 3
            c=c+1
        else:
           
            
            
            lis[1].visible=True   
            if not keyboard[pyglet.window.key.S]:
               
                if countx[i]!=230:
                    lis[i].x += 2
                    countx[i]+=1
                if county[i]!=230:
                    lis[i].y -= 3
                    county[i]+=1
                    if lis[i].y==0:
                        overlabel.text="Game Over"
                        
               
            else:
                if flag[i] == True:
                    
                    countx[i]=230
                    county[i]=230
                    if lis[i].x >(lis[i-1].x +lis[i-1].width) or (lis[i].x +lis[1-1].width)<lis[i].x:
                        county[i]=0
                        overlabel.text="Game Over"
                        
                            
                    else:
                        
                            
                        lis[i].y = lis[i-1].height
                        
                        if lis[i].x <lis[i-1].x and (lis[i].x + lis[i].width) > lis[i-1].x:
                            tmp = (lis[i].x + lis[i].width) - lis[i - 1].x  # Width of new block
                            #if tmp <=0 :
                            #    tmp = 1 #Block cannot be of 0 width
                            
                            #print(str(i)+" width"+str(lis[i].width))
                           # print(str(i)+" - 1 x " + str(lis[i-1].x))
                           # print(str(i)+" x "+str(lis[i].x))
                           #if tmp < 1:
                            #tmp = 1
                            bpart2 = bimage.get_region(20, 20, tmp, 20)
                            lis[i] = pyglet.sprite.Sprite(bpart2, lis[i - 1].x, lis[i - 1].y + lis[i - 1].height)
                            if tmp <=1:
                                overlabel.text="Game Over"
                                print(score)
                            lis.append(pyglet.sprite.Sprite(bpart, 20, 690))
                            
                            countx.append(0)
                            county.append(0)
                           
                            score+=1
                            
                            flag[i]= False
                            flag.append(True)
                            i+=1
                            
                        elif lis[i].x> lis[i-1].x:
                            a=lis[i].x
                            tmp = lis[i].width-(lis[i].x - lis[i-1].x)
                            bpart2=bimage.get_region(10,10,tmp,20)
                            lis[i]= pyglet.sprite.Sprite(bpart2, a,20*i )
                            if tmp <=1:
                                overlabel.text="Game Over"
                                print(score)
                            lis.append(pyglet.sprite.Sprite(bpart2, 20, 690))
                            countx.append(0)
                            county.append(0)
                            score+=1
                            i+=1



                          
        
# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)

pyglet.app.run()







