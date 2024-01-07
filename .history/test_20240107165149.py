from BPSK.pbsk_transmitter import bpsk_transmitter
from BPSK.bpsk_receiver import bpsk_receiver


bit_seq = [0, 1, 0, 1, 1, 0, 1, 0]
fc = 1000
Ab = 1
Tb = 1
n = 1000

passbannd_signal = bpsk_transmitter(bit_seq, fc, Ab, Tb, n)

#TODO: add the AWGN channel here

restored_bit_seq = bpsk_receiver(passbannd_signal, fc, Tb, n)

print(restored_bit_seq)