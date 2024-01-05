import numpy as np

def bpsk_modulator(bit_seq):
    """
    BPSK modulator
    :param bit_seq: bit sequence
    :return: BPSK modulated signal
    """


def gnerate_message(Eb):
    return [np.sqrt(Eb),    # s11, symbol 1
            -np.sqrt(Eb)]   # s21, symbol 0

def generate_basis_function(fc, Tb, n):
    """
    Generate basis function for BPSK modulation
    :param fc: carrier frequency
    :param Tb: bit duration
    :param n: number of samples per bit duration
    :return: basis function
    """
    dt = Tb/n
    t_symbol = np.arange(0, Tb-dt, dt)
    return np.sqrt(2/Tb) * np.cos(2*np.pi*fc*t_symbol)