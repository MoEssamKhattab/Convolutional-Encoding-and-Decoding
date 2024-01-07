from BPSK.pbsk_transmitter import bpsk_transmitter
from BPSK.bpsk_receiver import bpsk_receiver
from encoder import encoder
from communication_link import communication_link

bit_seq = [0, 1, 0, 1, 1, 0, 1, 0]
fc = 1000
Ab = 1
Tb = 1
n = 1000

generator_polynomials_example = [[1, 1, 1], [0, 1, 1], [1, 0, 1]]
s = '010011'

sequence = encoder.channel_encoder(s,generator_polynomials_example,3,3)
print(sequence)

passbannd_signal = bpsk_transmitter(sequence, fc, Ab, Tb, n)

restored_src_encoded_bit_seq = communication_link(sequence,passbannd_signal,0,20,2, fc, Tb, n)

print(restored_src_encoded_bit_seq)