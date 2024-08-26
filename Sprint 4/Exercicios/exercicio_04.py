def calcular_valor_maximo(operadores, operandos):

    def aplicar_operacao(op, nums): return (
        nums[0] + nums[1] if op == '+' else
        nums[0] - nums[1] if op == '-' else
        nums[0] * nums[1] if op == '*' else
        nums[0] / nums[1] if op == '/' else
        nums[0] % nums[1]
    )

    resultados = map(lambda x: aplicar_operacao(
        x[0], x[1]), zip(operadores, operandos))

    return max(resultados)


operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)
