class Point:
    x: int
    y: int


class Rect:
    x: int
    y: int
    width: int
    height: int


pt = Point()
rect = Rect()

pt.x = 3
pt.y = 13

rect.x = 2
rect.y = 2
rect.width = 10
rect.height = 10


def in_rectangle(point, rectangle):
    if (point.x < rectangle.x or point.y < rectangle.y) or (
            point.x > (rectangle.x + rectangle.width) or point.y > (rectangle.y + rectangle.height)):
        return False
    else:
        return True


print(in_rectangle(pt, rect))

pt1 = Point()
pt2 = Point()
pt3 = Point()
pt4 = Point()

pt1.x = 0
pt1.y = 0

pt3.x = 2
pt3.y = 5

pt2.x = 5
pt2.y = 6

pt4.x = 2
pt4.y = 2

points_list_ = [pt1, pt2, pt3, pt4]
print(points_list_)


def get_rectangle(points_list):
    rectangle = Rect()

    points_list.sort(key=lambda elem: elem.x)
    min_x = points_list[0].x
    max_x = points_list[-1].x

    points_list.sort(key=lambda elem: elem.y)
    min_y = points_list[0].y
    max_y = points_list[-1].y

    rectangle.x = min_x
    rectangle.y = min_y
    rectangle.width = max_x - min_x
    rectangle.height = max_y - min_y

    return rectangle


bar = get_rectangle(points_list_)
print(bar.x, bar.y, bar.width, bar.height)
