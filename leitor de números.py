número = int(input('Digite um número inteiro positivo menor que 1000: '))

if número >= 1000:
    print("Número invalido, digite um número entre 0 e 999.")
else:
    unidade = número % 10 #encontrando a unidade
    número = (número - unidade)/10 #excluindo a unidade do número
    dezena = número % 10 #encontrando as dezenas
    número = (número - dezena)/10 #excluindo a dezena do número 
    centena = número % 10 #encontrando a centena

#tranformando os número em inteiros
unidade = int(unidade)
dezena = int(dezena)
centena = int(centena)

#função if sendo usada para diferenciar plural e singular.
if unidade == 1:
    print("O número possui: ",centena,"centenas,",dezena,"dezenas e",unidade,"unidade")
elif dezena == 1:
    print("O número possui: ",centena,"centenas,",dezena,"dezena e",unidade,"unidades")
elif centena == 1:
    print("O número possui: ",centena,"centena,",dezena,"dezenas e",unidade,"unidades")
elif unidade == 1 and dezena == 1:
    print("O número possui: ",centena,"centenas,",dezena,"dezena e",unidade,"unidade")
elif unidade == 1 and centena == 1:
    print("O número possui: ",centena,"centena,",dezena,"dezenas e",unidade,"unidade")
elif unidade == 1 and dezena ==1 and centena == 1:
    print("O número possui: ",centena,"centena,",dezena,"dezena e",unidade,"unidade")
elif dezena == 1 and centena == 1:
    print("O número possui: ",centena,"centena,",dezena,"dezena e",unidade,"unidades")
else:
    print("O número possui: ",centena,"centenas,",dezena,"dezenas e",unidade,"unidades")