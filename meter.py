import math

# real world distance in meter 
real_world_distance = 60  
xy_start = 380 
xy_end = 430
per_pixel_distance = real_world_distance/(xy_end-xy_start)
fps = 1920/63


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
        
    
