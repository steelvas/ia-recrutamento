"""Simulação de interface: clique formal não demonstra revisão humana."""

def triagem(pontos, clique):
    sugestao = "eliminar" if pontos < 70 else "avançar"
    if clique == "confirmar":
        return sugestao
    return "pendente"

print(triagem(69, "confirmar"))  # eliminar
print(triagem(69, "revisar"))    # pendente
