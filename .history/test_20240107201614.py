from BPSK.pbsk_transmitter import bpsk_transmitter
from encoder import encoder
from communication_link import communication_link

bit_seq = [0, 1]
fc = 0.1
Ab = 1
Tb = 100
n = 1000

generator_polynomials_example = [[1, 1, 1], [0, 1, 1], [1, 0, 1]]
s = '010011'

#sequence = encoder.channel_encoder(s,generator_polynomials_example,3,3)
print(bit_seq)

passbannd_signal = bpsk_transmitter(bit_seq, fc, Ab, Tb, n)

restored_src_encoded_bit_seq = communication_link(bit_seq,passbannd_signal,-4,10,1, fc, Tb, n)

print(restored_src_encoded_bit_seq)