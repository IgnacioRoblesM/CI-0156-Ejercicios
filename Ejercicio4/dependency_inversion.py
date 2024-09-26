from abc import ABC, abstractmethod


# This class has a dependency on the DataSource class, which is an abstraction
class AudioPlayer:
    def __init__(self, data_source):
        self.data_source = data_source

    def play(self):
        return f"Playing {self.data_source.get_data()}"


# This is the abstraction
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


# These are the concrete implementations of the abstraction
class MP3(DataSource):
    def get_data(self):
        return "MP3 data"


class MP4(DataSource):
    def get_data(self):
        return "MP4 data"
