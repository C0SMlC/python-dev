#  FEW PROBLEMS WITH BELOW EXAMPLE
# WE CAN CREATE AN INSTANCE OF STREM CLASS WHICH CAN STILL ACCESS READ AND CLOSE ATTRIBUTES
# BECAUSE WHICH WE DONT KNOW FROM WHERE WE ARE READING THE DATA
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    @abstractmethod
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

    @abstractmethod  # AND WITH THIS KEYWORD NOW EVERY CLASS NOW MUST HAVE READ METHOD
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from FIle")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from Network")


#stream = Stream()
