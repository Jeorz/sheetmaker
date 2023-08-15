# algebra.py
# generating algebra questions



# I want to add support for more operations within the
# same function here
# I imagine having a str input on alg_question() that has shorthand for
# operations. the argument 'ma' or 'am' would give an equation with
# multiplication and addition
# I also imagine there being an argument that makes the constant/coefficients
# rational or integer
#
# I also need a way to automatically make spacing between questions
# this could be a hardcoded \vspace or somehow change with question context
def init_algebra():
    def alg_add(start, stop):
        a = str(random.randrange(start, stop))
        b = str(random.randrange(start, stop))
        diff = str(int(a) - int(b))
        var = "x"

        # Need to be able to generate different order as well
        ques = f"{a} + {var} = {b} "

        # I think classes would be the best way to do this?
        def generate_ques(reverse):
            

        def generate_ans(q):
            lines = (
                q,
                f"{a} + {var} - {a} = {b} - {a}",
                f"{var} = {diff}",
            )

            ans = "\n".join(lines)

            return ans

        q_pair = (ques, generate_ans(ques))

        print(q_pair)

