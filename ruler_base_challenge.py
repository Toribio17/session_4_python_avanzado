from spreadsheet_files import spreadsheet_files
import random 
import os


class ruler_method_base(spreadsheet_files):
    
    def __init__(self):
        print("My constructor")
        
    def chose_person(self,random_num):
        pass
        
        
    def ruler_game(self):
        
        low, high = 1,5
        max_guesses = 7
        num_guesses = 0
        
        secret_number = random.choice(range(low,high))
                
            

if __name__ == "__main__":
    obj = ruler_method_base()
    
    obj.ruler_game() 