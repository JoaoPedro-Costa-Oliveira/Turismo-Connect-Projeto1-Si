import os 
import crud_pontos_turisticos 
import crud_usuarios 
import crud_estabelecimentos_comerciais 
import inputs 
import estrutura_menu 

estrutura_menu = estrutura_menu.EstruturaMenu()
 crud_pontos_turisticos = crud_pontos_turisticos.PontosTuristicos()
 crud_usuarios = crud_usuarios.Usuarios()
 crud_estabelecimentos_comerciais = crud_estabelecimentos_comerciais.EstabelicimentoComerciais()
 inputs = inputs.Inputs()
 
class Menu():
    
    @staticmethod
 
    def menu():
        
        while True: 
 
            estrutura_menu.menu_principal() 
            inputs.escolha_menu_de_opcao() 
            match inputs.escolha_menu: 
                case 1:
                    while True:
                        estrutura_menu.menu_pontos_turisticos() 
                        inputs.escolha_menu_de_opcao() 
                        if inputs.escolha_menu == 1: 
                            inputs.cadastrar_ponto_turistico()
                            crud_pontos_turisticos.cadastrar_ponto_turistico(nome= inputs.nome_ponto_turistico, 
                                                                            endereco= inputs.endereco_ponto_turistico, 
                                                                            descricao= inputs.descricao_ponto_turistico,
                                                                            horario_de_funcionamento= inputs.horario_funcionamento_ponto_turistico, 
                                                                            media_de_avaliacoes= inputs.media_avaliacao_ponto_turistico)
                        
                        elif inputs.escolha_menu == 2:
                            crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()
                            estrutura_menu.menu_edicao_ponto_turistico()
                            inputs.editar_ponto_turistico()
                        
                            if inputs.id_coluna_para_alterar == 1:
                                campo_alteracao = "Nome"

                            elif inputs.id_coluna_para_alterar == 2:
                                campo_alteracao = "Endereço"

                            elif inputs.id_coluna_para_alterar == 3:
                                campo_alteracao = "Descrição"

                            elif inputs.id_coluna_para_alterar == 4:
                                campo_alteracao = "Horários de funcionamento"

                            elif inputs.id_coluna_para_alterar == 5:
                                campo_alteracao = "Média das avaliações"
                            
                            else:
                                print("Opção inválida!")

                            crud_pontos_turisticos.editar_informacao_ponto_turistico(id_ponto_turistico= inputs.id_ponto_turistico,
                                                                                     campo_de_alteracao= campo_alteracao,
                                                                                     nova_informacao= inputs.nova_informacao)
                        
                        elif inputs.escolha_menu == 3:
                            crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()
                            inputs.excluir_id()
                            crud_pontos_turisticos.deletar_ponto_turistico(id_ponto_turistico= inputs.id_excluir)
                        
                        elif inputs.escolha_menu == 4:
                            crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()

                        elif inputs.escolha_menu == 5:
                            break
                        
                        else: 
                            print("Opção inválida!")

                    os.system("cls")
                    
                case 2:
                    
                    while True:
                        estrutura_menu.menu_usuarios() 
                        inputs.escolha_menu_de_opcao() 
                        if inputs.escolha_menu == 1:
                            inputs.inputs_cadastrar_usuario()
                            crud_usuarios.cadatrar_usuario(nome= inputs.nome_usuario,
                                                           cpf= inputs.cpf_usuario, 
                                                           idade= inputs.idade_usuario,
                                                            email= inputs.email_usuario,
                                                             telefone= inputs.telefone_usuario,
                                                              endereco= inputs.endereco_usuario )
                            
                        elif inputs.escolha_menu == 2: 
                            
                            crud_usuarios.listar_usuarios_cadastrados() 
                            estrutura_menu.menu_edicao_usuario() 
                            inputs.inputs_editar_usuario()  

                            if inputs.id_coluna_para_alterar == 1:  
                                campo_alteracao = "Nome" 

                            elif inputs.id_coluna_para_alterar == 2: 
                                campo_alteracao = "CPF"

                            elif inputs.id_coluna_para_alterar == 3: 
                                campo_alteracao = "Idade" 

                            elif inputs.id_coluna_para_alterar == 4:
                                campo_alteracao = "Email"

                            elif  inputs.id_coluna_para_alterar == 5:  
                                campo_alteracao = "Telefone"

                            elif inputs.id_coluna_para_alterar == 6:   
                                campo_alteracao = "Endereço"

                            else:

                                print("Opção inválida!") 
                            crud_usuarios.editar_informacao_usuario(id_usuario= inputs.id_usuario,
                                                                    campo_de_alteracao= campo_alteracao,
                                                                    nova_informacao= inputs.nova_informacao)
                            
                        elif inputs.escolha_menu == 3:
                            
                            crud_usuarios.listar_usuarios_cadastrados()
                            inputs.excluir_id()
                            crud_usuarios.deletar_usuario(id_usuario= inputs.id_excluir)
                            
                        elif inputs.escolha_menu == 4:
                            crud_usuarios.listar_usuarios_cadastrados()

                        elif inputs.escolha_menu == 5:
                            
                            break

                        else: 
                            print("Opção inválida!")
                        
                    os.system("cls")
                    
                case 3:
                    while True:
                        
                        estrutura_menu.menu_estabelecimentos_comerciais()   
                        inputs.escolha_menu_de_opcao()  
                        if inputs.escolha_menu == 1:    
                            inputs.inputs_cadastrar_estabelecimento_comercial()
                            crud_estabelecimentos_comerciais.cadastrar_novo_estabelecimento_comercial(nome= inputs.nome_estabelecimento_comercial,
                                                                                                      tipo= inputs.tipo_estabelecimento_comercial,
                                                                                                      endereco= inputs.endereco_estabelecimento_comercial,
                                                                                                      descricao= inputs.descricao_estabelecimento_comercial,
                                                                                                      horario_de_funcionamento= inputs.horario_funcionamento_estabelecimento_comercial,
                                                                                                      medio_de_avaliacoes= inputs.media_avaliacao_estabelecimento_comercial)
                            
                        elif inputs.escolha_menu == 2:
                            crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()
                            estrutura_menu.menu_edicao_estabelecimentos_comerciais()
                            inputs.inputs_editar_estabelecimento_comercial()

                            if inputs.id_coluna_para_alterar == 1:
                                campo_alteracao = "Nome"

                            elif inputs.id_coluna_para_alterar == 2:
                                campo_alteracao = "Tipo"

                            elif inputs.id_coluna_para_alterar == 3:
                                campo_alteracao = "Endereço"

                            elif inputs.id_coluna_para_alterar == 4:
                                campo_alteracao = "Descrição"

                            elif inputs.id_coluna_para_alterar == 5:
                                campo_alteracao = "Horários de funcionamento"

                            elif inputs.id_coluna_para_alterar == 6:
                                campo_alteracao = "Média das avaliações"
                            
                            else:
                                print("Opção inválida!")

                            crud_estabelecimentos_comerciais.editar_informacao_estabelicimento_comercial(id_estabelecimento_comercial= inputs.id_estabelecimento_comercial,
                                                                                                            campo_de_alteracao= campo_alteracao,
                                                                                                                nova_informacao= inputs.nova_informacao)
                            
                        elif inputs.escolha_menu == 3:  
                            
                            crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()
                            inputs.excluir_id()
                            crud_estabelecimentos_comerciais.deletar_estabelicimento_comerciais(id_estabelecimento_comercial= inputs.id_excluir)

                        elif inputs.escolha_menu == 4:
                            crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()

                        elif inputs.escolha_menu == 5:
                            break

                        else:
                            print("Opção inválida!")

                    os.system("cls")
                    
                case 4:
                    print("""
                            -----------------------------------------------------------------------
                            Ahh poxa... Espero que possa voltar e conhecer nosso sistema. Obrigado!
                            -----------------------------------------------------------------------
                            """)
                    break
                
                case __:

                    print("Opção inválida!")   
