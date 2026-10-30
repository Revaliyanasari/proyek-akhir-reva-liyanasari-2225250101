import random


def buat_soal(operasi):
    """Membuat soal aritmetika sederhana secara acak."""
    angka1 = random.randint(1, 20)
    angka2 = random.randint(1, 20)

    if operasi == "+":
        soal = f"{angka1} + {angka2}"
        jawaban = angka1 + angka2

    elif operasi == "-":
        soal = f"{angka1} - {angka2}"
        jawaban = angka1 - angka2

    elif operasi == "*":
        soal = f"{angka1} * {angka2}"
        jawaban = angka1 * angka2

    elif operasi == "/":
        angka2 = random.randint(1, 10)
        angka1 = angka2 * random.randint(1, 10)
        soal = f"{angka1} / {angka2}"
        jawaban = angka1 // angka2

    else:
        raise ValueError("Operasi tidak dikenali.")

    return soal, jawaban