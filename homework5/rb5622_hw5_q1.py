from ArrayStack import ArrayStack

def calculate(a, b, sign):
    if sign == "+":
        res = a + b
    elif sign == "-":
        res = a - b
    elif sign == "*":
        res = a * b
    else:
        res = a / b
    return res

def evaluate_expression(expression, variables):
    st = ArrayStack()
    operations = "+-*/"
    st.push(expression[0])
    i = 1
    for el in expression:
        # while not st.is_empty():
        # el = expression[i]
        if el in operations:
            val2 = int(st.pop())
            val1 = int(st.pop())
            res = calculate(val1, val2, el)
            st.push(res)
        elif el.isdigit():
            st.push(el)
        else:
            for tpl in variables:
                if el == tpl[0]:
                    st.push(tpl[1])
        i += 1
    return st.pop()

def prompter():
    variables = []
    inp = ""
    while inp != "done()":
        inp = input("--> ")
        expression = inp.split()
        if len(expression) == 1:
            if expression[0].isdigit():
                print(int(expression[0]))
            else:
                for tpl in variables:
                    if expression[0] == tpl[0]:
                        print(tpl[1])
        elif expression[1] != "=":
            print(evaluate_expression(expression, variables))
        else:
            var_name = expression[0]
            res = evaluate_expression(expression[2:], variables)
            tpl = (var_name, res)
            variables.append(tpl)
            print(var_name)

prompter()