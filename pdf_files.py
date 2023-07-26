from PyPDF2 import PdfReader
from file_managment import file_managment 
import re

class pdf_files(file_managment):

    def __init__(self):
        print("My constructor")


    def read_pdf(self,path,pdf_name,mode):
        pdf_object = self.read_file(path,pdf_name,mode)

        # creating a pdf reader object
        pdf_reader = PdfReader(pdf_object)

        return pdf_reader


    def get_text_by_page(self,path,pdf_name,page_index,mode):
        doc_pdf = self.read_pdf(path,pdf_name,mode)

        # printing number of pages in pdf file
        pdf_content = doc_pdf.pages[page_index]
        
        print(pdf_content.extract_text())

    def get_text_all_pages(self,path,pdf_name,mode):
        doc_pdf = self.read_pdf(path,pdf_name,mode)

        page_list = list()
        number_page = len(doc_pdf.pages)
        print("number of page:", number_page)

        # printing number of pages in pdf file
        for page in doc_pdf.pages:
            page_list.append(page.extract_text())

        print(page_list)


    def check_pdf_names(self,path,directory_name):
        pdf_list = self.list_folder_files(path,directory_name)

        #pdf_nombre : date-email-version.pdf
        #tienen fecha valida

        for pdf_file in pdf_list:
            regex_pdf_rule = re.search(".pdf", pdf_file)
            if regex_pdf_rule:
                print(pdf_file," Yes, it is a PDF")
                list_name = re.split("-",pdf_file)
                if len(list_name) == 3 : 
                    print(pdf_file," Yes, it has -")
                    #"10/03/12-jose17@hotmail.com-v3.pdf
                    regex_rule_dates = re.search("^[0-9]{2}/[0-9]{2}/[0-9]{2}[-]", list_name[0])
                    if regex_rule_dates :
                        print(pdf_file," Yes, it has it")
                    else: 
                        print(pdf_file," No, it has it")
                    
                    regex_rule_email = re.search("^[a-zA-Z0-9]+[@]{1}[a-zA-Z0-9]*[.com]", list_name[1])
                    if regex_rule_email :
                        print(pdf_file," Yes, it has it")
                    else: 
                        print(pdf_file," No, it has it")

                    regex_rule_version = re.search("^v{1}[0-9]+", list_name[2])
                    if regex_rule_version :
                        print(pdf_file," Yes, it has it")
                    else: 
                        print(pdf_file," No, it has it")
                else: 
                    print(pdf_file," NO, it has -")
            else:
                print(pdf_file," No, it is not a PDF")
                




 
if __name__ == "__main__":
    obj = pdf_files()
    #Coloca el pdf tu path
    path = ""
    #Coloca coloca tu pdf file name
    file_name = "pdf_test.pdf"
    #obj.get_text_all_pages(path,file_name,"rb")
    obj.get_text_by_page(path,file_name,0,"rb")
    #Coloca el pdf tu path
    #path = ""
    #Coloca coloca tu pdf file name
    #directory_name = "input_files"
    obj.check_pdf_names(path,directory_name)