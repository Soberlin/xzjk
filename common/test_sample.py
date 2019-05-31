# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 10:45
# @Author  : Sober
# @Site    : 
# @File    : test_sample.py
import pytest
def fun(x):
    return x+1;

def test_answer():
    assert fun(3)==5;