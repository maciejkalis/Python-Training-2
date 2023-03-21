class Result:

    def __init__(self, message, value=None):
        self.isSuccess = None
        self.message = message
        self.value = value

    def is_ok(self):
        return self.isSuccess


class Ok(Result):

    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = True

    def __str__(self):
        return self.message + " " + str(self.value)


class Error(Result):

    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = False

    def __str__(self):
        return self.message + " " + str(self.value)
