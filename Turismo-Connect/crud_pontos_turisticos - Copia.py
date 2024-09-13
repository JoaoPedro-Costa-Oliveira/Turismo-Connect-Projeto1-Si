import pandas as pd # importando a biblioteca pandas, que ira subistitiuir o dicionario, usando como dataframe
import os # importando a biblioteca OS, servindo como ponte entre o codigo e o sistema operacional
from dotenv import load_dotenv # importando a função load.dotenv, que ira carregar o arquivo .dotenv

load_dotenv()
class PontosTuristicos: # criando uma classe para pontos turisisticos e atribuindo funcoes nela

    def __init__(self): # função incial, com o parametro self para poder buscar em outra funcoes

        self.diretorio = os.getenv("path_directory") # criando uma variavel diretorio com o self. para buscar em outros lugares
        # a variavel recebe os.getenv, vai buscar o path directory, que é o caminho da pasta
        self.arquivo_csv = os.path.join(self.diretorio, "Pontos_turisticos.csv") 
        # criando uma variavel arquivo_csv com o self. para buscar em outros lugares
        # vai usar a biblioteca os usando .path e .join, que vai entrar no diretorio e crir outro caminho com o Pontos_Turisricos.csv
        

        if os.path.exists(self.arquivo_csv):
            self._pontos_turisticos = pd.read_csv(self.arquivo_csv)
            # se o caminho exite do self.arquivo_csv, ele vai ler o arquivo csv

        else:
            self._colunas = ["ID", "Nome", "Endereço", "Descrição", "Horários de funcionamento", "Média das avaliações"]
            self._pontos_turisticos = pd.DataFrame(columns=self._colunas)
            # se ele não existir ele vai criar um data frame com as colunas, ID,Nome,Endereço,Descrição,Horários de funcionamento,Média das avaliações

    def criar_arquivo_csv(self):
       # função criar arquivo csv, com o paramento self para poder buscar em outra funcoes
        try:
            # vai tentar criar o arquivo se o caminho do diretorio nao existir
            if not os.path.exists(self.diretorio):
                os.makedirs(self.diretorio)

            self.salvar_arquivo_em_csv()
            print(f"Arquivo CSV criado com sucesso em {self.arquivo_csv}!")
            # puxou a função salvar arquivo e criou o arquivo e o caminho
            # pinta que teve sucesso criar o arquivo
            
        except Exception as exc:
            # se o caminho existir e da algum erro ele avisa se que não conseguiu
            print(f'Não foi possível criar o arquivo CSV: {exc}')
        
        finally: # e se existir ele vai entrar

            pass

    def salvar_arquivo_em_csv(self):
        # criando uma função salvar arquivo para com o self, servindo como parametro para poder puxar ela em outros lugares

        self._pontos_turisticos.to_csv(self.arquivo_csv, sep=',', index=False, encoding='utf-8')
         # vai puxar o data frame dos pontos turisticos com as colunas e mandar pro csv, ignorando o index e separando por virgulas 

    def cadastrar_ponto_turistico(self, nome, endereco, descricao, horario_de_funcionamento, media_de_avaliacoes):
        # criar a função de cadastro usando o parametro da variavel nome, endereco, descricao, horario_de_funcionamento, media_de_avaliacoes
        novo_ponto_turistico = pd.DataFrame({ #o novo ponto turistico vai virar data frame (dicionario)
            'ID': [self._pontos_turisticos["ID"].iloc[-1] + 1 if not self._pontos_turisticos.empty else 1], 
            # vai localizar o numero do id e adicionar mais 1 depois da ultima posição, e se ele estiver vazio vai começar com 1
            'Nome': nome, # varivael recebe 
            'Endereço': endereco,
            'Descrição': descricao,
            'Horários de funcionamento': horario_de_funcionamento,
            'Média das avaliações': media_de_avaliacoes
        })

        self._pontos_turisticos = pd.concat([self._pontos_turisticos, novo_ponto_turistico], ignore_index=True)
        self.salvar_arquivo_em_csv()
        # vai pegar o self pontos turisticos e juntar com o novo ponto turistico e ignorar o index
        # printa que foi cadastrado com sucesso 
        print("Ponto cadastrado com sucesso!")

    def listar_pontos_turisticos_cadastrados(self):
                
                if self._pontos_turisticos.empty:
                    # se a lista estiver vazia vai printar falando que nao tem nenhum ponto turistico
                    print("Nenhum ponto turístico cadastrado")
                else: 
                    pd.set_option('colheader_justify', 'center')
                    print(self._pontos_turisticos.to_string(index= False)) 
                    # pd set optition, vai deixar as colunas da lista centralizadas
                    # vai printar todos os pontos turisticos e ignorar o index  

    def editar_informacao_ponto_turistico(self, id_ponto_turistico, campo_de_alteracao, nova_informacao):
         # função de editar a informação
        if id_ponto_turistico not in self._pontos_turisticos['ID'].values:
            print("ID do ponto turístico não encontrado.")
            # se não existir nenhum ponto turistico vai printar falndo que não encontrou 
        
        else:
            self._pontos_turisticos.loc[self._pontos_turisticos["ID"] == id_ponto_turistico, campo_de_alteracao] = nova_informacao
            self.salvar_arquivo_em_csv()
            print(f"A informacao {campo_de_alteracao} do ponto turístico de id {id_ponto_turistico} foi alterada com sucesso!")
            # vai localizar o id , e vai alterar o campo de alteração criando uma nova informação
            # vai salvar o arquivo 
            # vai printar que deu certo a alteração

    def deletar_ponto_turistico(self, id_ponto_turistico):
        # criando função de deletar ponto turistico, e vai puxar variavel id 

        if id_ponto_turistico not in self._pontos_turisticos['ID'].values:
            print("ID do ponto turístico não encontrado.")
            # se o id nao estiver no pontos turisticos, vai falar que não encontrou

        self._pontos_turisticos= self._pontos_turisticos[self._pontos_turisticos["ID"] != id_ponto_turistico]
        self.salvar_arquivo_em_csv()
          # vai buscar o todos os ids diferentes do que foi selecionado e vai salvar, o id que foi selecionado vai ser exlcuido (nao vai salvar) 
