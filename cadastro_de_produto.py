#!/usr/bin/env python3 
"""Cadastro de produto"""

__version__ = "0.1.0"

produto = {
    "nome": "Caneta",
    "cores":["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,    
}

compra = ("Fábio", produto["nome"], 3)

cliente = {
    "nome": "Fábio"
}
compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
    
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']} comprou {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
) 