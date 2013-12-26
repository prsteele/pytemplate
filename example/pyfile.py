__all__ = ['foo', 'bar'] # We only export 'foo' and 'bar'

from math import pi
        
def foo_helper():
    return 'some text'
    
foo = foo_helper()
        
bar = 2 * pi
