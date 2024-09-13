import pandas as pd  
import os 
from dotenv import load_dotenv 

load_dotenv()

class EstabelicimentoComerciais:

    def __init__(self): 

        self.diretorio = os.getenv("path_directory") 
        self.arquivo_csv = os.path.join(self.diretorio, "Estabelecimentos_comerciais.csv")
        
        if os.path.exists(self.arquivo_csv):    
            self._estabelecimentos_comerciais = pd.read_csv(self.arquivo_csv)
            
        else:
            
            self._colunas = ["ID", "Nome", "Tipo", "Endereço", "Descrição", "Horário de funcionamento", "Média das avaliações"]
            self._estabelecimentos_comerciais = pd.DataFrame(columns= self._colunas)
            

    def criar_arquivo_csv(self):
         
        try:
            if not os.path.exists(self.diretorio): 
                os.makedirs(self.diretorio)

            self.salvar_aquivo_em_csv()
            print(f"Arquivo CSV criado com sucesso em {self.arquivo_csv}")
            
        except Exception as exc:
            print(f"Não foi possível criar o arquivo CSV: {exc}")

        finally:
            
            pass

    def salvar_aquivo_em_csv(self):
        
        self._estabelecimentos_comerciais.to_csv(self.arquivo_csv, sep= ",", index=False, encoding="utf-8")
        
    def cadastrar_novo_estabelecimento_comercial(self, nome, tipo, endereco, descricao, horario_de_funcionamento, medio_de_avaliacoes):
        novo_estabelecimento_comercial = pd.DataFrame ({
            "ID" : [self._estabelecimentos_comerciais["ID"].iloc[-1] + 1 if not self._estabelecimentos_comerciais.empty else 1],
            "Nome" : nome,
            "Tipo" : tipo,
            "Endereço" : endereco,
            "Descrição" : descricao,
            "Horário de funcionamento": horario_de_funcionamento,
            "Média das avaliações" : medio_de_avaliacoes
        })

        self._estabelecimentos_comerciais = pd.concat([self._estabelecimentos_comerciais, novo_estabelecimento_comercial], ignore_index= True)
        self.salvar_aquivo_em_csv()
        print("Estabelecimento comercial cadastrado com sucesso!")

    def listar_estabelicimento_comerciais_cadastrados(self):

        if self._estabelecimentos_comerciais.empty:
            print("Nenhum estabelecimento comercial cadastrado")

        else:
            
            pd.set_option('colheader_justify', 'center')
            print(self._estabelecimentos_comerciais.to_string(index= False))
            
    def editar_informacao_estabelicimento_comercial(self, id_estabelecimento_comercial, campo_de_alteracao, nova_informacao):
        if id_estabelecimento_comercial not in  self._estabelecimentos_comerciais["ID"].values:
            print("ID do ponto comercial não foi encontrado!")
            
        else:

            self._estabelecimentos_comerciais.loc[self._estabelecimentos_comerciais["ID"] == id_estabelecimento_comercial, campo_de_alteracao] = nova_informacao
            self.salvar_aquivo_em_csv()
            print(f"A informação {campo_de_alteracao} do estabelicimento comercial de id {id_estabelecimento_comercial} foi alterado com sucesso!")
            
    def deletar_estabelicimento_comerciais(self, id_estabelecimento_comercial):
        if id_estabelecimento_comercial not in self._estabelecimentos_comerciais["ID"].values:
            print("ID do establecimento comercial não encontrado!")
            
        else:

            self._estabelecimentos_comerciais = self._estabelecimentos_comerciais[self._estabelecimentos_comerciais["ID"] != id_estabelecimento_comercial]
            self.salvar_aquivo_em_csv()
            
