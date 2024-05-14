import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

def main():

    order = int(input("Enter the level of recursion: "))

    window = turtle.Screen()
    window.bgcolor("pink")
    t = turtle.Turtle()
    t.speed(0)  

    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, 300)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()