#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    def extend_tuple(t):
        return t + (0,) * (2 - len(t))
    
    tuple_a = extend_tuple(tuple_a)
    tuple_b = extend_tuple(tuple_b)
    
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
