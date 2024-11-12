#!/usr/bin/env python3
"""
Authentication module for managing access control and authorization.

This module provides an `Auth` class with methods to verify if a request path
requires authentication, retrieve authorization headers, and obtain the
current user.
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """
    Class providing basic authentication functionalities, such as path
    authorization, header extraction, and user retrieval.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.

        Args:
            path (str): The request path to check.
            excluded_paths (List[str]): A list of paths that do not require
                authentication. Patterns ending with `*` allow matching
                any subpath.

        Returns:
            bool: `True` if the path requires authentication; `False` if it is
            excluded.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the 'Authorization' header from a request.

        Args:
            request: The Flask request object containing headers.

        Returns:
            str: The value of the 'Authorization' header if present; `None`
            otherwise.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from a request. This is a placeholder method
        intended to be overridden by subclasses implementing user retrieval
        logic.

        Args:
            request: The Flask request object.

        Returns:
            User: `None` by default. Subclasses should return the authenticated
            user object if available.
        """
        return None
