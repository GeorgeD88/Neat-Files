import ntpath
import os


class File:

    def __init__(self, file_path: str):
        self.file_name = ntpath.basename(file_path)  # file name extracted from the provided file path
        self.file_path = file_path  # file path
        self.extension = self.file_name[self.file_name.find('.'):] # file extension extracted from the provided file path(.png, .pdf, etc.)


class Document(File):

    def __init__(self, file_path: str):
        super().__init__(file_path)


class Video(File):

    def __init__(self, file_path: str):
        super().__init__(file_path)
    
    def watch(self):
        os.startfile(self.file_path)
