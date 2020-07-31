import ntpath
import shutil
import os


def get_enclosing_folder(file_path: str):
    return file_path[:len(self.file_path) - len(ntpath.basename(file_path))]


class File:

    def __init__(self, file_path: str):
        self.file_name = ntpath.basename(file_path)  # file name extracted from the provided file path
        self.file_path = file_path  # file path
        self.enclosing_folder = get_enclosing_folder(self.file_path)  # enclosing folder extracted from the provided file path
        self.extension = self.file_name[self.file_name.find('.'):] # file extension extracted from the provided file path

    # opens file
    def open(self):
        os.startfile(self.file_path)  # simply opens the file using the os library

    # moves file to new destination
    def move(self, destination: str):
        shutil.move(self.file_path, destination)  # moves the file to a new destination using the shutil library
        self.file_path = f"{destination}\{self.file_name}"  # redefines self.file_path to the new path
        self.enclosing_folder

    # renames file and keeps the same enclosing folder but changes the path to accomodate the new file name
    def rename(self, new_name: str):
        new_path = self.enclosing_folder + new_name  # takes the enclosing folder and the new file name and constructs a new file path
        os.rename(self.file_path, new_path)  # renames the file with the newly constructed file path using the os library
        self.file_name = new_name  # redefines self.file_name to the new file name
        self.file_path = new_path  # redefines self.file_path to the newly constructed file path


class Document(File):

    def __init__(self, file_path: str):
        super().__init__(file_path)


class Video(File):

    def __init__(self, file_path: str):
        super().__init__(file_path)


class Picture(File):

    def __init__(self, file_path: str):
        super().__init__(file_path)
