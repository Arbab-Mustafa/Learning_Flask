class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {"username": self.username, "email": self.email}
