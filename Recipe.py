def _formatdata(data):
    data = data.strip().split(',, ')
    return data


class Recipe:
    def __init__(self, data):
        # Initialize recipe data
        self.data = data
        self.name = ""
        self.ingredients = None
        self.directions = None
        self.readfile(data)

    @classmethod
    def fromfile(cls, filename):
        # Initialize data from file
        data = open(filename).readlines()
        return cls(data)

    @classmethod
    def fromwebsite(cls, url):
        # Initialize data from website
        data = None

    def readfile(self, data):
        # Read data
        self.name = data[0].strip()
        self.ingredients = _formatdata(data[1])
        self.directions = _formatdata(data[2])

    def scrapewebsite(self, data):
        self.name = None
        self.ingredients = None
        self.directions = None

