import os
import shutil
import pathlib
from os import walk


class file_managment():

    def __init__(self):
        print("My constructor")



    def read_file(self,path,file_name,mode):
        #f = open(file_name, mode) 
        #Read a pdf use rb
        f = open(path + "/" + file_name, mode)
        #print(f.read())
        print("Done")

        return f


    def delete_file(self,path,file_name):
        os.remove(path + "/" + file_name)

        print("Delete it")

        return "delete it"

    def exist_file(self, path,file_name):
        status = False

        if os.path.exists(path + "/" + file_name):
            status = True
        else:
            status = False

        print("file status: ",status)

        return status

    #test with a txt
    def write_file(self,path,file_name,mode,content):

        f = self.read_file(path,file_name,mode)
        f.write(content)
        f.close()

        print("Complete")

    def create_folder(self,path,directory_name):
        # Path definition
        path = os.path.join(path, directory_name)
        os.chmod(path,0o777)
        # Create the directory
        #os.mkdir(path) 
        print("Directory '% s' created" % path) 
        
    def folder_access(self,path,directory_name):
        
        path = os.path.join(path, directory_name)
        os.chmod(path,0o777)
        
        print("Directory '% s' chmod" % path) 
        
        

    def delete_os_folder(self,path,directory_name):
        # Path
        path = os.path.join(path, directory_name) 
        
        #remove the path
        os.rmdir(path)
        print("% s has been removed successfully" % directory_name)

    #borrar folder y sus files adentro
    def delete_shutil_folder(self,path,directory_name):
        #path
        path = os.path.join(path, directory_name)
        # removing directory
        shutil.rmtree(path)
        print("% s has been removed successfully" % directory_name)


    def list_folder_files(self,path,directory_name):

        list_result = []

        dir_path = os.path.join(path, directory_name)
        # iterar en los folders
        for file_name in os.listdir(dir_path):
            #verificar si el actual path es un file
            if os.path.isfile(os.path.join(dir_path, file_name)):
                # add filename to list
                list_result.append(file_name)
                
        
        print("List of files", list_result)
        return list_result

    def list_walk_folder_files(self,path,directory_name):

        dir_path = os.path.join(path, directory_name)
        # list to store files name
        list_result = list()
        for (dir_path, dir_names, file_names) in walk(dir_path):
            print(file_names)

        print("List of files", list_result)


    def list_pathlib_folder_files(self,path,directory_name):

        # salvar el file
        list_files_result = []
        list_directory_result = list()

        # definir el path a consultar 
        path_directory = pathlib.Path(path + "/" + directory_name)

        # iterate directory
        for entry in path_directory.iterdir():
            # check if it a file
            if entry.is_file():
                list_files_result.append(entry)
            else:
                list_directory_result.append(entry)

        print("List of files", list_files_result)
        print("List of directories", list_directory_result)

        return list_files_result, list_directory_result

    def file_rename(self):
        pass


if __name__ == "__main__":
    obj = file_managment()
    #Coloca tu path
    #path = ""
    #Coloca el file_name 
    #file_name = ""
    #Coloca tu path
    path = ""
    #Coloca el file_directory
    directory_name = "input_files"
    #obj.read_file(path,file_name,"w")
    #obj.delete_file(path,file_name)
    #obj.exist_file(path,file_name)
    #obj.write_file(path,file_name,"a","second content in python avanzado")
    #obj.create_folder(path,directory_name)
    #obj.delete_os_folder(path,directory_name)
    #obj.delete_shutil_folder(path,directory_name)
    #obj.list_folder_files(path,directory_name)
    #obj.list_walk_folder_files(path,directory_name)
    #obj.list_pathlib_folder_files(path,directory_name)







    
    

    
            


    

    