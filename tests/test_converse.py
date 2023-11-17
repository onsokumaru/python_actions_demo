#!/usr/bin/env python3

import sys
sys.path.append("../")
from python_actions_demo.modules import converse

def test_hello_world():
    assert type(converse.hello_world()) is str
def test_greet():
    assert type(converse.greet("Mortimer")) is str
def test_bye():
    assert type(converse.bye()) is str
