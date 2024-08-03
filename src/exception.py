import sys


def error_message_details(error, error_detail:sys):
    # we are only interested in the third information that we receve for exc_info function as it tell us about the specifics of the error -> which line number , which file, message  etc..
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message= 'Error has occured in python script name [{0}] at line number[{1}] error message [{3}]'.format(filename, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message