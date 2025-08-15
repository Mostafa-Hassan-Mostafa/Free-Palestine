from turtle import *


#red triangle
color('red')
begin_fill()
lt(90)
fd(200)
rt(135)
fd(150)
rt(90)
fd(150)
end_fill()

#black rectangle
penup()
rt(135)
fd(210)
pendown()
rt(90)
color('black')
begin_fill()
fd(365)
rt(90)
fd(70)
rt(90)
fd(292)
rt(45)
fd(100)
end_fill()

#white rectangle
penup()
lt(180)
fd(100)
pendown()
color('white')
lt(45)
fd(227)
rt(90)
fd(70)

#green rectangle

color('green')
penup()
goto(68, 55)
pendown()
begin_fill()
lt(90)
fd(300)
rt(90)
fd(66.67)
rt(90)
fd(368)

end_fill()



# Add the text below the flag
penup()
goto(0, -100)
color("red")
write("#Free_Palestine", font=('Verdana', 15, 'bold'))

# Hide the turtle and keep the window open
hideturtle()
done()