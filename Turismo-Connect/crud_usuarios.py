import pandas as pd  
import os 
from dotenv import load_dotenv 
load_dotenv()

class Usuarios: 
    def __init__(self): 
        self.diretorio = os.getenv("path_directory") 
        self.arquivo_csv = os.path.join(self.diretorio, "Usuarios.csv")
        
        if os.path.exists(self.arquivo_csv):
            self._usuarios = pd.read_csv(self.arquivo_csv)
            
        else:
            self._colunas = ["ID", "Nome", "CPF", "Idade", "Email", "Telefone", "Endereço"]
            self._usuarios = pd.DataFrame(columns= self._colunas)
            
    def criar_arquivo_csv(self):
        
        try:
            
            if not os.path.exists(self.diretorio):
                os.makedirs(self.diretorio)

            self.salvar_arquivo_em_csv()
            print(f"Arquivo CSV criado com sucesso em {self.arquivo_csv}")
            
        except Exception as exc:
            
            print(f"Não foi possível criar o arquivo CSV: {exc}")

        finally:
            
            pass

    def salvar_arquivo_em_csv(self):
        
        self._usuarios.to_csv(self.arquivo_csv, sep=",", index= False, encoding="utf-8")
        
    def cadatrar_usuario(self, nome, cpf, idade, email, telefone, endereco):
        
        novo_usario = pd.DataFrame({
            "ID": [self._usuarios["ID"].iloc[-1] + 1 if not self._usuarios.empty else 1], 
            "Nome" : nome, 
            "CPF" : cpf,
            "Idade" :idade,
            "Email" : email,
            "Telefone" : telefone,
            "Endereço" : endereco
        })

        self._usuarios = pd.concat([self._usuarios, novo_usario], ignore_index=True)
        self.salvar_arquivo_em_csv()
        print("Usuario cadastrado com sucesso")

    def listar_usuarios_cadastrados(self):
        
        if self._usuarios.empty:
            
            print("Nenhum usuário registrado! ")
        else:
            
            pd.set_option('colheader_justify', 'center')
            print(self._usuarios.to_string(index= False))
            
    def editar_informacao_usuario(self, id_usuario, campo_de_alteracao, nova_informacao):
        
        if id_usuario not in self._usuarios["ID"].values:
            print("ID do usuario não foi encontrado")
           
        else:

            self._usuarios.loc[self._usuarios["ID"] == id_usuario, campo_de_alteracao] = nova_informacao
            self.salvar_arquivo_em_csv()
            print(f"A informação {campo_de_alteracao} do usuario de id {id} foi alterada com sucesso!")
           
    def deletar_usuario(self, id_usuario):
        if id_usuario not in self._usuarios["ID"].values:
            print("ID do usuario não encontrado")
            
        else:
            
            self._usuarios = self._usuarios[self._usuarios["ID"] != id_usuario]
            self.salvar_arquivo_em_csv()
            
