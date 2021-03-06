import pandas as pd


def primeira_parte():
    nomes = ("Fabricio Marcos Túlio Carlos".split())
    # print(f'Tipo de dado {type(nomes)}')
    telefones = [31993576193, 12349876, 1234, 98765]
    agenda = pd.Series(data=nomes, index=telefones)
    agenda.name = 'Nomes'
    print(f'Exemplo de Pandas Series\n{agenda}')
    print(f'Saída: agenda.loc[12349876]\n{agenda.loc[31993576193]}')

    print(f'Nome da Serie: {agenda.name}')

    print('*' * 30)
    novos_dados = pd.Series(data=[14.5, 15, 14, None, 13.8])
    print(f'Linhas {novos_dados.shape}')
    print(f'Tipos de dados {novos_dados.dtypes}')
    print(f'Resumo {novos_dados.describe()}')
    print(f'Valores nulos {novos_dados.hasnans}')
    print(f'Média {novos_dados.mean()}')

    idades = [39, 25, 22, 21]
    dados = list(zip(nomes, telefones, idades))
    print(f'Dados: {dados}')
    meu_data_frame = pd.DataFrame(data=dados, columns=['nome', 'telefone', 'idade'])
    print(f'Dataframe: \n{meu_data_frame}')
    print(f'Idade média: \n{meu_data_frame["idade"].mean()}')
    print(f'Resumo dos dados (dataframe) \n{meu_data_frame.describe()}')


def segunda_parte():
    dataset = pd.read_csv("/home/fabricio/Documents/Lecture/code/cursos-prouni.csv.csv")
    # print(dataset)
    print(dataset.info())
    print(f"Shape: \n{dataset.shape}")
    print('-' * 20)
    print(f"Mean: \n{dataset.mean()}")
    print('-' * 20)
    print(dataset.describe())
    print('-' * 20)
    print('-' * 50)
    print(dataset['mensalidade'].mean())


if __name__ == '__main__':
    # primeira_parte()
    segunda_parte()
