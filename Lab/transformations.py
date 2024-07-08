import matplotlib.pyplot as plt
import numpy as np
import math


def draw_rectangle(ax, x1, y1, x2, y2, color, label=None):
    width = x2 - x1
    height = y2 - y1
    rect = plt.Rectangle((x1, y1), width, height, fill=None, edgecolor=color, label=label)
    ax.add_patch(rect)


def rotate_point(x, y, angle):
    angle_rad = math.radians(angle)
    xr = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    yr = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return xr, yr


def main():
    # Initialize the plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 400)
    ax.invert_yaxis()  # To match the coordinate system used in graphics.h

    print("1. Translation\n2. Rotation\n3. Scaling\n")
    s = int(input("Selection: "))

    if s == 1:
        x1, y1 = 200, 150
        x2, y2 = 300, 250
        tx, ty = 50, 50
        print("Rectangle before translation")
        draw_rectangle(ax, x1, y1, x2, y2, color='blue', label='Before Translation')

        print("Rectangle after translation")
        draw_rectangle(ax, x1 + tx, y1 + ty, x2 + tx, y2 + ty, color='red', label='After Translation')

    elif s == 2:
        x1, y1 = 200, 200
        x2, y2 = 300, 300
        print("Rectangle with rotation")
        draw_rectangle(ax, x1, y1, x2, y2, color='blue', label='Before Rotation')

        a = float(input("Angle of rotation: "))

        corners = np.array([[x1, y1], [x2, y1], [x2, y2], [x1, y2]])
        new_corners = []
        for (x, y) in corners:
            # Rotate point around the origin
            xr, yr = rotate_point(x, y, a)
            new_corners.append([xr, yr])
        new_corners = np.array(new_corners)

        draw_rectangle(ax, new_corners[0][0], new_corners[0][1], new_corners[2][0], new_corners[2][1], color='green',
                       label='After Rotation')

    elif s == 3:
        x1, y1 = 30, 30
        x2, y2 = 70, 70
        sx, sy = 2, 2
        print("Before scaling")
        draw_rectangle(ax, x1, y1, x2, y2, color='blue', label='Before Scaling')

        print("After scaling")
        draw_rectangle(ax, x1 * sx, y1 * sy, x2 * sx, y2 * sy, color='green', label='After Scaling')

    else:
        print("Invalid Selection")
        return

    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
