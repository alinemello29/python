desconto = 300.00
salario_fixo = 1650.50
vendas_mes =  50
valor_comissao = 20.00
valor_total_vendas = vendas_mes * valor_comissao

valor_salario_liquido = (salario_fixo + valor_total_vendas) - desconto

print(valor_salario_liquido)