from graphics import Line,Point

class Cell:
    def __init__(self,x1,y1,x2,y2,win):
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    
    def draw(self):
        if self.has_top_wall:
            line= Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line= Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            self._win.draw_line(line)
        if self.has_left_wall:
            line= Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line= Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            self._win.draw_line(line)
    
    def draw_move(self,to_cell,undo=False):
        if not undo:
            color = 'red'
        else:
            color = 'gray'
        own_center_x = (self._x1 + self._x2)//2
        own_center_y = (self._y1 + self._y2)//2
        other_cell_center_x = (to_cell._x1 + to_cell._x2)//2
        other_cell_center_y = (to_cell._y1 + to_cell._y2)//2

        line = Line(Point(own_center_x,own_center_y),
                    Point(other_cell_center_x,other_cell_center_y))
        self._win.draw_line(line,fill_color = color)

        


