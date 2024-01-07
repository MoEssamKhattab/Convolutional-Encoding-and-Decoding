import random


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


def add_awgn(A, Pe):
    if not (0 <= Pe <= 1):
        raise ValueError("Probability 'Pe' must be between 0 and 1")
    noise_sequence = ''.join(['1' if random.random() < Pe else '0' for _ in range(len(A))])
    result = xor_two_sequences(A, noise_sequence)

    return result


original_sequence = '00000000'
probability_of_one = 1.1
noisy_sequence = add_awgn(original_sequence, probability_of_one)
print(noisy_sequence)
