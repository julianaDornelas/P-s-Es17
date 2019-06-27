import pytest
#import principal importa a pasta inteira
from principal import somar #import especifico 

def test_somar():
    assert somar(2,3)==5
    
    def test_sub():
        assert sub(5,2)==3
    