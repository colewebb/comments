import PythonFile
import GenericFile

class FileFactory:
    def __init__(self):
        pass

    def makeFile(self, filename):
        if filename.endswith(".py"):
            return PythonFile.PythonFile(filename)
        else:
            return GenericFile.GenericFile(filename)