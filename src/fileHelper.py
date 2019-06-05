class FileHelper:

    def __init__(self, file):
        self.file = open(file, "a")

    def write(self, line):
        self.file.write(line + "\n")

    def close(self):
        self.file.close()
