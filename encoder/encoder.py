from util import encode_sequence_with_polynomial, add_awgn

generator_polynomials_example = [[1, 1, 1], [0, 1, 1], [1, 0, 1]]


def encode(A, generator_polynomials, k):
    A = '0' * (k - 1) + A
    encoded_sequencies = []
    for polynomial in generator_polynomials:
        C = ''
        for i in range(len(A) - k + 1):
            C += encode_sequence_with_polynomial(A[i:i + k], polynomial)
        encoded_sequencies.append(C)
    return encoded_sequencies


print(encode('100101', generator_polynomials_example, 3))
