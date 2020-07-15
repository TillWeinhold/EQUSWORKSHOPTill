class Parrot():

    def __init__(self, squawk, is_alive=True):
        self.squawk = squawk
        self.is_alive = is_alive

african_grey = Parrot('Polly want a Cracker?')
norwegian_blue = Parrot('', is_alive=False) 

def squawk(self):
        if self.is_alive:
            return self.squawk
        else:
            return None

african_grey.squawk()
norwegian_blue.squawk()

def set_alive(self, is_alive):
    self.is_alive = is_alive