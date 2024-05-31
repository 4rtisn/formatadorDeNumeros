def formatar_telefone(telefone):
    telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    telefone_formatado = "55" + telefone
    return telefone_formatado

with open('numeros.txt', 'r') as arquivo_entrada:
    telefones = arquivo_entrada.readlines()

telefones_formatados = [formatar_telefone(telefone.strip()) for telefone in telefones]

with open('numeros_tratados.txt', 'w') as arquivo_saida:
    for telefone in telefones_formatados:
        arquivo_saida.write(telefone + '\n')

print("Números formatados foram salvos em 'numeros_tratados.txt'.")