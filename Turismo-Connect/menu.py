import os # importando a biblioteca OS, servindo como ponte entre o codigo e o sistema operacional
import crud_pontos_turisticos # importando o crud e tudo o que tem nele
import crud_usuarios # importando o crud e tudo o que tem nele
import crud_estabelecimentos_comerciais # importando o crud e tudo o que tem nele
import inputs # importando os inputs e tudo o que tem nele
import estrutura_menu # importando os menus e tudo o que tem nele


estrutura_menu = estrutura_menu.EstruturaMenu()
 # criando uma variavel estrutura menu e que recebe a classe EsturutaMenu que tava no codigo estrutura menu
crud_pontos_turisticos = crud_pontos_turisticos.PontosTuristicos()
 # criando uma variavel crud pontos turisticos e que recebe a classe PontosTuristicos que tava no crud pontos turisticos
crud_usuarios = crud_usuarios.Usuarios()
    # criando uma crud variavel e que recebe a classe Usuarios que tava no crud usuarios
crud_estabelecimentos_comerciais = crud_estabelecimentos_comerciais.EstabelicimentoComerciais()
    # criando uma crud variavel estabelecimento comerciais e que recebe com a classe EstabelicimentoComerciais que tava no crud estabelecimentos comerciais
inputs = inputs.Inputs()
    # criando uma crud variavel input e que recebe a classe Inputs que tava no codigo inputs

class Menu():
    # criando uma classe para menu e atribuindo funcoes nela
    
    @staticmethod
    # é uma classe idependente que não precisa do self porque nao puxa atributos de outra função, e está acessando a classe estrutura menu
    # e vai atribuir uma função nela

    def menu():
        # função menu
        
        while True: 
            # loop do crud enquanto for verdadeiro a condiçao

            estrutura_menu.menu_principal() #chamando a função menu principal do codigo estrutura menu
            inputs.escolha_menu_de_opcao() #chamando a função escolha menu de opção do codigo inputs

            match inputs.escolha_menu: # escolhe a variavel inputs e chama a função escolha menu dentro da variavel que recebe o classe Inputs

                case 1:
                    # caso escolha 1, crud pontos turisticos
                    while True:
                     # iniciando outro loop enquanto a condição for verdadeira   
                        estrutura_menu.menu_pontos_turisticos() #chamando a função menu principal do codigo estrutura menu
                        inputs.escolha_menu_de_opcao() #chamando a função escolha menu de opção do codigo inputs

                        if inputs.escolha_menu == 1: # se a escolha do menu dos pontos turisticos for 1
                            # vai dar o input de cadastrar ponto turistico
                            # chamando os parametros que o usuario vai escrever
                            # vai ter que escrever o nome, endereço, descrição, hora, e avaliações
                            inputs.cadastrar_ponto_turistico()
                            crud_pontos_turisticos.cadastrar_ponto_turistico(nome= inputs.nome_ponto_turistico, 
                                                                            endereco= inputs.endereco_ponto_turistico, 
                                                                            descricao= inputs.descricao_ponto_turistico,
                                                                            horario_de_funcionamento= inputs.horario_funcionamento_ponto_turistico, 
                                                                            media_de_avaliacoes= inputs.media_avaliacao_ponto_turistico)
                        # puxando os parametros que a pessoa vai escrever

                        elif inputs.escolha_menu == 2:
                            # se a escolha do menu dos pontos turisticos for 2
                            # vai listar todos o pontos turisticos que tem ate em então
                            # vai editar o que escolher para não gerar erro
                            crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()
                            estrutura_menu.menu_edicao_ponto_turistico()
                            inputs.editar_ponto_turistico()
                            # puxando funções

                            if inputs.id_coluna_para_alterar == 1:
                                # se for 1 edita o nome
                                campo_alteracao = "Nome"

                            elif inputs.id_coluna_para_alterar == 2:
                                # se for 2 edita o endereço
                                campo_alteracao = "Endereço"

                            elif inputs.id_coluna_para_alterar == 3:
                                # se for 3 edita descrição
                                campo_alteracao = "Descrição"

                            elif inputs.id_coluna_para_alterar == 4:
                                # se for 4 edita hora
                                campo_alteracao = "Horários de funcionamento"

                            elif inputs.id_coluna_para_alterar == 5:
                                # se for 5 edita avaliações
                                campo_alteracao = "Média das avaliações"
                            
                            else:
                                # se for algum numero que nao ta nas opções 
                                # printa opção invalida
                                print("Opção inválida!")

                            crud_pontos_turisticos.editar_informacao_ponto_turistico(id_ponto_turistico= inputs.id_ponto_turistico,
                                                                                     campo_de_alteracao= campo_alteracao,
                                                                                     nova_informacao= inputs.nova_informacao)
                            # puxando os parametros que a pessoa vai escrever

                        elif inputs.escolha_menu == 3:
                            # se a escolha do menu dos pontos turisticos for 3
                            # vai listar todos os pontos turistico
                            # vai puxar o input que você escolheu e vai excluir (salvar todos os id diferentes que tu não escolheu)
                            crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()
                            inputs.excluir_id()
                            crud_pontos_turisticos.deletar_ponto_turistico(id_ponto_turistico= inputs.id_excluir)
                            #puxando funções

                        elif inputs.escolha_menu == 4:
                            # se a escolha do menu dos pontos turisticos for 4
                            # vai listar os pontos turisticos
                            # puxando função lista ponto
                            crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()

                        elif inputs.escolha_menu == 5:
                            # se a escolha do menu dos pontos turisticos for 5
                            # vai sair do crud e voltar pro menu principal
                            break
                            #acabando o loop do crud 

                        else: # se digitar algo que não tem a opção, vai printar que foi invalido e vai repetir ate o usuario digitar o certo

                            print("Opção inválida!")

                    os.system("cls")
                    # lipando o terminal 

                case 2:
                    # caso escolha 2, crud usuarios

                    while True:
                        # iniciando outro loop enquanto a condição for verdadeira
                        estrutura_menu.menu_usuarios() #chamando a função menu usuarios do codigo estrutura menu
                        inputs.escolha_menu_de_opcao() #chamando a função menu de opções do codigo estrutura menu

                        if inputs.escolha_menu == 1:
                            # se a escolha do usuario for 1 
                            # vai dar um input e cadastrar o usuario 
                            # chamando os parametros que o usuario vai escrever
                            # vai ter que escrever o nome, cpf, email, telefone, endereço do usuario
                            inputs.inputs_cadastrar_usuario()
                            crud_usuarios.cadatrar_usuario(nome= inputs.nome_usuario,
                                                           cpf= inputs.cpf_usuario, 
                                                           idade= inputs.idade_usuario,
                                                            email= inputs.email_usuario,
                                                             telefone= inputs.telefone_usuario,
                                                              endereco= inputs.endereco_usuario )
                            # puxando os parametros que a pessoa vai escrever

                        elif inputs.escolha_menu == 2: 
                            # se a escolha do usuario for 2
                            # vai listar todos os usuarios
                            # e vai editar o que o usuario vai escrever

                            crud_usuarios.listar_usuarios_cadastrados() # chamando função
                            estrutura_menu.menu_edicao_usuario() # chamando função
                            inputs.inputs_editar_usuario()  # chamando função

                            if inputs.id_coluna_para_alterar == 1:  # campo de alteração  1 (Nome)

                                campo_alteracao = "Nome" 

                            elif inputs.id_coluna_para_alterar == 2: # campo de alteração  2 (cpf)

                                campo_alteracao = "CPF"

                            elif inputs.id_coluna_para_alterar == 3:    # campo de alteração  3 (idade)

                                campo_alteracao = "Idade" 

                            elif inputs.id_coluna_para_alterar == 4: # campo de alteração  4 (email)

                                campo_alteracao = "Email"

                            elif  inputs.id_coluna_para_alterar == 5:   # campo de alteração  5 (telefone)

                                campo_alteracao = "Telefone"

                            elif inputs.id_coluna_para_alterar == 6:    # campo de alterção 6 (endereço)

                                campo_alteracao = "Endereço"

                            else:

                                print("Opção inválida!") # se digitar algo que não tem a opção, vai printar que foi invalido e vai repetir ate o usuario digitar o certo

                            crud_usuarios.editar_informacao_usuario(id_usuario= inputs.id_usuario,
                                                                    campo_de_alteracao= campo_alteracao,
                                                                    nova_informacao= inputs.nova_informacao)
                            # puxando os parametros que a pessoa vai escrever
                            
                        elif inputs.escolha_menu == 3:
                            # se a escolha do menu dos usuarios for 3
                            # vai listar todos os usuarios
                            # vai puxar o input que você escolheu e vai excluir (salvar todos os id diferentes que tu não escolheu)

                            crud_usuarios.listar_usuarios_cadastrados()
                            inputs.excluir_id()
                            crud_usuarios.deletar_usuario(id_usuario= inputs.id_excluir)
                            # puxando as funções
                        elif inputs.escolha_menu == 4:
                            # se a escolha for 4 
                            # vai listar todos os usuarios
                            # puxando a função de lsita do usuario
                            crud_usuarios.listar_usuarios_cadastrados()

                        elif inputs.escolha_menu == 5:
                            # se for 5 vai sair desse menu de usuarios e voltar para o menu principal

                            break

                        else: 
                            # se digitar algo que não tem a opção, vai printar que foi invalido e vai repetir ate o usuario digitar o certo
                            print("Opção inválida!")
                        
                    os.system("cls")
                    # vai limpar o terminal

                case 3:
                    # caso o usuario escolher o 3 vai mostrar o crud de estabelecimentos
                    while True:
                        # iniciando outro loop enquanto a condição for verdadeira
                        
                        estrutura_menu.menu_estabelecimentos_comerciais()   #chamando a função menu estabelecimento do codigo estrutura menu
                        inputs.escolha_menu_de_opcao()  #chamando a função menu de opções do codigo estrutura menu

                        if inputs.escolha_menu == 1:    # se o usuario escolher 1 no menu de estabelecimento
                            # vai cadastrar o estbelecimento 
                            # chamando os parametros que o usuario vai escrever
                            # vai ter que digitar nome, tipo , endereco, descricao, hora, avaliação
                            inputs.inputs_cadastrar_estabelecimento_comercial()
                            crud_estabelecimentos_comerciais.cadastrar_novo_estabelecimento_comercial(nome= inputs.nome_estabelecimento_comercial,
                                                                                                      tipo= inputs.tipo_estabelecimento_comercial,
                                                                                                      endereco= inputs.endereco_estabelecimento_comercial,
                                                                                                      descricao= inputs.descricao_estabelecimento_comercial,
                                                                                                      horario_de_funcionamento= inputs.horario_funcionamento_estabelecimento_comercial,
                                                                                                      medio_de_avaliacoes= inputs.media_avaliacao_estabelecimento_comercial)
                            # puxando os parametros que a pessoa vai escrever
                            
                        elif inputs.escolha_menu == 2:
                            # se a escolha do menu de estabelecimento for 2
                            # vai puxar a função de listar e vai listar os estabelecimentos
                            # e vai puxar a estrutura de edição
                            # o usuario vai digitar o numero que quer mudar
                            # puxando o input
                            crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()
                            estrutura_menu.menu_edicao_estabelecimentos_comerciais()
                            inputs.inputs_editar_estabelecimento_comercial()

                            if inputs.id_coluna_para_alterar == 1:
                                # se for 1 vai editar o nome
                                campo_alteracao = "Nome"

                            elif inputs.id_coluna_para_alterar == 2:
                                # se for 2 vai editar tipo
                                campo_alteracao = "Tipo"

                            elif inputs.id_coluna_para_alterar == 3:
                                # se for 3 vai editar endereço
                                campo_alteracao = "Endereço"

                            elif inputs.id_coluna_para_alterar == 4:
                                # se for 4 vai editar descrição
                                campo_alteracao = "Descrição"

                            elif inputs.id_coluna_para_alterar == 5:
                                # se for 5 vai editar o horario
                                campo_alteracao = "Horários de funcionamento"

                            elif inputs.id_coluna_para_alterar == 6:
                                # se for 6 vai editar as avaliações
                                campo_alteracao = "Média das avaliações"
                            
                            else:
                                # caso escolha algo que não tem no menu vai printar opção invalida ate ele escolher certo
                                print("Opção inválida!")

                            crud_estabelecimentos_comerciais.editar_informacao_estabelicimento_comercial(id_estabelecimento_comercial= inputs.id_estabelecimento_comercial,
                                                                                                            campo_de_alteracao= campo_alteracao,
                                                                                                                nova_informacao= inputs.nova_informacao)
                            # puxando os parametros que a pessoa vai escrever
                            
                        elif inputs.escolha_menu == 3:  
                            # se escholer o 3 no menu de estabelecimento
                            # vai puxar a função de listar e listar os estabelecimentos comerciais
                            # vai pegar o input que o usuario escreveu
                            # vai excluir esse id
                            #( vai salvar todos os ids diferentes do que foi escolhido)

                            crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()
                            inputs.excluir_id()
                            crud_estabelecimentos_comerciais.deletar_estabelicimento_comerciais(id_estabelecimento_comercial= inputs.id_excluir)

                        elif inputs.escolha_menu == 4:
                            # se o usuario escolheu no menu de estabelecimentos 4 vai listar os estabelecimentos puxando a função
                            crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()

                        elif inputs.escolha_menu == 5:
                            # se for 5 a escolha no menu vai sair do menu de estabelecimento e voltar pro menu principal
                            break

                        else:
                            # se escolher algum numero errado vai printar opção invalida e vai voltar para o menu esperando o usuario digitar o certo
                            print("Opção inválida!")

                    os.system("cls")
                    # limpando o terminal
                case 4:
                    # caso a escolha for 4 no menu principal ele vai sair do sistema
                    print("""
                            -----------------------------------------------------------------------
                            Ahh poxa... Espero que possa voltar e conhecer nosso sistema. Obrigado!
                            -----------------------------------------------------------------------
                            """)
                    break
                # fim do progama e do loop

                case __:

                    print("Opção inválida!")    # caso contrario vai voltar o loop ate a pessoa digitar certo