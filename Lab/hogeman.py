import matplotlib.pyplot as plt

def clip_polygon(polygon, edge):
    def inside(p):
        return (edge == 'LEFT' and p[0] >= xmin) or \
               (edge == 'RIGHT' and p[0] <= xmax) or \
               (edge == 'BOTTOM' and p[1] >= ymin) or \
               (edge == 'TOP' and p[1] <= ymax)

    def intersection(p1, p2):
        if edge in ('LEFT', 'RIGHT'):
            x = xmin if edge == 'LEFT' else xmax
            y = p1[1] + (p2[1] - p1[1]) * (x - p1[0]) / (p2[0] - p1[0])
        else:
            y = ymin if edge == 'BOTTOM' else ymax
            x = p1[0] + (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1])
        return (x, y)

    output = []
    s = polygon[-1]
    for p in polygon:
        if inside(p):
            if not inside(s):
                output.append(intersection(s, p))
            output.append(p)
        elif inside(s):
            output.append(intersection(s, p))
        s = p
    return output

xmin, ymin, xmax, ymax = 1, 1, 4, 4
polygon = [(0.5, 0.5), (2, 2.5), (3.5, 0.5), (3.5, 3.5), (0.5, 3.5)]

for edge in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP']:
    polygon = clip_polygon(polygon, edge)

x, y = zip(*polygon)
plt.fill(x, y, 'g', alpha=0.5)

rect_x = [xmin, xmax, xmax, xmin, xmin]
rect_y = [ymin, ymin, ymax, ymax, ymin]
plt.plot(rect_x, rect_y, 'r')

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
