def contar_letra_a(texto):
    count_a = texto.lower().count('a')
    
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes no texto infomado.")
    else:
        print("A letra 'a' não foi encontrada no texto informado.")

string = input("Digite um texto para ser lido e verificado: ")

contar_letra_a(string)
