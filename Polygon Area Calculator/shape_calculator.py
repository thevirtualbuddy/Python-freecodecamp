class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    def set_width(self, width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        peri = (2 * self.width) + (2 * self.height)
        return peri
    def get_diagonal(self):
        dia = (self.width ** 2 + self.height ** 2) ** .5
        return dia
    '''
    def get_picture(self):
        if self.width>50 or self.height>50:
            return f'Too big for picture.'
        else:
            line_1 = "*" * self.width
            pic = ""
            for i in range(self.height):
                if i<self.height-1:
                    pic += line_1 + "\n"
                else:
                    pic += line_1
            return pic
    '''
    def get_picture(self):
      if self.width > 50 or self.height > 50:
        return("Too big for picture.")
      else:
        return( ( ("*" * self.width)+ "\n" ) * self.height)  
    
    def get_amount_inside(self, shape):
        areaGuest = shape.get_area()
        areaHome = self.get_area()
        i = 0
        while areaHome>=areaGuest:
            areaHome = areaHome-areaGuest
            i=i+1
        return i
            
    

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.width = side
    Rectangle.height = side

  def set_side(self, value):
    Rectangle.set_width(self, value)
    Rectangle.set_height(self, value)

  def __str__(self):
    return(("Square(side={0})").format(self.width) )
