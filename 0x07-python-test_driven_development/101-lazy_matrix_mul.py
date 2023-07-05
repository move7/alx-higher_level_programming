#!/usr/bin/python3
"""Multiplies 2 matrices by using the module NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Parmeters:
        m_a and m_b : two matrices.
    Returns:
        a matrix that represent the multiplication of m_a by m_b.
    """

    return (np.matmul(m_a, m_b))
