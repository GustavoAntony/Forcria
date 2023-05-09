from JogoDeForca import JogoDeForca
import re
import random
import pandas as pd

class Jogador():
    def __init__(self, tamanho_palavra, content):
        self.acertos = {}
        self.erros = ""
        self.tamanho_palavra = tamanho_palavra
        self.dict_probabilidades_letra = {}
        self.regex = "^"+"[a-z]"*tamanho_palavra+"$"
        self.palavras_possiveis = list(map(str.lower, content))
        self.letras_tentadas = ""

    def atualiza_regex(self):
        lista = ["[a-z]" for i in range(self.tamanho_palavra)]
        for letra,indices in self.dict_acertos.items():
            for indice in indices:
                lista[indice] = letra
            self.regex = "^"+"".join(lista)+"$"
    
    def atualiza_regex(self):
        if self.erros == "":
            padrao = "[a-z]"
        else:
            padrao = "[^"+f"{self.letras_tentadas}"+"]"
        lista = [padrao for i in range(self.tamanho_palavra)]
        for letra,indices in self.acertos.items():
            for indice in indices:
                lista[indice] = letra
            self.regex = "^"+"".join(lista)+"$"

    def atualiza_base_de_palavras(self):
        p_finais = []
        regex = re.compile(self.regex)
        for palavra in self.palavras_possiveis:
            if regex.search(palavra):
                p_finais.append(palavra)
        # p_possiveis = [palavra for palavra in content if regex.search(palavra) == True]
        return p_finais
    
    def escolhe_melhor_jogada(self):
        melhor_letra = ""
        maior_valor = 0
        for letra in self.dict_probabilidades_letra:
            if self.dict_probabilidades_letra[letra] >= maior_valor and letra not in self.letras_tentadas:
                maior_valor = self.dict_probabilidades_letra[letra]
                melhor_letra = letra
        self.letras_tentadas += melhor_letra
        return melhor_letra
    
    def atualiza_dict_acertos(self, letra, lista_acertos):
        if lista_acertos != []:
            self.acertos[letra] = lista_acertos
        else:
            self.erros += letra
 
    def atualiza_probabilidades(self):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        dict = {letra : 0 for letra in alfabeto}
        for palavra in self.palavras_possiveis:
            letras_ja_adicionadas = ""
            for letra in palavra.lower():
                if letra not in letras_ja_adicionadas:
                    dict[letra] += 1
                    letras_ja_adicionadas += letra
        return dict
            
    def jogada(self, letra, lista_acertos):
        self.atualiza_dict_acertos(letra, lista_acertos)
        self.atualiza_regex()
        self.palavras_possiveis = self.atualiza_base_de_palavras()
        self.dict_probabilidades_letra = self.atualiza_probabilidades()
        return self.escolhe_melhor_jogada()

    


qtd_vitorias = 0
qtd_derrotas = 0
lista_derroatas = []
for i in range(100):
    jogo = JogoDeForca()
    tamanho_palavra = jogo.novo_jogo()
    # jogo.palavra = "falece"
    # tamanho_palavra = 6
    inicial = jogo.palavra
    print(inicial)
    jogador = Jogador(tamanho_palavra, jogo.content)
    letra = ""
    lista_acertos = []
    terminou = False
    while terminou == False and jogo.vidas >= 1:
        letra = jogador.jogada(letra,lista_acertos)
        if len(jogador.palavras_possiveis) == 1: 
            chute = jogador.palavras_possiveis[0]
            print(chute)
            terminou = True
            break
        else:
            if jogo.vidas == 1:
                chute = random.choice(jogador.palavras_possiveis)
                print(chute)
                terminou = True
            else:
                lista_acertos = jogo.tentar_letra(letra)
    # print(chute)
    # print(inicial)
    if chute == inicial:
        qtd_vitorias += 1
    else:
        qtd_derrotas += 1
        lista_derroatas.append(chute)
    
print(f"qtd vitorias: {qtd_vitorias}")
print(f"qtd derrotas: {qtd_derrotas}")
print(lista_derroatas)

dict = {"erros":lista_derroatas }
df = pd.DataFrame(dict)
df.to_csv("erros3.csv")
