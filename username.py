def groupfinder(userid, request):
    user = Users.by_id(userid)
    return [g.groupname for g in user.mygroups]

class Groups(Base):
    __tablename__ = 'groups'
    id = sa.Column(sa.Integer,
                   sa.Sequence('groups_seq_id', optional=True),
                   primary_key=True)
    groupname = sa.Column(sa.Unicode(255), unique=True)

    def __init__(self, groupname):
        self.groupname = groupname

class Users(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer,
                   sa.Sequence('users_seq_id', optional=True),
                   primary_key=True)
    username = sa.Column(sa.Unicode(80), nullable=False, unique=True)
    password = sa.Column(sa.Unicode(80), nullable=False)
    mygroups = orm.relationship(Groups, secondary='user_group')

    def __init__(self, user, password):
        self.username = user
        self._set_password(password)

    @classmethod
    def by_id(cls, userid):
        return Session.query(Users).filter(Users.id==userid).first()

    @classmethod
    def by_username(cls, username):
        return Session.query(Users).filter(Users.username==username).first()

    def _set_password(self, password):
        hashed_password = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password

        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password_8bit + salt.hexdigest())
        hashed_password = salt.hexdigest() + hash.hexdigest()

        if not isinstance(hashed_password, unicode):
            hashed_password = hashed_password.decode('UTF-8')

        self.password = hashed_password

    def validate_password(self, password):
        hashed_pass = sha1()
        hashed_pass.update(password + self.password[:40])
        return self.password[40:] == hashed_pass.hexdigest()

user_group_table = sa.Table('user_group', Base.metadata,
    sa.Column('user_id', sa.Integer, sa.ForeignKey(Users.id)),
    sa.Column('group_id', sa.Integer, sa.ForeignKey(Groups.id)),
)
