import time
import sys
from psychopy import visual,event,core # import the bits of PsychoPy we'll need for this exercise

win = visual.Window([400,400],color="black", units='pix',checkTiming=False) #open a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) #create a Rectangle type object with certain parameters

#spinning!!!!
while True:
    square.draw()
    win.flip()
    square.ori +=6 #assuming 60 Hz refresh rate, so 6*60 ~360 degrees per second
    if event.getKeys('q'):
        break

win.close() #close the window -- don't need this if you're running this as a separate file
core.quit() #quit out of the program -- don't need this if you're running this as a separate file