from graphics import Window,Line,Point


def main():
    win = Window(800,600)
    l = Line(Point(50,50),Point(450,450))
    win.draw_line(l,'blue')
    win.wait_to_close()


main()