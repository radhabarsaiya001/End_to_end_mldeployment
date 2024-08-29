import sys
import logging

def error_msg_detail(error, error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "The error occured in script [{0}], line number [{1}] and the error is [{2}]]".format(
    file_name,exec_tb.tb_lineno, str(error))
    # print("*********************************")
    # print(error_message)
    return error_message
    

class Custom_Exception(Exception):  
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ =="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("It's the first error append in logging which is Zero Divion error>>>>>>>>>>>>")
        raise Custom_Exception(e,sys)
    
    


