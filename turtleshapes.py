import turtle

num_pts = 20 # number of Sides
for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(100)

turtle.mainloop()
