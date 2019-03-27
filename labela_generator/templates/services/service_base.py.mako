"""
BaseService from template
"""
import logging
from typing import Union
from uuid import UUID


class BaseService:
    """
    Base services for most services
    """

    def __init__(self, repository):
        self.logger = logging.getLogger(type(self).__name__)
        self._repository = repository

    def get(self, id_):
        """
        Get object from database based on its primary ID
        :param id_: Primary ID of the to be found object
        :return: a single object or None
        """
        return self._repository.get(id_)

    def list(self, **criteria):
        """
        Return a list of all objects in a repository
        :return: List of objects
        """
        return self._repository.list(**criteria)

    def create(self, flush=True, **kwargs):
        """
        Have the repository create a new object
        :param flush: Flush directly or not
        :param kwargs: Object attributes and values
        :return: Newly created object
        """
        return self._repository.create(flush, **kwargs)

    def update(self, object_, **data):
        """
        Have the repository update an object and return it
        :param object_: Object to update
        :param data: Model attributes and their values dictionary
        :return: Updated object
        """
        return self._repository.update(object_, **data)

    def delete(self, id_):
        """
        Performs a soft delete on an object in the database by ID
        :param id_: Id of model object to be deleted
        :return: None
        """
        return self._repository.delete(id_)
