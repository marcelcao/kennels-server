class Customer():
    """Class for customer data"""
    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password

    def serialized(self):
        """Only passes the non-private information"""
        return {"name": self.name, "address": self.address, "email": self.email}
