class ArgumentError(Exception):
    def __init__(self, message="Invalid argument provided"):
        self.message = message
        super().__init__(self.message)
