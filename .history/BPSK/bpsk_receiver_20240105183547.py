import numpy as np
from .pbsk_transmitter import generate_basis_function

def bpsk_receiver(recieved_signal, fc, Tb, n):

    num_bits = len(recieved_signal) // n
    t_total = num_bits * Tb
    dt = Tb/n
    t = np.arange(0, t_total, dt)
    basis_function = generate_basis_function(fc, Tb, n)

    pass


def detector(symbol, t_symbol, basis_function):
    """
    Correlator detector
    :param symbol: symbol to be detected
    :param t_symbol: time axis for symbol
    :param basis_function: basis function
    :return: observable element
    """
    return np.trapz(np.multiply(symbol, basis_function), t_symbol)