#!/usr/bin/python3
"""Module implementing MyInt"""


class MyInt(int):
    """Class MyInit"""
    def __eq__(self, other):
        """Swaps meaning of `==` with `!=`
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Swaps meaning of `==` with `!=`
        """
        return super().__eq__(other)i
