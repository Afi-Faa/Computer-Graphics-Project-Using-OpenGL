import turtle


def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def draw_character_outline(x, y, ch, scale):
    if ch == 'A':
        draw_line(x, y, x + 10 * scale, y + 20 * scale)
        draw_line(x + 10 * scale, y + 20 * scale, x + 20 * scale, y)
        draw_line(x + 5 * scale, y + 10 * scale, x + 15 * scale, y + 10 * scale)
    elif ch == 'B':
        draw_line(x, y, x, y + 20 * scale)
        draw_line(x, y + 20 * scale, x + 10 * scale, y + 20 * scale)
        draw_line(x + 10 * scale, y + 20 * scale, x + 15 * scale, y + 15 * scale)
        draw_line(x + 15 * scale, y + 15 * scale, x + 15 * scale, y + 10 * scale)
        draw_line(x + 15 * scale, y + 10 * scale, x + 10 * scale, y + 5 * scale)
        draw_line(x + 10 * scale, y + 5 * scale, x, y + 5 * scale)
    elif ch == 'C':
        draw_line(x + 15 * scale, y, x, y)
        draw_line(x, y, x, y + 20 * scale)
        draw_line(x, y + 20 * scale, x + 15 * scale, y + 20 * scale)
    elif ch == 'D':
        draw_line(x, y, x, y + 20 * scale)
        draw_line(x, y, x + 15 * scale, y)
        draw_line(x, y + 20 * scale, x + 15 * scale, y + 20 * scale)
        draw_line(x + 15 * scale, y, x + 15 * scale, y + 20 * scale)
    elif ch == 'E':
        draw_line(x, y, x, y + 20 * scale)
        draw_line(x, y, x + 15 * scale, y)
        draw_line(x, y + 10 * scale, x + 10 * scale, y + 10 * scale)
        draw_line(x, y + 20 * scale, x + 15 * scale, y + 20 * scale)
    else:
        print(f"Character '{ch}' not supported!")


# Setup turtle
turtle.speed(0)
turtle.color("white")
turtle.bgcolor("black")
draw_character_outline(-50, 50, 'E', 10)
turtle.hideturtle()
turtle.done()
