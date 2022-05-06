Rect(0,0,400,400,fill=gradient('firebrick','red',start='top'))
# Draw the head.
### Place Your Code Here ###
Circle(200,200,100,fill='black')
Circle(100,100,50,fill='black')
Circle(300,100,50,fill='black')
# Draw Mickey's mouth.
### (HINT: His mouth is composed of four lines, and three ovals.
#          The peachpuff and salmon ovals hide part of the black oval.)
### Place Your Code Here ###
Oval(170,190,70,120,fill='peachpuff')
Oval(230,190,70,120,fill='peachpuff')
Oval(200,260,160,80,fill='peachpuff')
Line(145,260,160,240,fill='peru',lineWidth=2)
Line(150,250,175,265,fill='peru',lineWidth=2)
Line(240,240,255,260,fill='peru',lineWidth=2)
Line(225,265,250,250,fill='peru',lineWidth=2)
Oval(200,270,50,50,fill='black')
Oval(200,245,80,50,fill='peachpuff')
Oval(200,285,40,20,fill='salmon')

# Draw Mickey's eyes and nose.
### Place Your Code Here ###
Oval(200,230,40,20,fill='black')
Oval(195,228,10,5,fill='white')
Oval(230,185,30,70,fill='white')
Oval(170,185,30,70,fill='white')
Oval(165,195,20,30,fill='black')
Oval(225,195,20,30,fill='black')
