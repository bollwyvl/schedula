#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2015-2019, Vincenzo Arcidiacono;
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl
"""
It contains a comprehensive list of all modules and classes within schedula.

Docstrings should provide sufficient understanding for any individual function.

Modules:

.. currentmodule:: schedula

.. autosummary::
    :nosignatures:
    :toctree: _build/schedula

    ~dispatcher
    ~utils
    ~ext
"""
import sys
import functools
# noinspection PyUnresolvedReferences
from ._version import *

_all = {
    'Dispatcher': '.dispatcher',
    'BlueDispatcher': '.utils.blue',
    'Blueprint': '.utils.blue',
    'PoolExecutor': '.utils.asy',
    'ProcessExecutor': '.utils.asy',
    'ThreadExecutor': '.utils.asy',
    'register_executor': '.utils.asy',
    'shutdown_executor': '.utils.asy',
    'shutdown_executors': '.utils.asy',
    'await_result': '.utils.asy',
    'EMPTY': '.utils.cst',
    'START': '.utils.cst',
    'NONE': '.utils.cst',
    'SINK': '.utils.cst',
    'SELF': '.utils.cst',
    'END': '.utils.cst',
    'PLOT': '.utils.cst',
    'stlp': '.utils.dsp',
    'combine_dicts': '.utils.dsp',
    'bypass': '.utils.dsp',
    'summation': '.utils.dsp',
    'map_dict': '.utils.dsp',
    'map_list': '.utils.dsp',
    'selector': '.utils.dsp',
    'replicate_value': '.utils.dsp',
    'add_args': '.utils.dsp',
    'stack_nested_keys': '.utils.dsp',
    'get_nested_dicts': '.utils.dsp',
    'inf': '.utils.dsp',
    'are_in_nested_dicts': '.utils.dsp',
    'SubDispatchFunction': '.utils.dsp',
    'combine_nested_dicts': '.utils.dsp',
    'SubDispatch': '.utils.dsp',
    'parent_func': '.utils.dsp',
    'SubDispatchPipe': '.utils.dsp',
    'DispatchPipe': '.utils.dsp',
    'kk_dict': '.utils.dsp',
    'add_function': '.utils.dsp',
    'DispatcherError': '.utils.exc',
    'DispatcherAbort': '.utils.exc',
    'ExecutorShutdown': '.utils.exc',
    'SkipNode': '.utils.exc',
    'counter': '.utils.gen',
    'Token': '.utils.gen',
    'pairwise': '.utils.gen',
    'save_dispatcher': '.utils.io',
    'load_dispatcher': '.utils.io',
    'save_default_values': '.utils.io',
    'load_default_values': '.utils.io',
    'save_map': '.utils.io',
    'load_map': '.utils.io'
}

__all__ = tuple(_all)


@functools.lru_cache(None)
def __dir__():
    return __all__ + (
        '__doc__', '__author__', '__updated__', '__title__', '__version__',
        '__license__', '__copyright__'
    )


def __getattr__(name):
    if name in _all:
        import importlib
        obj = getattr(importlib.import_module(_all[name], __name__), name)
        globals()[name] = obj
        return obj
    raise AttributeError("module %s has no attribute %s" % (__name__, name))


if sys.version_info[:2] < (3, 7):
    globals().update({k: __getattr__(k) for k in _all})
