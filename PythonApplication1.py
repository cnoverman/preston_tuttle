#!/usr/bin/env python
# coding: utf-8

# In[7]:


import turtle as trtl
painter = trtl.Turtle()


# In[ ]:


#This code draws a flower using modules to alternate
#every other color
trtl.speed(0)
trtl.pensize(5)

#stem
trtl.color("green")
trtl.pensize(15)
trtl.goto(0,-150)
trtl.setheading(90)
trtl.forward(100)

#leaf
trtl.setheading(270)
trtl.circle(20,120,20)
trtl.setheading(90)
trtl.goto(0,-60)

#rest of stem
trtl.forward(60)
trtl.setheading(0)
#change pen
trtl.penup()
trtl.shape("circle")

########
#blocked out by Casey on 9/23/2020
##########
#trtl.trtlsize(2)

#draw flower
trtl.goto(20,180)
trtl.petals=0
#removed {} at the end of the while
while(trtl.petals<18):
    trtl.right(20)
    trtl.forward(30)
    trtl.color("violet")
    #removed {} at the end of the if statement and tested spacing.  (I will look up spacing on VR? later)
    # i don't know what .rem is supposed to do?  I can't find any documentation on what it's supposed to do.  
    #can you help me with what the idea of what this is supposed to evaluate?
    if(trtl.rem==0):
        trtl.color("blue")
        #does anything go at the end of the stamp?
    trtl.stamp
    trtl.petals=trtl.petals+1


# In[ ]:


wn = trtl.Screen()
wn.mainloop()


# In[ ]:





