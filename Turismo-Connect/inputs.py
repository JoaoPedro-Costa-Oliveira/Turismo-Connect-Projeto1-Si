class Inputs: # criando classe de inputs para o codigo ficar mais limpo

    def escolha_menu_de_opcao(self):
        # definindo função de escolher o menu e atribuindo o self como parametro para poder buscar em outros lugares ou em outras funções
    
        while True:
            # enquanto a condição for verdadeira vai ficar em loop
            
            try:
                # vai tentar escolher uma informação valida
                # se a opção que o usuario digitar for valida vai quebrar o loop 
                self.escolha_menu = int(input("Informe a opção desejada: "))
                break
            
            except ValueError as value:
                #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal
                print(f"Digite um número inteiro")

    def cadastrar_ponto_turistico(self):   
        # função de cadastrar ponto turistico com o self para usar como parametro e buscar ela em outras funções e lugares

        while True:
            # enquanto a condição for verdadeira vai ficar em loop
            try: 
                # vai tentar o dar input em todas a informações de cadastro

                self.nome_ponto_turistico = input("Insira o nome do ponto turístico: ")
                self.endereco_ponto_turistico = input("Insira o endereço do ponto turístico: ")
                self.descricao_ponto_turistico = input("Insira a descrição do ponto turístico: ")
                self.horario_funcionamento_ponto_turistico = input("Insira os horários de funcionamento do ponto turístico: ")
                self.media_avaliacao_ponto_turistico = float(input("Insira a médida das avaliações do ponto turístico: "))
                break
                # se o usuario digitar tudo certo vai acabar o loop
            except ValueError:
                 #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal

                print("Digite um valor válido!")


        
    def editar_ponto_turistico(self):
        # função editar ponto com parametro self para poder buscar em outras funções e lugares
        while True:
            # enquanto a condição for verdadeira vai ficar em loop
            try:
                # vai tentar da input nas informações de editar
                self.id_ponto_turistico = int(input("Informe o ID do ponto turístico que deseja alterar: "))
                self.id_coluna_para_alterar = int(input("Informe o número de qual coluna deseja alterar: " ))
                self.nova_informacao = input("Insira a nova alteração: ")
                break
                # se o usuario digitar tudo certo vai acabar o loop

            except ValueError:
                 #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal

                print("Digite um número inteiro")

    def excluir_id(self):
        # função de excluir id usando o self para usar como parametro para buscar em outras funções e lugares
        while True:
             # enquanto a condição for verdadeira vai ficar em loop
            try:
                # vai tentar dar input no id que foi digitado
                self.id_excluir = int(input("Informe o ID que deseja excluir: "))
                break
                 # se o usuario digitar tudo certo vai acabar o loop

            except ValueError:
                 #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal

                print("Digite um número inteiro")

    def inputs_cadastrar_usuario(self):
        # definindo função de cadastrar usuario usando o self como parametro para buscar em outros lugares e funções

        
        while True:
            # enquanto a condição for verdadeira vai ficar em loop

            try:    
                # vai tentar dar input em todas essas variaves que foi digitado

                self.nome_usuario = input("Insira o seu nome: ")
                self.cpf_usuario = input("Insira o seu CPF: ")
                self.idade_usuario = int(input("Insira a sua idade: "))
                self.email_usuario = input("Insira o seu email: ")
                self.telefone_usuario = input("Insira o seu telefone: ")
                self.endereco_usuario = input("Insira o endereço: ")
                break
             # se o usuario digitar tudo certo vai acabar o loop

            except ValueError:
                 #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal

                print("Informe número inteiro no campo idade")

    def inputs_editar_usuario(self):
        # definindo função de editar usuario usando o self como parametro para buscar em outros lugares e funções
        while True:
            # enquanto a condição for verdadeira vai ficar em loop

            try:
                # vai tentar dar input em todas essas variaves que vai ser digitado 
                # vai informar o id para editar
                self.id_usuario = int(input("Informe o ID do usuário que deseja alterar: "))
                self.id_coluna_para_alterar = int(input("Informe o número de qual coluna deseja alterar: " ))
                self.nova_informacao = input("Insira a nova alteração: ")
                break
             # se o usuario digitar tudo certo vai acabar o loop

            except ValueError:
                 #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal

                print("Informe um número inteiro no campo ID usuário")

    def inputs_cadastrar_estabelecimento_comercial(self):
        # definindo função de cadastrar estabelecimento comercial usando o self como parametro para buscar em outros lugares e funções

        while True:
            # enquanto a condição for verdadeira vai ficar em loop

            try: 
                # vai tentar dar input em todas essas variaves de cadastro

                self.nome_estabelecimento_comercial = input("Insira o nome do estabelecimento comercial: ")
                self.tipo_estabelecimento_comercial = input("Insira o tipo de estabelecimento comercial: ")
                self.endereco_estabelecimento_comercial = input("Insira o endereço do estabelecimento comercial: ")
                self.descricao_estabelecimento_comercial = input("Insira a descrição do estabelecimento comercial: ")
                self.horario_funcionamento_estabelecimento_comercial = input("Insira os horários de funcionamento do estabelecimento comercial: ")
                self.media_avaliacao_estabelecimento_comercial = float(input("Insira a médida das avaliações do estabelecimento comercial: "))
                break
             # se o usuario digitar tudo certo vai acabar o loop
            
            except ValueError:
                 #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal

                print("Digite um valor válido!")

    def inputs_editar_estabelecimento_comercial(self):
        # definindo função de editar estabelecimento comercial usando o self como parametro para buscar em outros lugares e funções
        while True:
            # enquanto a condição for verdadeira vai ficar em loop

            try:
                # vai tentar dar input em todas as variaves de id

                self.id_estabelecimento_comercial = int(input("Informe o ID do estabelecimento comercial que deseja alterar: "))
                self.id_coluna_para_alterar = int(input("Informe o número de qual coluna deseja alterar: " ))
                self.nova_informacao = input("Insira a nova alteração: ")
                break
             # se o usuario digitar tudo certo vai acabar o loop

            except ValueError:
                 #  se o usuario digitar algo errado vai printar o erro, e vai voltar para o loop pro usuario digitar a opção certa
                # tratando o erro para o usuario saber o que errou
                # ao inves de aparececr um erro gigante no terminal
                
                print("Informe um número inteiro no campo ID estabelecimento comercial")