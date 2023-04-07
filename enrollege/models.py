from enrollege import db, login_manager
from enrollege import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=30), nullable=False, unique=True)
    firstname = db.Column(db.String(length=30), nullable=False)
    lastname = db.Column(db.String(length=30), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False, unique=True)

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correctness(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=30), nullable=False, unique=True)
    firstname = db.Column(db.String(length=30), nullable=False)
    lastname = db.Column(db.String(length=30), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False, unique=True)

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correctness(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get_or_404(user_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Profile(db.Model, UserMixin):
    __tablename__ = "profile"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), unique=True, nullable=False)
    sat_score = db.column(db.Integer(), nullable=False)
    max_tuition = db.column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'SAT: {self.sat_score}, Max Tuition: {self.max_tuition}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get_or_404(user_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Result(db.Model, UserMixin):
    __tablename__ = "result"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), unique=True, nullable=False)
    # University name and Acceptance rate for the 5 universities to be recommended
    u1 = db.Column(db.String(length=100), unique=True, nullable=False)
    r1 = db.Column(db.Float(), nullable=False)
    u2 = db.Column(db.String(length=100), unique=True, nullable=False)
    r2 = db.Column(db.Float(), nullable=False)
    u3 = db.Column(db.String(length=100), unique=True, nullable=False)
    r3 = db.Column(db.Float(), nullable=False)
    u4 = db.Column(db.String(length=100), unique=True, nullable=False)
    r4 = db.Column(db.Float(), nullable=False)
    u5 = db.Column(db.String(length=100), unique=True, nullable=False)
    r5 = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'#1 University: {self.u1} \t| Acceptance rate: {self.r1}\n' \
               f'#2 University: {self.u2} \t| Acceptance rate: {self.r2}\n' \
               f'#3 University: {self.u3} \t| Acceptance rate: {self.r3}\n' \
               f'#4 University: {self.u4} \t| Acceptance rate: {self.r4}\n' \
               f'#5 University: {self.u5} \t| Acceptance rate: {self.r5}\n '

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get_or_404(user_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()