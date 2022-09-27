# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:24:22 2022

@author: manuz
"""

def is_all_upper(text: str) -> bool:
    if text.upper() == text:
        return True
    if text.upper() != text:
        return False
    
def test_is_all_upper():
    assert is_all_upper('False answer') == False