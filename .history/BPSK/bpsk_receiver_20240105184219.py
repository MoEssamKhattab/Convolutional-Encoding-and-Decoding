import numpy as np
from .pbsk_transmitter import generate_basis_function

def bpsk_receiver(received_signal, fc, Tb, n):
    """
    BPSK correlator receiver
    :param received_signal: received signal
    :param fc: carrier frequency
    :param Tb: bit duration
    :param n: number of samples per bit duration
    :return: restored bit sequence
    """
    num_bits = len(received_signal) // n
    restored_bit_seq = np.zeros(num_bits)

    t_total = num_bits * Tb
    dt = Tb/n
    t = np.arange(0, t_total, dt)

    basis_function = generate_basis_function(fc, Tb, n)

    for i in range(num_bits):
        symbol = received_signal[i*n:(i+1)*n]
        t_symbol = t[i*n:(i+1)*n]

        observable_element = detector(symbol, t_symbol, basis_function)
        restored_bit_seq[i] = 1 if observable_element > 0 else 0

    return restored_bit_seq, t

def detector(symbol, t_symbol, basis_function):
    """
    Correlator detector
    :param symbol: symbol to be detected
    :param t_symbol: time axis for symbol
    :param basis_function: basis function
    :return: observable element
    """
    return np.trapz(np.multiply(symbol, basis_function), t_symbol)