from tkinter import Tk,BOTH,Canvas

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.title = self.__root.title()
        self.canvas = Canvas()
        self.canvas.pack()
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