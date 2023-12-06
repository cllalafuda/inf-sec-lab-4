TEXT_MAPPING = {
    "1": "0123456789",
    "2": "9876543210",
    "3": " 1000005",  # пробелы указаны в варианте
    "4": " 1500000"  # пробелы указаны в варианте
}

a = 23
b = 7
c = 256
t0 = 131
sequence = []


def select_variant():
    variants = "\n".join(f"{k} - {v}" for (k, v) in TEXT_MAPPING.items()) + "\n"
    print(f"Выберите вариант:\n{variants}")
    choice = input("Введите номер выбранного варианта (1, 2, 3 или 4): ")
    return choice


def get_hash(P, c, sequence):
    K = 0
    for l in P:
        K = K + ord(l)
        sequence.append(ord(l))
    if K < c - 1:
        k_summ = K
        return k_summ
    else:
        k_summ = K % c
        print(K, c, k_summ)
        return k_summ


def get_gamma_sequence(a, b, t0, length, n):
    gamma_sequence = []
    max_val = 2 ** n - 1

    for i in range(length):
        ti = (a * t0 + b) % max_val
        gamma_sequence.append(ti)
        t0 = ti

    return gamma_sequence


def get_checksum(text, gamma_sequence, max_val):
    checksum = 0

    for i in range(len(text)):
        Yi = ord(text[i]) ^ gamma_sequence[i]
        checksum = (checksum + Yi) % (max_val + 1)

    return checksum


def main():
    P = select_variant()
    length = len(P)
    n = 8
    gamma_sequence = get_gamma_sequence(a, b, t0, length, n)
    max_val = 2 ** n - 1
    checksum = get_checksum(P, gamma_sequence, max_val)
    checksum1 = get_hash(P, c, sequence)
    print(f"""Текст: {P}
Последовательность гаммы: {gamma_sequence}
Контрольная сумма гаммированием: {checksum}
Контрольная сумма методом контрольных сумм: {checksum1}""")


if __name__ == '__main__':
    main()
