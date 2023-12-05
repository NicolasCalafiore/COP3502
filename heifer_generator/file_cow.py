from cow import Cow

class FileCow(Cow):
    def __init__(self, name, filename):
        super().__init__(name)
        self.filename = filename
        temp = open(f'{self.filename}.cow', "r").read()
        self.set_image(temp)


    def set_image(self, image):
        try:
            self.image = image
        except:
            raise RuntimeError('MOOOOO!!!!!')
        




