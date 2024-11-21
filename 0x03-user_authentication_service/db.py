"""Database module for user authentication service.
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """Database class for managing user data.
    """

    def __init__(self) -> None:
        """Initialize a new instance of the DB class.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def session(self) -> Session:
        """Create and return a session object.
        """
        if self.session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.session = DBSession()
        return self.session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            self.__session.add(user)
            self.__session.commit()
        except Exception:
            self.__session.rollback()
            user = None
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database by specified attributes.
        """
        fields, values = [], []
        for key, value in kwargs.items():
            if hasattr(User, key):
                fields.append(getattr(User, key))
                values.append(value)
            else:
                raise InvalidRequestError()
        result = self.session.query(User).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound()
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes in the database.
        """
        user = self.find_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                update_source[getattr(User, key)] = value
            else:
                raise ValueError()
        self.session.query(User).filter(User.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self.session.commit()
