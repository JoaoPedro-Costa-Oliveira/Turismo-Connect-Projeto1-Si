import pandas as pd  # importando a biblioteca pandas, que ira subistitiuir o dicionario, usando como dataframe
import os # importando a biblioteca OS, servindo como ponte entre o codigo e o sistema operacional
from dotenv import load_dotenv # importando a função load.dotenv, que ira carregar o arquivo .dotenv

load_dotenv()

class EstabelicimentoComerciais: # criando uma classe para estabelecimentos comerciais e atribuindo funcoes nela

    def __init__(self): # função incial, com o paramento self para poder buscar em outra funcoes

        self.diretorio = os.getenv("path_directory") # criando uma variavel diretorio com o self. para buscar em outros lugares
        # a variavel recebe os.getenv, vai buscar o path directory, que é o caminho da pasta
        self.arquivo_csv = os.path.join(self.diretorio, "Estabelecimentos_comerciais.csv")
        # criando uma variavel arquivo_csv com o self. para buscar em outros lugares
        # vai usar a biblioteca os usando .path e .join, que vai entrar no diretorio e crir outro caminho com o Pontos_Turisricos.csv
        
        if os.path.exists(self.arquivo_csv):    
            self._estabelecimentos_comerciais = pd.read_csv(self.arquivo_csv)
            # se o caminho exite do self.arquivo_csv, ele vai ler o arquivo csv

        else:
            
            self._colunas = ["ID", "Nome", "Tipo", "Endereço", "Descrição", "Horário de funcionamento", "Média das avaliações"]
            self._estabelecimentos_comerciais = pd.DataFrame(columns= self._colunas)
            # se ele não existir ele vai criar um data frame com as colunas, ID ,Nome ,Tipo ,Endereço ,Descrição,Horários de funcionamento,Média das avaliações


    def criar_arquivo_csv(self):
         # função criar arquivo csv, com o paramento self para poder buscar em outra funcoes

        try:
            # vai tentar criar o arquivo se o caminho do diretorio nao existir
            if not os.path.exists(self.diretorio): 
                os.makedirs(self.diretorio)

            self.salvar_aquivo_em_csv()
            print(f"Arquivo CSV criado com sucesso em {self.arquivo_csv}")
            # puxou a função salvar arquivo e criou o arquivo e o caminho
            # pinta que teve sucesso criar o arquivo
            
        except Exception as exc:
             # se o caminho existir e da algum erro ele avisa se que não conseguiu
            print(f"Não foi possível criar o arquivo CSV: {exc}")

        finally:
            # se existir ele vai entrar

            pass

    def salvar_aquivo_em_csv(self):
        # criando uma função salvar arquivo para com o self, servindo como parametro para poder puxar ela em outros lugares

        self._estabelecimentos_comerciais.to_csv(self.arquivo_csv, sep= ",", index=False, encoding="utf-8")
         # vai puxar o data frame dos pontos turisticos com as colunas e mandar pro csv, ignorando o index e separando por virgulas   

    def cadastrar_novo_estabelecimento_comercial(self, nome, tipo, endereco, descricao, horario_de_funcionamento, medio_de_avaliacoes):
        # criar a função de cadastro usando o parametro da variavel nome, tipo, endereco, descricao, horario_de_funcionamento, media_de_avaliacoes
        novo_estabelecimento_comercial = pd.DataFrame ({
            "ID" : [self._estabelecimentos_comerciais["ID"].iloc[-1] + 1 if not self._estabelecimentos_comerciais.empty else 1],
            # vai localizar o numero do id e adicionar mais 1 depois da ultima posição, e se ele estiver vazio vai começar com 1
            "Nome" : nome, #criando variavel que vai receber a coluna
            "Tipo" : tipo,
            "Endereço" : endereco,
            "Descrição" : descricao,
            "Horário de funcionamento": horario_de_funcionamento,
            "Média das avaliações" : medio_de_avaliacoes
        })

        self._estabelecimentos_comerciais = pd.concat([self._estabelecimentos_comerciais, novo_estabelecimento_comercial], ignore_index= True)
        self.salvar_aquivo_em_csv()
        # vai pegar o self estabelecimentos comerciais e juntar com o novo estabelecimento comercial e ignorar o index
        # printa que foi cadastrado com sucesso
        print("Estabelecimento comercial cadastrado com sucesso!")

    def listar_estabelicimento_comerciais_cadastrados(self):
        # função de listar com o self, servindo como parametro para poder puxar ela em outros lugares

        if self._estabelecimentos_comerciais.empty:
            # se a lista estiver vazia vai printar falando que nao tem nenhum estabelecimento comercial
            print("Nenhum estabelecimento comercial cadastrado")

        else:
            
            pd.set_option('colheader_justify', 'center')
            print(self._estabelecimentos_comerciais.to_string(index= False))
            # pd set optition, vai deixar as colunas da lista centralizadas
            # vai printar todos os estabelecimentos comercias e ignorar o index propio  

    def editar_informacao_estabelicimento_comercial(self, id_estabelecimento_comercial, campo_de_alteracao, nova_informacao):
        # função de editar a informação
        if id_estabelecimento_comercial not in  self._estabelecimentos_comerciais["ID"].values:
            print("ID do ponto comercial não foi encontrado!")
            # se não existir nenhum ponto turistico vai printar falndo que não encontrou

        else:

            self._estabelecimentos_comerciais.loc[self._estabelecimentos_comerciais["ID"] == id_estabelecimento_comercial, campo_de_alteracao] = nova_informacao
            self.salvar_aquivo_em_csv()
            print(f"A informação {campo_de_alteracao} do estabelicimento comercial de id {id_estabelecimento_comercial} foi alterado com sucesso!")
            # senão vai localizar o id , e vai alterar o campo de alteração criando uma nova informação
            # vai salvar o arquivo 
            # vai printar que deu certo a alteração

    def deletar_estabelicimento_comerciais(self, id_estabelecimento_comercial):
        # criando função de deletar estabelecimento comercial, e vai puxar variavel id
        if id_estabelecimento_comercial not in self._estabelecimentos_comerciais["ID"].values:
            print("ID do establecimento comercial não encontrado!")
            # se o id nao estiver no pontos turisticos, vai falar que não encontrou

        else:

            self._estabelecimentos_comerciais = self._estabelecimentos_comerciais[self._estabelecimentos_comerciais["ID"] != id_estabelecimento_comercial]
            self.salvar_aquivo_em_csv()
            # senão vai buscar o todos os ids diferentes do que foi selecionado e vai salvar, o id que foi selecionado vai ser exlcuido (nao vai salvar)