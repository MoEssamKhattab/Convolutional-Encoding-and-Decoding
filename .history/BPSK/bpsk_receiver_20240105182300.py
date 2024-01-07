import numpy as np

def bpsk_receiver(recieved_signal, fc, ):
    pass


def detector(symbol, t_symbol, basis_function):

    return np.trapz(np.multiply(symbol,basis_function), t_symbol)