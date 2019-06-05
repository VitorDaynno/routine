class FileHelper:

    def __init__(self):
        self.file = None

    def open(self, file, mode):
        self.file = open(file, mode)

    def write(self, line):
        self.file.write(line + "\n")

    def close(self):
        self.file.close()
