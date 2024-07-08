import matplotlib.pyplot as plt

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    outcode0 = compute_outcode(x0, y0, xmin, ymin, xmax, ymax)
    outcode1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
    while True:
        if not (outcode0 | outcode1):
            return x0, y0, x1, y1
        elif outcode0 & outcode1:
            return None
        else:
            if outcode0:
                x, y, outcode = x0, y0, outcode0
            else:
                x, y, outcode = x1, y1, outcode1
            if outcode & TOP:
                x += (x1 - x0) * (ymax - y) / (y1 - y0)
                y = ymax
            elif outcode & BOTTOM:
                x += (x1 - x0) * (ymin - y) / (y1 - y0)
                y = ymin
            elif outcode & RIGHT:
                y += (y1 - y0) * (xmax - x) / (x1 - x0)
                x = xmax
            elif outcode & LEFT:
                y += (y1 - y0) * (xmin - x) / (x1 - x0)
                x = xmin
            if outcode == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0, xmin, ymin, xmax, ymax)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)

# def draw_line(x0, y0, x1, y1, color='k'):
#     plt.plot([x0, x1], [y0, y1], color=color)

def draw_line(x0, y0, x1, y1, color='k', linestyle='-'):
    plt.plot([x0, x1], [y0, y1], color=color, linestyle=linestyle)

def draw_rect(xmin, ymin, xmax, ymax):
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'r')

xmin, ymin, xmax, ymax = 1, 1, 4, 4
lines = [(0, 0, 5, 5), (2, 2, 3, 3), (0, 2, 5, 2), (2, 0, 2, 5), (0, 0, 5, 0), (0, 0, 0, 5), (5, 5, 0, 5), (5, 5, 5, 0)]

for line in lines:
    result = cohen_sutherland(*line, xmin, ymin, xmax, ymax)
    if result:
        draw_line(*result, color='g', linestyle='-')  # solid blue line
    draw_line(*line, color='k', linestyle=':')  # dotted black line
#         draw_line(*result, 'g')
#     draw_line(*line, 'k:')
draw_rect(xmin, ymin, xmax, ymax)
plt.show()
