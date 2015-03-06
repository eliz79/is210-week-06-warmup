#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Importing a module namespace"""

import task_01.peanut

TIME = task_01.peanut.BUTTER

if TIME:
    print 'I am truthy'
