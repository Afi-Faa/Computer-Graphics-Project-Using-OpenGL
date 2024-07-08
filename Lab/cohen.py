import matplotlib.pyplot as plt

INSIDE, LEFT, RIGHT, LOWER, UPPER = 0, 1, 2, 4, 8

def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= LOWER
    elif y > ymax:
        code |= UPPER
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
            x = y = 0
            if outcode0:
                outcode_out = outcode0
            else:
                outcode_out = outcode1
            if outcode_out & UPPER:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif outcode_out & LOWER:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif outcode_out & RIGHT:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif outcode_out & LEFT:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin
            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0, xmin, ymin, xmax, ymax)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)

def draw_line(x0, y0, x1, y1, color='k', linestyle='-'):
    plt.plot([x0, x1], [y0, y1], color=color, linestyle=linestyle)

def draw_rect(xmin, ymin, xmax, ymax):
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'r')


xmin, ymin, xmax, ymax = 1, 1, 4, 4
lines = [(0, 0, 5, 5), (2, 2, 3, 3), (0, 2, 5, 2), (2, 0, 2, 5), (0, 0, 5, 0), (0, 0, 0, 5), (5, 5, 0, 5), (5, 5, 5, 0)]

for line in lines:
    result = cohen_sutherland(*line, xmin, ymin, xmax, ymax)
    if result:
        draw_line(*result, color='g', linestyle='-')  # solid green line
    draw_line(*line, color='k', linestyle=':')  # dotted black line

draw_rect(xmin, ymin, xmax, ymax)
plt.show()
