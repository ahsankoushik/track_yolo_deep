import math
import json


class Meter:
    prev = {}
    centers =  {}
    his = {}
    y_start = 0
    y_end = 0 
    fps = 0 
    real_world_distance = 0
    per_pixel_distance = 0
    def __init__(self) ->None or int:
        if __class__.per_pixel_distance == 0 :
            return -1
        __class__.prev = __class__.centers.copy()
    
    @classmethod
    def metrics(cls,y_start:int,y_end:int,fps:int,real_world_distance:int)->None:
        '''Initialize all the values needed for calculations'''
        cls.y_start = y_start
        cls.y_end = y_end
        cls.fps = fps
        cls.real_world_distance = real_world_distance
        cls.per_pixel_distance = real_world_distance/(y_end-y_start)

    def enter(self,id:int,x1:int,y1:int,x2:int,y2:int)->int:
        # print(__class__.prev)
        center = (int((x1+x2)/2),int((y1+y2)/2))
        __class__.centers[id] = center
        if len(__class__.prev) != 0:
            if id in __class__.prev.keys():
                distance = math.sqrt(((center[0]-__class__.prev[id][0])**2) +((center[1]-__class__.prev[id][1])**2))
                real_distance = distance*__class__.per_pixel_distance
                speed = round(real_distance*__class__.fps,2)
                self.history(id,speed)
                return speed
        return (-1)

    @classmethod        
    def history(cls,id:int,speed:float)->None:
        if id not in cls.his.keys():
            cls.his[id] = [speed]
        else:
            cls.his[id].append(speed)

    @classmethod
    def generalize(cls)->dict:
        '''Generalize or find the mean of speeds for all the cars'''
        avg = {}
        for i,j in cls.his.items():
            avg[i] = round(sum(j)/len(j),2)
        return avg

    @classmethod 
    def export_to_txt(cls)->None:
        '''Dumps generalized speed data to txt'''
        data = cls.generalize()
        with open("outputs/txt/output.txt","w") as f:
            f.write(str(data))

    @classmethod
    def export_to_json(cls)->None:
        '''Dumps generalized speed data to txt'''
        data = cls.generalize()
        json_data = json.dumps(data,indent=4)

        with open("outputs/json/output.json",'w') as f:
            f.write(json_data)


        

    
