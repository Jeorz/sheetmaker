# mult.py
# generate vertical multiplication question

from question import *


def init_mult():
    def mult_question(start, stop):
        a = random.randrange(start, stop)
        b = random.randrange(start, stop)
        prod = a * b

        q_pair = (
            f"\\multq{{{str(a)}}}{{{str(b)}}}",
            f"\\multq[{str(prod)}]{{{str(a)}}}{{{str(b)}}}",
        )

        return q_pair

    global mult
    mult = TwoInt(
        2,  # start
        12,  # stop
        mult_question,
        "../latex/questions/mult.txt",
        5,  # row_width
        12,  # column_with
    )
