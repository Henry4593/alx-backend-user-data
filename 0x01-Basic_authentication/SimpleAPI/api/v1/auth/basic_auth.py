#!/usr/bin/env python3
"""
Module for Basic Authentication handling.

This module provides functionality for extracting and decoding Base64-encoded
authorization headers commonly used in Basic Authentication. It includes a
class `BasicAuth` that extends the `Auth` class, offering methods to process
authentication headers, extract user credentials, and validate user identities.

The module utilizes regular expressions for token extraction and Base64
encoding for decoding tokens into readable formats.
"""
from api.v1.auth.auth import Auth
import base64
import re
import binascii
from typing import Tuple, TypeVar, Union
from models.user import User


class BasicAuth(Auth):
    """
    A class for handling basic authentication tasks, such as extracting and
    decoding Base64-encoded authorization headers. Inherits from the `Auth`
    class to extend its functionality with Basic Authentication-specific
    methods.
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> Union[str, None]:
        """
        Extracts the Base64-encoded token from an HTTP Basic Authorization
        header.

        Args:
            authorization_header (str): The HTTP authorization header
            containing the Basic token.

        Returns:
            str: The Base64-encoded token extracted from the authorization
            header.
            None: If the header is invalid or doesn't match the expected
            format.
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            matched_auth = re.fullmatch(pattern, authorization_header.strip())
            if matched_auth is not None:
                return matched_auth.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> Union[str, None]:
        """
        Decodes a Base64-encoded authorization token into a UTF-8 string.

        Args:
            base64_authorization_header (str): The Base64-encoded authorization
            token.

        Returns:
            str: The decoded authorization string, in UTF-8 format.
            None: If decoding fails due to invalid Base64 data or encoding
            errors.
        """
        if type(base64_authorization_header) == str:
            try:
                decoded_auth_header = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return decoded_auth_header.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts user credentials (email and password) from a decoded
        authorization header.

        Args:
            decoded_base64_authorization_header (str): The decoded
            authorization header in the format "email:password".

        Returns:
            Tuple[str, str]: A tuple containing the user email and password.
            (None, None): If the input string is invalid or doesn't match the
            expected pattern.
        """
        if type(decoded_base64_authorization_header) == str:
            pattern = r'(?P<user_email>[^:]+):(?P<password>.+)'
            matched_decode_b64auth_header = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip()
            )
            if matched_decode_b64auth_header is not None:
                user_email = matched_decode_b64auth_header.group('user_email')
                password = matched_decode_b64auth_header.group('password')
                return user_email, password
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieves a `User` object based on provided credentials.

        Args:
            user_email (str): The user's email address.
            user_pwd (str): The user's password.

        Returns:
            User: The `User` object if credentials match a user in the database
            None: If the email is not found or the password is incorrect.
        """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) == 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the authorization header in a
        request.

        Args:
            request: The HTTP request object containing authorization details.

        Returns:
            User: The authenticated `User` object if credentials are valid.
            None: If the user cannot be authenticated.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
