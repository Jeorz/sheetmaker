# main.py

import os
import random
import subprocess

import sympy as sp

import ques

# import shutil

# print_ans = True

ques.init_questions()


def make_page(question_type):
    def get_preamble():
        with open("../latex/template.tex", "r", newline="\n") as f:
            preamble = ""

            for line in f:
                if line == "\\begin{document}\n":
                    break
                preamble += line

            return preamble

    # I plan this to be a dict that stores all the functions for making the questions
    # question_types =

    output = ""
    output += get_preamble() + "\n"

    output += mult.get_command()  # This is currently wrong

    output += "\n\\begin{document}\n\n"

    output += print_questions(mult)  # this is not yet genearalized

    output += "\n\\end{document}"

    with open("./output/output.tex", "w+", newline="\n") as f:
        f.write(output)

    subprocess.run(
        "latexmk -xelatex -output-directory=./output ./output/output.tex",
        shell=True,
        stdout=subprocess.DEVNULL,
    )


def print_questions(q):
    def make_row(row_width):
        row = ""
        ans_row = ""
        row += f"\\begin{{multicols}}{{{str(row_width)}}}\n"
        ans_row += f"\\begin{{multicols}}{{{str(row_width)}}}\n"
        for i in range(row_width):
            question = q.print_question()
            row += question[0] + "\n"
            ans_row += question[1] + "\n"

        row += "\\end{multicols} \n"
        ans_row += "\\end{multicols} \n"
        return (row, ans_row)

    def make_columns(column_height):
        def add_q_env(string):
            string = "\\begin{questions}\n\n" + string + "\\end{questions}"
            return string

        column = ""
        ans_column = ""
        for i in range(column_height):
            row = make_row(q.row_width)
            column += row[0] + "\n"
            ans_column += row[1] + "\n"

        column = add_q_env(column)
        ans_column = add_q_env(ans_column)

        final = column + "\\clearpage\n\n" + ans_column

        return final

    return make_columns(q.column_height)


# testing functions
# init_mult()

# sympy testing
# x = sp.symbols("x")
# eq = sp.Eq(2 * x, 8)
# sp.solve(eq)


# TODO
# - make a single page of multiplication
# - start another question type
