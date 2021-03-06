#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2015-2019, Vincenzo Arcidiacono;
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl

"""
It contains classes and functions of general utility.

These are python-specific utilities and hacks - general data-processing or
numerical operations.
"""

import itertools

__author__ = 'Vincenzo Arcidiacono <vinci1it2000@gmail.com>'


def counter(start=0, step=1):
    """
    Return a object whose .__call__() method returns consecutive values.

    :param start:
        Start value.
    :type start: int, float, optional

    :param step:
        Step value.
    :type step: int, float, optional
    """
    return itertools.count(start, step).__next__


class Token(str):
    """
    It constructs a unique constant that behaves like a string.

    Example::

        >>> s = Token('string')
        >>> s
        string
        >>> s == 'string'
        False
        >>> s == Token('string')
        False
        >>> {s: 1, Token('string'): 1}
        {string: 1, string: 1}
        >>> s.capitalize()
        'String'
    """

    # noinspection PyMissingConstructor
    def __init__(self, *args):
        import inspect
        f = inspect.currentframe()
        self.module_name = f and f.f_back and f.f_back.f_globals.get('__name__')
        del f

    def __reduce__(self):
        if self.module_name:
            import importlib
            mdl = importlib.import_module(self.module_name)
            for name, obj in mdl.__dict__.items():
                if obj is self:
                    return getattr, (mdl, name)
        return super(Token, self).__reduce__()

    def __repr__(self):
        return self

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self is not other

    def __hash__(self):
        return id(self)

    def __copy__(self):
        return self

    # noinspection PyUnusedLocal
    def __deepcopy__(self, memo):
        return self


def pairwise(iterable):
    """
    A sequence of overlapping sub-sequences.

    :param iterable:
        An iterable object.
    :type iterable: iterable

    :return:
        A zip object.
    :rtype: zip

    Example::

        >>> list(pairwise([1, 2, 3, 4, 5]))
        [(1, 2), (2, 3), (3, 4), (4, 5)]
    """

    a, b = itertools.tee(iterable)

    next(b, None)

    return zip(a, b)
