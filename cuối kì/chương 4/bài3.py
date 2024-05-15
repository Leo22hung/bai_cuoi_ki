class BieuThuc:
    def GiaTri(self, bt):
        def thuc_hien_phep_toan(operand_stack, operator_stack):
            op = operator_stack.pop()
            b = operand_stack.pop()
            a = operand_stack.pop()
            if op == '+':
                operand_stack.append(a + b)
            elif op == '-':
                operand_stack.append(a - b)
            elif op == '*':
                operand_stack.append(a * b)
            elif op == '/':
                operand_stack.append(a / b)

        priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        operand_stack = []
        operator_stack = []
        i = 0
        while i < len(bt):
            if bt[i].isdigit():
                operand = ''
                while i < len(bt) and bt[i].isdigit():
                    operand += bt[i]
                    i += 1
                operand_stack.append(int(operand))
            elif bt[i] in priority:
                while operator_stack and priority[operator_stack[-1]] >= priority[bt[i]]:
                    thuc_hien_phep_toan(operand_stack, operator_stack)
                operator_stack.append(bt[i])
                i += 1
            else:
                i += 1

        while operator_stack:
            thuc_hien_phep_toan(operand_stack, operator_stack)

        return operand_stack[-1]

bieu_thuc = BieuThuc()
print(bieu_thuc.GiaTri("3+2*4"))
