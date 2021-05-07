from br.com.pitagoras.pac.src.aula25mar.Pessoa import Pessoa

if __name__ == '__main__':
    person = Pessoa(nome='Fabricio Valadares', idade=39)
    print(person)
    # print(f'Salario de {person.nome}: R$ {(person.calcular_pagamento(10)):.2f}')
    if person.eh_adolescente():
        print(f'{person.nome} eh adolescente')
    else:
        print(f'{person.nome} está velho')

    print('*' * 50)
    print(f'Quantidade de pessoas criadas: {Pessoa.contandor_de_instancia}')
    person = Pessoa(nome='Miguel Valadares', idade=7)
    person = Pessoa(nome='Miguel Valadares', idade=7)
    person = Pessoa(nome='Miguel Valadares', idade=7)
    person = Pessoa(nome='Miguel Valadares', idade=7)

    print(f'Quantidade de pessoas criadas: {Pessoa.contandor_de_instancia}')

    Pessoa.incrementar_contador_instancia()
    Pessoa.incrementar_contador_instancia()
    Pessoa.incrementar_contador_instancia()
    Pessoa.incrementar_contador_instancia()
    print(f'Quantidade de pessoas criadas (contando uma chamada ao método de classe): {Pessoa.contandor_de_instancia}')
    print('*' * 50)
    Pessoa.metodo_estatico()
