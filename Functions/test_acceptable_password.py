# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:57:47 2022

@author: manuz
"""
def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    return cond1


def test_acceptable_password():
    assert is_acceptable_password('environment') == True