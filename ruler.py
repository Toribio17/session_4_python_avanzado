from spreadsheet_files import spreadsheet_files
import random 
import os


class ruler_method(spreadsheet_files):
    
    def __init__(self):
        print("My constructor")
        
    def chose_person(self,random_num):
        
        path = os.environ['PATH_PROJECT'] + "input_files/"
        file_name = "informacion_alumnos.xlsx"
        df = self.read_data_frame(path,file_name)
        df = self.get_columns_name(df,"Nombre")
        
        people_list = df["Nombre"].to_list()
        
        return people_list[random_num]
        
        
    def ruler_game(self):
        
        low, high = 1,5
        max_guesses = 7
        num_guesses = 0
        
        secret_number = random.choice(range(low,high))
        
        while True:
            print("Chose a number between: ",low," and ",high)
            guess = int(input("\Guess a number: "))
            num_guesses = num_guesses + 1 
            
            if guess == secret_number:
                person_num = random.choice(range(1,32))
                person = self.chose_person(person_num)
                print("Congrats, you've chosen: ", person)
                break
            
            if num_guesses == max_guesses:
                print("Sorry, you have no more changes")
                break
            else:
                print("No correct, you have more changes")
                
            

if __name__ == "__main__":
    obj = ruler_method()
    
    obj.ruler_game()  
    