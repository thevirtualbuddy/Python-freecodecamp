def arithmetic_arranger(problems,StartPrint=False):
    
    if len(problems)>5:
        return "Error: Too many problems."
    else:
        arranged_problems=[]
        align_Operand1 = ""
        align_Result = ""
        align_operator_Operand2 = ""
        dash = ""

        for i, problem in enumerate(problems):
            elements = problem.split()
            operand1 = elements[0]
            operator = elements[1]
            operand2 = elements[2]

            if operator not in ["+","-"]:
                return "Error: Operator must be '+' or '-'."
            
            else:
                for digit in operand1:
                    if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
                      return "Error: Numbers must only contain digits."
                    else:
                      continue
                
                for digit in operand2:
                    if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
                      return "Error: Numbers must only contain digits."
                    else:
                      continue
                
                if len(operand1)>4 or len(operand2)>4:
                    return "Error: Numbers cannot be more than four digits."
                
                else:
                    if operator == "+":
                        result = int(operand1) + int(operand2)
                    else:
                        result = int(operand1) - int(operand2)
                    
                    alignLen = max(len(operand1),len(operand2)) + 2

                    align_Operand1 += str(operand1.rjust(alignLen))
                    align_operator_Operand2 += str(operator + operand2.rjust(alignLen-1))
                    dash += str("-"*alignLen)
                    align_Result += str(result).rjust(alignLen)

                    if i< len(problems)-1:
                        align_Operand1 += "    "
                        align_operator_Operand2 += "    "
                        dash += "    "
                        align_Result += "    "

                    if StartPrint:
                        arranged_problems = (align_Operand1 + "\n" + align_operator_Operand2 + "\n" + dash + "\n" + align_Result)
                    else:
                        arranged_problems = (align_Operand1 + "\n" + align_operator_Operand2 + "\n" + dash)

                    

        return arranged_problems