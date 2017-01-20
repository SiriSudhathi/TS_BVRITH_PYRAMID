class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    password = Column(String(300), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = hashlib.sha224(password).hexdigest()
        
def __repr__(self):
        return "<User(username ='%s', password='%s')>" % (self.username, self.password)
