class Dam:
    def __init__(self,name,length):
        self.name=name
        self._length=length
    def get_length(self):
        return self._length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam length:",dam1._length)