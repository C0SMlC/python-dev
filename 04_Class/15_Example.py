class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream Already open")
        self.opened = True
        print("Stream opened")

    def Close(self):
        if not self.opened:
            raise InvalidOperationError("Stream Already Close")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from FIle")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from Network")


Read = NetworkStream()
Read.open()
