from psychopy import visual, event, core # import the bits of PsychoPy we'll need for this walkthrough

#open a window
win = visual.Window([600,600],color="grey", units='pix', checkTiming=False) 

## instructions
instruction_text = "Press the first letter of the circle's color."
instruction = visual.TextStim(win, text=instruction_text, pos=(0, -100))

#create a blue circle
# blue_circle = visual.Circle(win,lineColor="grey",fillColor="blue",size=[100,100])

# orange_circle = visual.Circle(win,lineColor="grey",fillColor="orange",size=[100,100])

circle = visual.Circle(win,lineColor="grey",fillColor="blue",size=[100,100])

color_list = ["blue", "orange", "purple", "red"]
#show the blue circle
#first, draw the blue circle to the back buffer of the window
#this means that the blue circle won't be displayed right away
# blue_circle.draw()
circle.draw()
#then "flip" the window to show what you just drew
win.flip()

# key_pressed = event.waitKeys(keyList=["b", "o"])
# if key_pressed:
#     print(key_pressed)
#     win.flip()

# core.wait(1.0)

# orange_circle.draw()
# win.flip()

# key_pressed = event.waitKeys(keyList=["b", "o"])
# if key_pressed:
#     print(key_pressed)
#     win.flip()

# win.flip()

for current_color in color_list:
    circle.color = current_color
    circle.draw()
    instruction.draw()
    win.flip()
    key_pressed = event.waitKeys(keyList=["b", "o", "p", "r"])
    if key_pressed:
        print(key_pressed)

    win.flip()
    core.wait(1.0)

#wait 2 seconds
core.wait(2.0)

win.close() #close the window
core.quit() #quit out of the program

