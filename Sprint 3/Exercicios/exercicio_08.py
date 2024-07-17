palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

def palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

for palavra in palavras:
    if palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")


