import numpy as np

def bpsk_receiver(recieved_signal, fc, ):
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