import pickle
import json
import numpy as np
import config

class AdultAutism():
    def __init__(self,A1, A2, A3, A4, A5, A6, A7, A8, A9,A10,age,gender,jaundice,autism):
        self.A1       = A1
        self.A2       = A2
        self.A3       = A3
        self.A4       = A4
        self.A5       = A5
        self.A6       = A6
        self.A7       = A7
        self.A8       = A8
        self.A9       = A9
        self.A10      = A10
        self.age      = age
        self.jaundice = jaundice
        self.gender   = gender 
        self.autism   = autism
        
    def load_model(self):
        # we are reading model and json file"
        with open(config.ADULT_MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file)
        with open(config.ADULT_JOSN_FILE_PATH,"r") as file:
            self.json_data = json.load(file)
      
        
    def get_adultautism(self):
        self.load_model() 
        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.gender
        test_array[1] = self.autism
        test_array[2] = self.jaundice
        test_array[3] = self.A1
        test_array[4] = self.A2
        test_array[5] = self.A3
        test_array[6] = self.A4
        test_array[7] = self.A5
        test_array[8] = self.A6
        test_array[9] = self.A7
        test_array[10] = self.A8
        test_array[11] = self.A9
        test_array[12] = self.A10      
        test_array[13] = self.age    
        autism = self.model.predict([test_array])
        return autism


    
class ToddlerAutism():
    def __init__(self,A1, A2, A3, A4, A5, A6, A7, A8, A9,A10,age,gender,Jaundice,autism):
        self.A1       = A1
        self.A2       = A2
        self.A3       = A3
        self.A4       = A4
        self.A5       = A5
        self.A6       = A6
        self.A7       = A7
        self.A8       = A8
        self.A9       = A9
        self.A10      = A10
        self.age      = age
        self.Jaundice = Jaundice
        self.gender   = gender 
        self.autism   = autism
        
    def load_model(self):
        # we are reading model and json file"
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file)
        with open(config.JOSN_FILE_PATH,"r") as file:
            self.json_data = json.load(file)
      
        
    def get_toddlerautism(self):
        self.load_model() 
        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.gender
        test_array[1] = self.autism
        test_array[2] = self.Jaundice
        test_array[3] = self.A1
        test_array[4] = self.A2
        test_array[5] = self.A3
        test_array[6] = self.A4
        test_array[7] = self.A5
        test_array[8] = self.A6
        test_array[9] = self.A7
        test_array[10] = self.A8
        test_array[11] = self.A9
        test_array[12] = self.A10      
        test_array[13] = self.age    
        autism = self.model.predict([test_array])
        return autism


    







