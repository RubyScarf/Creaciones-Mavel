import bcrypt

class User(db.Model):
    #...

    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash)
