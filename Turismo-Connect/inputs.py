class Inputs: 
    def escolha_menu_de_opcao(self):
        
        while True:
            
            try:
                self.escolha_menu = int(input("Informe a opção desejada: "))
                break
            
            except ValueError as value:
                print(f"Digite um número inteiro")

    def cadastrar_ponto_turistico(self):   
        
        while True:
            try: 
        
                self.nome_ponto_turistico = input("Insira o nome do ponto turístico: ")
                self.endereco_ponto_turistico = input("Insira o endereço do ponto turístico: ")
                self.descricao_ponto_turistico = input("Insira a descrição do ponto turístico: ")
                self.horario_funcionamento_ponto_turistico = input("Insira os horários de funcionamento do ponto turístico: ")
                self.media_avaliacao_ponto_turistico = float(input("Insira a médida das avaliações do ponto turístico: "))
                break
            except ValueError:
        
                print("Digite um valor válido!")


        
    def editar_ponto_turistico(self):
        while True:
            try:
                self.id_ponto_turistico = int(input("Informe o ID do ponto turístico que deseja alterar: "))
                self.id_coluna_para_alterar = int(input("Informe o número de qual coluna deseja alterar: " ))
                self.nova_informacao = input("Insira a nova alteração: ")
                break
        
            except ValueError:
        
                print("Digite um número inteiro")

    def excluir_id(self):
        while True:
            try:
                self.id_excluir = int(input("Informe o ID que deseja excluir: "))
                break
        
            except ValueError:
        
                print("Digite um número inteiro")

    def inputs_cadastrar_usuario(self):
        
        
        while True:
        
            try:    
        
                self.nome_usuario = input("Insira o seu nome: ")
                self.cpf_usuario = input("Insira o seu CPF: ")
                self.idade_usuario = int(input("Insira a sua idade: "))
                self.email_usuario = input("Insira o seu email: ")
                self.telefone_usuario = input("Insira o seu telefone: ")
                self.endereco_usuario = input("Insira o endereço: ")
                break
        
            except ValueError:
        
                print("Informe número inteiro no campo idade")

    def inputs_editar_usuario(self):
        while True:
        
            try:
                self.id_usuario = int(input("Informe o ID do usuário que deseja alterar: "))
                self.id_coluna_para_alterar = int(input("Informe o número de qual coluna deseja alterar: " ))
                self.nova_informacao = input("Insira a nova alteração: ")
                break
        
            except ValueError:
        
                print("Informe um número inteiro no campo ID usuário")

    def inputs_cadastrar_estabelecimento_comercial(self):
        
        while True:
        
            try: 
        
                self.nome_estabelecimento_comercial = input("Insira o nome do estabelecimento comercial: ")
                self.tipo_estabelecimento_comercial = input("Insira o tipo de estabelecimento comercial: ")
                self.endereco_estabelecimento_comercial = input("Insira o endereço do estabelecimento comercial: ")
                self.descricao_estabelecimento_comercial = input("Insira a descrição do estabelecimento comercial: ")
                self.horario_funcionamento_estabelecimento_comercial = input("Insira os horários de funcionamento do estabelecimento comercial: ")
                self.media_avaliacao_estabelecimento_comercial = float(input("Insira a médida das avaliações do estabelecimento comercial: "))
                break
            
            except ValueError:
        
                print("Digite um valor válido!")

    def inputs_editar_estabelecimento_comercial(self):
        while True:
        
            try:
        
                self.id_estabelecimento_comercial = int(input("Informe o ID do estabelecimento comercial que deseja alterar: "))
                self.id_coluna_para_alterar = int(input("Informe o número de qual coluna deseja alterar: " ))
                self.nova_informacao = input("Insira a nova alteração: ")
                break
        
            except ValueError:
                
                print("Informe um número inteiro no campo ID estabelecimento comercial")
