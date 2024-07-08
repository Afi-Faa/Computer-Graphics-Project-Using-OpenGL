import turtle

# Define the bitmap for characters
characterBitmaps = {
    'A': [
        "01110",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001"
    ],
    'B': [
        "11110",
        "10001",
        "10001",
        "11110",
        "10001",
        "10001",
        "11110"
    ],
    'C': [
        "01110",
        "10001",
        "10000",
        "10000",
        "10000",
        "10001",
        "01110"
    ],
    'D': [
        "11110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11110"
    ]
}


def draw_bitmap_char(x, y, char, scale):
    if char not in characterBitmaps:
        print(f"Character '{char}' not supported!")
        return

    bitmap = characterBitmaps[char]
    for i in range(len(bitmap)):
        for j in range(len(bitmap[i])):
            if bitmap[i][j] == '1':
                turtle.penup()
                turtle.goto(x + j * scale, y - i * scale)
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(scale)
                    turtle.right(90)
                turtle.end_fill()


# Setup turtle
turtle.speed(0)
turtle.color("white", "black")
turtle.bgcolor("black")

draw_bitmap_char(-50, 50, 'C', 20)

turtle.hideturtle()
turtle.done()
