from util.util import encode_sequence_with_polynomial, generate_binary_sequences

generator_polynomials_example = [[1, 1, 1], [0, 1, 1], [1, 0, 1]]


def divide_into_blocks(A, block_size):
    num_blocks = (len(A) + block_size - 1) // block_size
    A += '0' * (num_blocks * block_size - len(A))
    blocks = [A[i * block_size: (i + 1) * block_size] for i in range(num_blocks)]
    return blocks


def convert_sequence_to_string(sequence):
    S = []
    for i in range(len(sequence[0])):
        for j in range(len(sequence)):
            S.append(sequence[j][i])
    return S


def encode(A, generator_polynomials, k):
    A = '0' * (k - 1) + A
    encoded_sequences = []
    for polynomial in generator_polynomials:
        C = ''
        for i in range(len(A) - k + 1):
            curr_list = A[i:i + k]
            curr_list = curr_list[::-1]
            C += encode_sequence_with_polynomial(curr_list, polynomial)
        encoded_sequences.append(C)
    encoded_sequence_string = convert_sequence_to_string(encoded_sequences)
    return encoded_sequence_string


def encode_all_blocks(blocks, generator_polynomials, k):
    encoded_sequences = []
    for block in blocks:
        sequence = encode(block, generator_polynomials, k)
        encoded_sequences.extend(sequence)
    encoded_sequences = [int(char) for string in encoded_sequences for char in string]
    return encoded_sequences


def channel_encoder(A, generator, k, block_size):
    blocks = divide_into_blocks(A, block_size)
    return encode_all_blocks(blocks, generator, 3)
