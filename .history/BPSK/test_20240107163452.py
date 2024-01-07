from BPSK.bpsk_receiver import bpsk_receiver
from BPSK.bpsk_trnsmitter import bpsk_transmitter


bit_seq = [0]
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