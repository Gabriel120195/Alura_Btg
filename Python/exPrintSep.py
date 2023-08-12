# print("Brasil ganhou 5 titulos mundiais")
# print("Brasil", "ganhou", 5, "titulos mundiais", sep="")
# print("Brasil", "ganhou", 5, "titulos mundiais", sep=" ")
# print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")
#
# dia = 12
# mes = 1
# ano = 1995
#
# print(dia, mes, ano, sep="/")
arquivo = open("palavras.txt", "r")
for linha in arquivo:
    print(linha)
