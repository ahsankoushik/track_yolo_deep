import math



per_pixel_distance = 0

y_start = 0 
y_end = 0 
fps = 0
real_world_distance=0
def metrics(y1:int,y2:int,f:int,real_distance:int):
    '''Initialize all the values to metrics'''
    y_start = y1
    y_end = y2
    real_world_distance = real_distance
    fps = f
    per_pixel_distance = real_world_distance/(y_end-y_start)



class Meter:
    prev = {}
    centers =  {}
    
    def __init__(self):
        __class__.prev = __class__.centers.copy()
        

    def enter(self,id:int,x1:int,y1:int,x2:int,y2:int):
        # print(__class__.prev)
        center = (int((x1+x2)/2),int((y1+y2)/2))
        __class__.centers[id] = center
        if len(__class__.prev) != 0:
            if id in __class__.prev.keys():
                distance = math.sqrt(((center[0]-__class__.prev[id][0])**2) +((center[1]-__class__.prev[id][1])**2))
                real_distance = distance*per_pixel_distance

                return round(real_distance*fps,2)
        return (-1)
        
    
