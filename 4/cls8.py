class Table:
    def __init__(self):
        self.no_of_legs=4
        self._glass_top=None
        self._wooden_top=None
    def assign_data(self, glass_top, wooden_top):
        self._glass_top=glass_top
        self._wooden_top=wooden_top
    def identify_rate (self, glass_top, wooden_top):
        self.assign_data(glass_top, wooden_top)
        if (self._glass_top==True):
            rate = 20000
        elif (self._wooden_top==True):
            rate = 30000
        else:
            rate=0
        return rate


