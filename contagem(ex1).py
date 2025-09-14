def contar_palavras():
    texto = input("Digite um texto (mínimo 3 palavras): ").strip()
    
    if not texto:
        print("Nenhum texto foi digitado!")
        return
    
    palavras = texto.split()
    
    if len(palavras) < 3:
        print("Digite pelo menos 3 palavras!")
        return
    
    print(f"\nTotal de palavras: {len(palavras)}")
    
    mais_longa = max(palavras, key=len)
    print(f"Palavra mais longa: '{mais_longa}' ({len(mais_longa)} letras)")
    
    contagem = {}
    for palavra in palavras:
        palavra_limpa = palavra.strip('.,!?;:').lower()
        if palavra_limpa:
            contagem[palavra_limpa] = contagem.get(palavra_limpa, 0) + 1
    
    mais_comum = max(contagem, key=contagem.get)
    print(f"Palavra mais comum: '{mais_comum}' ({contagem[mais_comum]} vezes)")

if __name__ == "__main__":
    contar_palavras()
