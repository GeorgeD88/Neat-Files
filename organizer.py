from pathlib import Path
from files import File
import os 


subdirectories = {
    'Docs': ['.pdf','.rtf','.txt'],
    'Audio': ['.m4a','.m4b','.mp3'],
    'Vids': ['.mov','.avi','.mp4'],
    'Images': ['.jpg','.jpeg','.png']
}

to_organize = r"C:\Users\Georg\Downloads"  # path of the directory I would like to organize
os.chdir(to_organize)  # moves to the directory it's organizing


def classify(file_type: str):
    for category, suffixes in subdirectories.items():
        for suffix in suffixes:
            if suffix == file_type:
                return category
    return 'Misc'


for item in os.scandir():  # iterates through everything in the directory it's organizing
    if item.is_dir():  # skips code if the item is a directory
        continue
    file_path = Path(item)  # saves the path of the item
    file_type = file_path.suffix.lower()  # saves the file type of the item
    directory = classify(file_type)  # classifies the directory that the file should be under and saves it
    directory_path = Path(directory)  # Gets the path of the directory
    if directory_path.is_dir() is False:  # If the path isn't a directory, it makes one
        directory_path.mkdir()
    file_path.rename(directory_path.joinpath(file_path))  # renames the file path to a joined file path?? (not sure how this one works)
  
#def organize_directory():
#    for item in os.scandir():
#        if item.is_dir():
#            continue
#        file_path = Path(item)
#        file_type = file_path.suffix.lower()
#        directory = pick_directory(file_type)
#        directory_path = Path(directory)
#        if directory_path.is_dir() is False:
#            directory_path.mkdir()
#        file_path.rename(directory_path.joinpath(file_path))
#
