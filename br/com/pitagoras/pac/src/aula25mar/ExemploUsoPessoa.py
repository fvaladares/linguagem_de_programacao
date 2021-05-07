from br.com.pitagoras.pac.src.aula25mar.Person import Person

if __name__ == '__main__':
    person = Person(nome='Fabricio Valadares', idade=39)
    print(person)
    print(f'Salario de {person.nome}: R$ {(person.calcular_pagamento(10)):.2f}')
    if person.eh_adolescente():
        print(f'{person.nome} eh adolescente')
    else:
        print(f'{person.nome} está velho')
