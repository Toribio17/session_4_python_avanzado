from file_managment import file_managment
import pandas as pd 
import os

class spreadsheet_files(file_managment):
    
    def __init__(self):
        print("My constructor")
        
        
    def read_data_frame(self,path,file_name):
        
        df = pd.DataFrame()
        type_file = file_name.split(".")
        file_path = os.path.join(path,file_name)
        
        if type_file == "csv":
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        
        columns = df.head()
        print(columns)
        
        return df
    
    
    def drop_empty_values(self,df):
        
        df.dropna()
        #df.dropna(inplace = True)
        print(df)
        print("removed the null values")
        
        return df
    
    def full_empty_values_all(self,df):
        
        df.fillna(130, inplace = True)
        print(df)
        
        return df
    
    def full_empty_values_column(self,df,column):
        
        df[column].fillna(130, inplace = True)
        print(df)
        return df
    
    def mean_column(self,df,column):
        
        mean_column = df[column].mean()
        print("Mean: ",mean_column)
        
        return mean_column
    
    def median_column(self, df,column):
        
        median_column = df[column].median()
        print("Median: ",median_column)
        
        return median_column
    
    def get_columns_name(self,df,column):
        
        df_column = df.loc[:,[column]]
        
        return df_column
        
    

if __name__ == "__main__":
    obj = spreadsheet_files()
    path = os.environ['PATH_PROJECT'] + "input_files/"
    file_name = "informacion_alumnos.xlsx"
    column_name = "edad"
    df = obj.read_data_frame(path,file_name)
    #obj.drop_empty_values(df)
    #obj.full_empty_values_all(df)
    #obj.full_empty_values_column(df,column_name)
    #obj.mean_column(df,column_name)
    #obj.median_column(df,column_name)
    obj.get_columns_name(df,column_name)
    
    
    
    
    
    
    
    
    
    
    
        
        
        