# Question class


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


# class for questions that only need two integer inputs.
# I imagine this would be good for arithmetic questions where you are mostly
# concerned about the largest and the smallest numbers.
class TwoInt(Question):
    def __init__(self, start, stop, print_func, file_string, row_width, column_height):
        self.start = start
        self.stop = stop
        super().__init__(print_func, file_string, row_width, column_height)

    def print_question(self):
        return self._print_func(self.start, self.stop)
