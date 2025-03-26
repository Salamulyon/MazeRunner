from tkinter import Tk,BOTH,Canvas

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point1: Point,point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self,canvas,fill_color):
        canvas.create_line(self.point1.x,self.point1.y,
                                self.point2.x,self.point2.y,
                                fill=fill_color,width=2)

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.title = self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root,bg='white',height=height,width=width)
        self.__canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_to_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self,line: Line,fill_color):
        line.draw(self.__canvas,fill_color=fill_color)


        