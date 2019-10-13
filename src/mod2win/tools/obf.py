import base64
import py_compile
import os


class Obf:
    def __init__(self, input_file=None, output_file=None):
        self.input = input_file
        self.output = output_file

    def obf(self):
        py_compile.compile(self.input, dfile="level_01.py", cfile=self.output)

    def hide(self):
        with open(self.input, "rb") as i, open(self.output, "wb") as o:
            base64.encode(i, o)
        os.unlink(self.input)

    def unhide(self):
        with open(self.input, "rb") as i, open(self.output, "wb") as o:
            base64.decode(i, o)


if __name__ == "__main__":
    pass
