import pytest
from add_module import add

class TestAdd:
    def test_add_int(self):
        assert add(3, 4) == 7
    
    def test_add_str(self):
        assert add('hello', 'world') == 'helloworld'

    def test_add_int_str(self):
        assert add(3, 'hello') == 8