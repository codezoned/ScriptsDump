class Error(Exception):
    # base class
    pass

class PaddingError(Error):
    def __init__(self, msg):
        self.msg = msg
        super(PaddingError, self).__init__(self.msg)

class MatrixRankError(Error):
    def __init__(self, msg):
        self.msg = msg
        super(MatrixRankError, self).__init__(self.msg)

class DivisionError(Error):
    def __init__(self, msg):
        self.msg = msg
        super(DivisionError, self).__init__(self.msg)
