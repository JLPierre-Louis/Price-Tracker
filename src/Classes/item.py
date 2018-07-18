"""
Author: Luco
Author: Ryan
Python Version: 3.7
"""


class Item(object):

    def __init__(self, price, url, email, name="", brand="", priority=0,
                 starred=False, group=None):
        self._name = name
        self._price = price
        self._last_accessed = None   # future
        self._priority = priority
        self._starred = starred
        self._group = group
        self._url = url
        self._email = email
        self._brand = brand

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def last_accessed(self):
        return self._last_accessed

    @property
    def priority(self):
        return self._priority

    @property
    def starred(self):
        return self._starred

    @property
    def group(self):
        return self._group

    @property
    def url(self):
        return self._url

    @property
    def email(self):
        return self._email

    @property
    def brand(self):
        return self._brand