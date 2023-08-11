# main.py

import os
import random
import subprocess

# import shutil

# print_ans = True


class Question:
    # I don't have a good way of storing the args for question_f
    def __init__(self, print_func, file_string, row_width, column_height):
        self._print_func = print_func
        self._file_string = file_string
        self.row_width = row_width
        self.column_height = column_height

    def get_command(self):
        with open(self._file_string, "r", newline="\n") as f:
            return f.read()


class TwoInputs(Question):
    def __init__(self, start, stop, print_func, file_string, row_width, column_height):
        self.start = start
        self.stop = stop
        super().__init__(print_func, file_string, row_width, column_height)

    def print_question(self):
        return self._print_func(self.start, self.stop)


def init_questions():
    def mult_question(start, stop):
        a = random.randrange(start, stop)
        b = random.randrange(start, stop)
        prod = a * b

        q_pair = (
            "\\multq{" + str(a) + "}" + "{" + str(b) + "}",
            "\\multq" + "[" + str(prod) + "]" + "{" + str(a) + "}" + "{" + str(b) + "}",
        )

        return q_pair

    global mult
    mult = TwoInputs(
        2,
        12,
        mult_question,
        "../latex/questions/mult.txt",
        5,
        12,
    )


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

    output += half_page_questions(mult)  # this is not yet genearalized

    output += "\n\\end{document}"

    with open("./output/output.tex", "w+", newline="\n") as f:
        f.write(output)

    subprocess.run(
        "latexmk -xelatex -output-directory=./output ./output/output.tex",
        shell=True,
        stdout=subprocess.DEVNULL,
    )


def half_page_questions(q):
    def make_row(row_width):
        row = ""
        ans_row = ""
        row += "\\begin{multicols}{" + str(row_width) + "}\n"
        ans_row += "\\begin{multicols}{" + str(row_width) + "}\n"
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
init_questions()

# TODO
# - make a single page of multiplication
# - start another question type
