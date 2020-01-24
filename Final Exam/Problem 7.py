class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        # FILL THIS IN
        self.keys = []
        self.items = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        # FILL THIS IN
        if k in self.keys:
            ourind = self.keys.index(k)
            self.items[ourind] = v
        else:
            self.keys.append(k)
            self.items.append(v)

    def getval(self, k):
        """ k, immutable object  """
        # FILL THIS IN
        try:
            ourind = self.keys.index(k)
            return self.items[ourind]
        except:
            raise KeyError(k)

    def delete(self, k):
        """ k, immutable object """
        # FILL THIS IN
        try:
            myind = self.keys.index(k)
            del self.keys[myind]
            del self.items[myind]
        except:
            raise KeyError(k)


