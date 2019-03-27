"""
BaseRepository from template
"""
from typing import Union
from uuid import UUID

from sqlalchemy.sql.expression import desc, asc


class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def create(self, flush=True, **kwargs):
        """
        Creates a new instance of this object in the database
        :param flush: Flush directly or not
        :param kwargs: Object attributes and values
        :return: Newly created object
        """
        object_ = self.model(**kwargs)

        self.session.add(object_)
        if flush:
            self.session.flush()
        return object_

    def update(self, object_, **kwargs):
        """
        Update object and return it
        :param object_: Object to be updated
        :param data: Model attributes and their values dictionary
        :return: Updated object
        """
        for attribute, value in data.items():
            if hasattr(object_, attribute):
                setattr(object_, attribute, value)
        self.session.add(object_)
        return object_

    def list(self, offset=0, limit=25, **kwargs):
        """
        Get a list of all items of this model that are not deleted
        :param offset: rows to skip
        :param limit: results limit
        :param kwargs: filter parameters
        :return: List of objects
        """
        query = self._find(**kwargs)
        return query.limit(limit).offset(offset).all()

    def get(self, id_):
        """
        Fetch object form database based on its primary ID
        :param id_: Primary ID
        :return: Object or None
        """
        return self._query().filter(self.model.id == id_).one_or_none()

    def delete(self, id_):
        """
        Performs a soft delete on an object in the database by ID
        :param id_: Id of model object to be deleted
        :return: None
        """
        to_delete = self.get(id_)
        if to_delete:
            self.update(to_delete, deleted=utc_aware_datetime_now())

    def _find(self, order=None, **kwargs):
        """
        Prepare a query with filter kwargs
        :param offset: Int of items to skip
        :param limit: Int of items to return
        :param order: Order by attribute
        :param kwargs: Filter attributes
        :return: Query
        """
        query = self._query()
        query = self._apply_filtering(query, **kwargs)
        return self._order(query, order)

    def _apply_filtering(self, query, **kwargs):
        """
        apply filter kwargs
        :param kwargs:
        :return:
        """
        for _filter, value in kwargs.items():
            column = getattr(self.model, _filter, None)
            if column:
                if type(value) == list:
                    query = query.filter(or_(column == v for v in value))
                else:
                    query = query.filter(column == value)
        return query

    def _order(self, query, order):
        """
        Order query results
        :param order: string of order attributes separated by comma
        :return: ordered query string
        """
        if order:
            columns_to_order = self._apply_ordering(order.split(','))
            query = query.order_by(*columns_to_order)
        return query

    def _apply_ordering(self, ordering):
        """
        Logical ordering based on passed parameters
        :param ordering: List of strings to order by
        :return: Query ordering
        """
        order_list = []
        for order_value in ordering:
            column = order_value.replace('-', '')
            if not hasattr(self.model, column):
                continue
            column = getattr(self.model, column)
            if order_value.startswith('-'):
                order_list.append(desc(column))
            else:
                order_list.append(asc(column))
        return order_list

    def _query(self):
        """
        Basic function that prepares a query to exclude deleted objects
        :return: Query
        """
        query = self.session.query(self.model)
        if hasattr(self.model, 'deleted'):
            query = query.filter(self.model.deleted.is_(None))

        return query
