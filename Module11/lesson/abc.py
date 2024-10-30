from abc import ABC, abstractmethod

class FileStorage(ABC):
    @abstractmethod
    def upload_file(filename):
        pass

    @abstractmethod    
    def get_file_info(file_id):
        pass

class Dropbox(FileStorage):
    def upload_file(filename):
        pass

    def get_file_info(file_id):
        pass 

class GoogleDrive(FileStorage):
    def upload_file(filename):
        pass

    def get_file_info(file_id):
        pass 