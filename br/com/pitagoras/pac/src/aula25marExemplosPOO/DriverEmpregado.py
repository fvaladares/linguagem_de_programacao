from br.com.pitagoras.pac.src.aula25marExemplosPOO.Empregado import Empregado
from br.com.pitagoras.pac.src.aula25marExemplosPOO.Pessoa import Pessoa
from br.com.pitagoras.pac.src.aula25marExemplosPOO.VendedorViajante import VendedorViajante

if __name__ == '__main__':
    print('Pessoa')
    p = Pessoa(nome='Fabricio Valadares', idade=39)
    print(p)
    print('-' * 50)

    print('Empregado')
    e = Empregado(nome='Fulano de Tal', idade=25, id='001')
    e.fazer_aniversario()
    print(e)
    print(f'Salario: R${e.calcular_pagamento(40):.2f}')
    print('-' * 50)

    print("Caixeiro viajante")
    v = VendedorViajante(nome='Senhor Vendedor', idade=60, id="4823", vendas=5_000, regiao='Sudeste')
    v.fazer_aniversario()
    pagamento = v.calcular_pagamento(horas_trabalhadas=60) + v.bonus()
    print(f"Pagamento com bônus: R$ {pagamento:.2f}")
    print(v)
