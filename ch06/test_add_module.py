import pytest
from add_module import add

def test_add():
    result = add(3, 4)
    assert result == 7