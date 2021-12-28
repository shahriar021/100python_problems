class MyError(Exception):
    """My own exception class

    Attribute:
        msg -- explanation of the error"""

    def __init__(self,msg):
        self.msg=msg

error = MyError("something wrong")        