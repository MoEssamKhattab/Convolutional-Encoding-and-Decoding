import numpy as np


def xor_char(a, b):
    if (a == '0' and b == '0') or (a == '1' and b == '1'):
        return '0'
    else:
        return '1'


def xor_sequence(A):
    C = '0'
    for a in A:
        C = xor_char(C, a)

    return C


def xor_two_sequences(A, B):
    if len(A) != len(B):
        raise ValueError("Input sequences must have the same length")

    C = ''
    for a, b in zip(A, B):
        C += xor_char(a, b)

    return C


def encode_sequence_with_polynomial(A, polynomial):
    C = ''
    for i in range(len(A)):
        if polynomial[i] == 0:
            C += '0'
        else:
            C += A[i]
    return xor_sequence(C)

# AWGN Channel
def awgn(signal, snr):
    """
    Additive White Gaussian Noise Channel
    :param signal: input signal
    :param snr: signal to noise ratio
    :return: noisy signal
    """
    signal_power = np.sum(signal**2)/len(signal)
    noise_power = signal_power/(10**(snr/10))
    noise = np.sqrt(noise_power)*np.random.randn(len(signal))
    return signal + noise

def calculate_ber(bit_seq, restored_bit_seq):
    """
    Calculate Bit Error Rate
    :param bit_seq: original bit sequence
    :param restored_bit_seq: restored bit sequence
    :return: BER
    """
    return np.sum(a != b for a, b in zip(bit_seq, restored_bit_seq))/len(bit_seq)