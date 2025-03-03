def arithmetic_arranger(problems, show_answers=False):
    #   ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    if len(problems)>5:
        return 'Error: Too many problems.'
    top = []   
    buttom = []   
    line = []   
    result = []   
    
    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts
        
        if operator not in ['-','+']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(num1)>4 or len(num2)>4:
            return 'Error: Numbers cannot be more than four digits.'
        
        width = max(len(num1), len(num2))+2
        
        top.append(num1.rjust(width))
        buttom.append(operator+num2.rjust(width-1))
        line.append('-'*width)
        arranged_problem = '    '.join(top)+'\n'+'    '.join(buttom)+'\n'+'    '.join(line)
        
        if show_answers:
            if operator=='+':
                result_problem = int(num1)+int(num2)
            else:
                result_problem = int(num1)-int(num2)
                
            result.append(str(result_problem).rjust(width) )
            arranged_problem= arranged_problem+'\n'+'    '.join(result)

    return arranged_problem

print(f'\n{arithmetic_arranger(["44 - 813", "9 + 2", "4 - 43", "123 + 49", "888 + 40"])}')
