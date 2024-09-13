class EstruturaMenu():
    #classe atribuindo funções e caracteristica, com o nome estrutra menu

    @staticmethod
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
     # vai atribuir uma função nela

    def menu_principal():
        # definiu a função como menu principal, todas vez que chamar ela vai aparecer isso
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
        # printou menu principal e o que da para fazer
        
    @staticmethod
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
    # vai atribuir uma função nela

    def menu_pontos_turisticos():
        # definiu a função como menu do crud pontos turisticos, todas vez que chamar ela vai aparecer isso
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
        #printou o menu do crud e o que da para fazer nele

    @staticmethod 
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
    # vai atribuir uma função nela

    def menu_edicao_ponto_turistico():
       # definiu a função como menu do de editar no crud pontos turisticos, todas vez que chamar ela vai aparecer isso
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
        #printou o campo de alterção e o que da para fazer nele
        
    @staticmethod
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
    # vai atribuir uma função nela

    def menu_usuarios():
        # definiu a função como menu do crud usuarios, todas vez que chamar ela vai aparecer isso
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
        #printou o menu e o que da para fazer nele
        
    @staticmethod
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
    # vai atribuir uma função nela

    def menu_edicao_usuario():
        # função para editar o crud de usuarios, toda as vezes que chamar ele vai aparecer isso
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
        #printou o campo de alterção e o que da para fazer nele

    @staticmethod
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
    # vai atribuir uma função nela

    def menu_estabelecimentos_comerciais():
        # definiu a função como menu do crud estabelecimentos comercias, todas vez que chamar ela vai aparecer isso
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
            # printou o menu do crud e o que da para fazer nele
        
    @staticmethod
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
    # vai atribuir uma função nela

    def menu_edicao_estabelecimentos_comerciais():
       # função de ediação do crud de estabelecimentos, todas as vezes que chamar vai mostrar isso
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
        #printou o campo de alterção e o que da para fazer nele