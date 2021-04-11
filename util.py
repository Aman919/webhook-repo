class Update:
    def __init__(self, data):
        self.data = data
    def get_id(self):
        return self.data["_id"]
