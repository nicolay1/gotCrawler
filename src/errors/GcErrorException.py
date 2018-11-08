class GcErrorException(Exception):
    def __init__(self, message=""):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)
    
    @staticmethod
    def flask_desc_code(args=None):
        """
            Provide to Flask Error Handler a description and a code for the error
        """
        raise NotImplementedError
