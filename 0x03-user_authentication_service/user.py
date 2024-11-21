#!/usr/bin/env python3
"""
This module defines the User class and sets up the database connection
using SQLAlchemy.
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from uuid import uuid4

Base = declarative_base()


class User(Base):
    """
    User class represents a user in the database.

    Attributes:
        id (int): Unique identifier for the user.
        email (str): User's email address, must be unique and not null.
        hashed_password (str): User's hashed password, cannot be null.
        session_id (str, optional): Session identifier for the user, can be
            null.
        reset_token (str, optional): Token used for resetting the user's
            password, can be null.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
