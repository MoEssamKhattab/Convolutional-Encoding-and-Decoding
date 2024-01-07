import numpy as np

def bpsk_transmitter(bit_seq, fc, Ab, Tb, n):
    """
    BPSK transmitter
    :param bit_seq: bit sequence
    :param fc: carrier frequency
    :param Ab: amplitude of message signal pulse
    :param Tb: bit duration
    :param n: number of samples per bit duration
    :return: BPSK modulated signal
    """
    if fc <= 10/Tb:
        raise ValueError('Carrier frequency (fc) must be at least 10 times the the bit rate (1/Tb)')
    
    num_bits = len(bit_seq)         # number of bits
    n_total = num_bits * n      # total number of samples

    t_total = num_bits * Tb     # total time duration of symbol/bit
    dt = Tb/n
    t = np.arange(0, t_total, dt) # time axis

    Eb = Ab**2 * Tb
    basis_function = generate_basis_function(fc, Tb, n)
    passbannd_signal = np.zeros(n_total)

    for i in range(num_bits):
        sign = (-1)**(bit_seq[i]+1) # bit 1 -> 1, bit 0 -> -1       
        passbannd_signal[i*n:(i+1)*n] = sign * np.sqrt(Eb) * basis_function

    return passbannd_signal, t

def generate_basis_function(fc, Tb, n):
    """
    Generate basis function for BPSK modulation
    :param fc: carrier frequency
    :param Tb: bit duration
    :param n: number of samples per bit duration
    :return: basis function
    """
    dt = Tb/n
    t_symbol = np.arange(0, Tb, dt)
    return np.sqrt(2/Tb) * np.cos(2*np.pi*fc*t_symbol)

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

        observable_element = detector(symbol, dt, basis_function)
        restored_bit_seq[i] = 1 if observable_element > 0 else 0

    return restored_bit_seq, t

def detector(symbol, dt, basis_function):
    """
    Correlator detector
    :param symbol: symbol to be detected
    :param t_symbol: time axis for symbol
    :param basis_function: basis function
    :return: observable element
    """
    return np.trapz(np.multiply(symbol, basis_function), dx = dt)


bit_seq = [0, 1, 0, 1, 1, 0, 1, 0]
fc = 1000
Ab = 1
Tb = 1
n = 1000

passbannd_signal, t = bpsk_transmitter(bit_seq, fc, Ab, Tb, n)

# plot passband signal
import matplotlib.pyplot as plt
plt.plot(t, passbannd_signal)
plt.xlabel('t')
plt.ylabel('s(t)')
plt.title('Passband signal')

restored_bit_seq, t = bpsk_receiver(passbannd_signal, fc, Tb, n)

print(restored_bit_seq)