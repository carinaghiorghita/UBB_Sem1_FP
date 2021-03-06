
class StudentException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class AssigmentException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class LengthError(AssigmentException):
    def __init__(self,msg):
        super().__init__(msg)

class NoID_S(StudentException):
    def __init__(self,msg):
        super().__init__(msg)

class NameError(StudentException):
    def __init__(self,msg):
        super().__init__(msg)

class GroupError(StudentException):
    def __init__(self,msg):
        super().__init__(msg)

class DuplicateId(StudentException):
    def __init__(self,msg):
        super().__init__(msg)

class NoID_A(AssigmentException):
    def __init__(self,msg):
        super().__init__(msg)

class ValidationError(StudentException):
    def __init__(self,msg):
        super().__init__(msg)

class AgainError(StudentException):
    def __init__(self,msg):
        super().__init__(msg)

class GradeException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class NoID_G(GradeException):
    def __init__(self,msg):
        super().__init__(msg)

class GradeError(GradeException):
    def __init__(self,msg):
        super().__init__(msg)