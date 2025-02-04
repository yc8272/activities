import time
import sys
from psychopy import visual,event,core # import the bits of PsychoPy we'll need for this exercise

win = visual.Window([400,400],color="black", units='pix',checkTiming=False) #open a window

# square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100]) #create a Rectangle type object with certain parameters
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square.setOri(0)

square.draw() #draw the square to the screen buffer

win.flip() #make the buffer visible, i.e., show what's been drawn to it

# 2. 
# core.wait(.5) #pause for half a second (i.e., 500 ms)
core.wait(1)

# 4. 
# color = ['blue', 'red']
# for i in range (6):
#     temp_clr = color[i % 2]
#     square.color = temp_clr
#     square.draw()
#     win.flip()
#     core.wait(1)
#     win.flip()
#     core.wait(0.05)

# 5.
# square.setOri(45)
# square.draw()
# win.flip()
# core.wait(1) 

# 6. 
# value = 0
# for i in range(8):
#     value += 45
#     square.setOri(value)
#     square.draw()
#     win.flip()
#     core.wait(0.125) 

# 7.
value = 0
continue_rotation = True
while(True):
    while(continue_rotation):
        value += 45
        square.setOri(value)
        square.draw()
        win.flip()
        
        keys = event.getKeys()
        if 's' in keys:
            continue_rotation = False
        core.wait(0.125)
    keys = event.getKeys()
    if 'r' in keys:
        continue_rotation = True



win.close() #close the window -- don't need this if you're running this as a separate file
core.quit() #quit out of the program -- don't need this if you're running this as a separate file