class EstruturaMenu():
    
    @staticmethod
    
    def menu_principal():
        print("""
            ----------------------------------
            SEJA BEM VINDO AO NOSSO SISTEMA!
            ----------------------------------
            Escolha uma opção para ter acesso
            ao nosso conteúdo. DIVIRTA-SE!
            ----------------------------------
            1 - Acessar Pontos Turísticos
            2 - Acessar Usuários
            3 - Acessar Estabelecimentos
                Comerciais
            4 - Sair 
            ----------------------------------
            """
        )
        
    @staticmethod
    
    def menu_pontos_turisticos():
        print(
                    """
                    ------------------------------
                    CRUD PONTOS TURÍSTICOS
                    ------------------------------
                    1 - Cadastrar ponto turístico
                    2 - Editar ponto turístico
                    3 - Deletar ponto turístico
                    4 - Listar ponto(s) turístico(s)
                    5 - Sair
                    ------------------------------
                    """
            )
    
    @staticmethod 
    
    def menu_edicao_ponto_turistico():
        print(
                """
                    ------------------------------
                    CAMPO DE AlTERAÇÃO
                    ------------------------------
                    1 - Nome
                    2 - Endereço
                    3 - Descrição
                    4 - Horários de funcionamento
                    5 - Média das avaliações
                    ------------------------------

                """
        )
        
    @staticmethod
    
    def menu_usuarios():
        print(
                    """
                    ------------------------------
                    CRUD USUÁRIOS
                    ------------------------------
                    1 - Cadastrar usuário
                    2 - Editar usuário
                    3 - Deletar usuário
                    4 - Listar usuário(s)
                    5 - Sair
                    ------------------------------
                    """
            )
        
    @staticmethod
    
    def menu_edicao_usuario():
        print(
                """
                    ------------------------------
                    CAMPO DE AlTERAÇÃO
                    ------------------------------
                    1 - Nome
                    2 - Cpf
                    3 - Idade
                    4 - Email
                    5 - Telefone
                    6 - Endereço
                    ------------------------------

                """
        )
    
    @staticmethod
    
    def menu_estabelecimentos_comerciais():
        print(
                    """
                    ------------------------------
                    CRUD ESTABELECIMENTOS 
                    COMERCIAIS (E.C)
                    ------------------------------
                    1 - Cadastrar E.C
                    2 - Editar E.C
                    3 - Deletar E.C
                    4 - Listar E.C(s)
                    5 - Sair
                    ------------------------------
                    """
            )
    
        
    @staticmethod
    
    def menu_edicao_estabelecimentos_comerciais():
        print(
                """
                    ------------------------------
                    CAMPO DE ALTERAÇÃO
                    ------------------------------
                    1 - Nome
                    2 - Tipo
                    3 - Endereço
                    4 - Descrição
                    5 - Horários de funcionamento
                    6 - Média das avaliações
                    ------------------------------

                """
        )
    
