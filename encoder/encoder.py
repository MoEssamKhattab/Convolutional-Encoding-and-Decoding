from util import encode_sequence_with_polynomial

generator_polynomials_example = [[1, 1, 1], [0, 1, 1], [1, 0, 1]]


def divide_into_blocks(A,block_size):
    num_blocks = (len(A) + block_size - 1) // block_size
    A += '0' * (num_blocks * block_size - len(A))
    blocks = [A[i * block_size: (i + 1) * block_size] for i in range(num_blocks)]
    return blocks


def encode(A, generator_polynomials, k):
    A = '0' * (k - 1) + A
    encoded_sequences = []
    for polynomial in generator_polynomials:
        C = ''
        for i in range(len(A) - k + 1):
            C += encode_sequence_with_polynomial(A[i:i + k], polynomial)
        encoded_sequences.append(C)
    return encoded_sequences


def encode_all_blocks(blocks, generator_polynomials, k):
    encoded_sequences = []
    for block in blocks:
        sequence = encode(block,generator_polynomials,k)
        encoded_sequences.append(sequence)
    return encoded_sequences


blocks = divide_into_blocks('010001010001011',5)
print(encode_all_blocks(blocks, generator_polynomials_example, 3))
