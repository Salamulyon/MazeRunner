from graphics import Window,Line,Point
from cell import Cell


def main():
    win = Window(800,800)
    # l = Line(Point(50,50),Point(450,450))
    # win.draw_line(l,'blue')
    c1 = Cell(50, 50, 100, 100,win)
    c1.has_left_wall = False
    c1.draw()

    c2 = Cell(125, 125, 200, 200,win)
    c2.has_right_wall = False
    c2.draw()

    c3 = Cell(225, 225, 250, 250,win)
    c3.has_bottom_wall = False
    c3.draw()

    c4 = Cell(300, 300, 500, 500,win)
    c4.has_top_wall = False
    c4.draw()

    c4.draw_move(c3)
    win.wait_to_close()


main()