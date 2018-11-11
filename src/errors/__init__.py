from .GcErrorException import GcErrorException

class ErrorShowDoesNotExist(GcErrorException):
    def __init__(self, message=""):
        super().__init__(message)

    @staticmethod
    def flask_desc_code(args=None):
        return "Cette série n'existe pas.", 400

class ErrorSeasonDoesNotExist(GcErrorException):
    def __init__(self, message=""):
        super().__init__(message)

    @staticmethod
    def flask_desc_code(args=None):
        return "Cette saison n'existe pas.", 400

class ErrorEpisodeDoesNotExist(GcErrorException):
    def __init__(self, message=""):
        super().__init__(message)

    @staticmethod
    def flask_desc_code(args=None):
        return "Cet épisode n'existe pas.", 400

class ErrorUserDoesNotExist(GcErrorException):
    def __init__(self, message=""):
        super().__init__(message)

    @staticmethod
    def flask_desc_code(args=None):
        return "Cet utilisateur n'existe pas.", 400

class ErrorUserAlreadyExist(GcErrorException):
    def __init__(self, message=""):
        super().__init__(message)

    @staticmethod
    def flask_desc_code(args=None):
        return "Erreur, un utilisateur avec le meme login existe deja.", 400

class ErrorApiConnexionError(GcErrorException):
    def __init__(self, message=""):
        super().__init__(message)

    @staticmethod
    def flask_desc_code(args=None):
        return "Erreur de connexion à l'API.", 500

class ErrorDbConnexionError(GcErrorException):
    def __init__(self, message=""):
        super().__init__(message)

    @staticmethod
    def flask_desc_code(args=None):
        return "Erreur de connexion à la bdd.", 500