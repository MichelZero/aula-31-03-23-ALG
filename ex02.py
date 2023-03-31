
# autores:
# Michel
# Cristiano

# data: 31/03/2023

# 5.	Desenvolva um programa em linguagem Python 
# que recebe do usuário o preço de um produto e 
# um valor de desconto. Com estas informações,
# o programa deve exibir o preço do produto com desconto. 
# Observações: O valor do desconto deve ser informado 
# entre 1 (100%) e 0 (0%). 
# Assim, 0.5 corresponde a um desconto de 50%. 
# Neste momento, considere que sempre 
# serão informados valores válidos pelo usuário.

# entrada
preco = 10
# 0.1 -> 10% -> 10/100
# 0.2 -> 20% -> 20/100
# 0.21 -> 21% -> 21/100
# 0.03 -> 3% -> 3/100
desconto = 0.1 # 0.1 -> 10% -> 10/100

# processamento
valor_desconto = preco * desconto
valor_final = preco - valor_desconto
# valor_final = preco - (preco * desconto)

# saída
print(f"valor original do produto: {preco}")
print(f"valor do desconto: {valor_desconto}")
print(f"o valor final é: {valor_final}")
print("fim do programa...")
