import numpy as np
import matplotlib.pyplot as plt
from BPSK.bpsk_receiver import bpsk_receiver
from util.util import awgn, calculate_ber


def communication_link(bit_seq, src_encoded_mod_sig, snr_start, snr_end, snr_step, fc, Tb, n):
    """
    Communication Link (AWGN Channel -> Demodulation)
    :param bit_seq: original bit sequence
    :param src_encoded_mod_sig: source encoded modulated signal
    :param channel_encoded_mod_sig: channel encoded modulated signal
    :param snr_start: start point of SNR
    :param snr_end: end point of SNR
    :param snr_step: step of SNR
    :return: restored bit sequence of source encoded signal and channel encoded signal
    """
    SNR_dB = np.arange(snr_start, snr_end + snr_step, snr_step)
    src_encoded_ber = np.zeros(len(SNR_dB))
    channel_encoded_ber = np.zeros(len(SNR_dB))

    for i in range(len(SNR_dB)):
        # AWGN Channel
        noisy_src_encoded_sig = awgn(src_encoded_mod_sig, SNR_dB[i])

        # noisy_channel_encoded_sig = awgn(channel_encoded_mod_sig, SNR_dB[i])

        # Demodulation
        restored_src_encoded_bit_seq = bpsk_receiver(noisy_src_encoded_sig, fc, Tb, n)
        # restored_channel_encoded_bit_seq = bpsk_receiver(noisy_channel_encoded_sig)

        # BER
        src_encoded_ber[i] = calculate_ber(bit_seq, restored_src_encoded_bit_seq)

        # TODO: Channel Decoding here
        # channel_encoded_ber[i] = calculate_ber(bit_seq, restored_channel_encoded_bit_seq)

    #plt.plot(SNR_dB, channel_encoded_ber, label='Channel Encoded')
    plt.plot(SNR_dB, src_encoded_ber, label='Source Encoded')
    plt.yscale('log')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.legend()
    plt.grid()
    plt.show()

    print(src_encoded_ber)
    return restored_src_encoded_bit_seq  # of the max SNR
