#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import localtime

from back_end.password_manager import PasswordManager
from back_end.service_structure import search_for_service, insert_service, list_service, edit_service, del_service


# Variáveis
_TITLE = 'Py Password Manager'
_AUTHOR = 'Alex'
__version__ = '0.0.1'

master_user = 'alex'
master_pass = '123456'

# Dicionário de dados temporário.
password_manager = [
    PasswordManager(1, 'YouTube', 'alcamargos', '123456', localtime()),
    PasswordManager(2, 'DropBox', 'camargos', '7895644', localtime()),
    PasswordManager(3, 'Google', 'lopescamargos', 'camargos123456', localtime()),
    PasswordManager(4, 'Hotmail', 'sanders', '654321', localtime())
]


def show_title():
    print(f'\n{_TITLE :>40}, by {_AUTHOR}\n')


def show_continue():
    return input('\nPressione <ENTER> para continuar.')


def clear_cli():

    """Limpa o terminar."""

    os.system('cls') or None


def master_login():
    clear_cli()
    show_title()

    user = input('\nLOGIN: ')
    u_pass = input('Password: ')

    if user == master_user and u_pass == master_pass:
        return True
    else:
        print('\n\nInformações erradas, encerrando aplicação!!!\n')
        show_continue()
        return False


def show_menu(menu):

    clear_cli()
    show_title()

    for item in menu:
        print(f'\t{item}')

    while True:
        try:
            print()
            return int(input('>>> '))
        except ValueError:
            print('Selecione uma das opções acima!')


def input_service():

    """Solicita do usuário as informações sobre os serviços!

    Return:
        PasswordManager instance

    """

    clear_cli()
    show_title()

    print('Insira as informações do serviço.\n')
    serv = input('Serviço: ')
    user = input('Usuário: ')
    u_pass = input('Senha: ')

    return serv, user, u_pass


def add_service_menu():
    serv, user, u_pass = input_service()
    insert_service(serv, user, u_pass, localtime(), password_manager)
    show_continue()
    clear_cli()


def search_service_menu(serv):

    identity = search_for_service(serv, password_manager)

    if identity:
        print('\nServiço existe no banco de dados!!!\n')
        print(password_manager[identity[0] - 1])
    else:
        print('\nServiço não existe no banco de dados!!!')

    show_continue()
    clear_cli()


def del_service_menu(service):

    clear_cli()

    opt = input('Deletar serviços: (s)im, (N)ão: ')
    if opt.lower() == 's':
        del_service(service, password_manager)


def edit_service_menu(service):
    identity = search_for_service(service, password_manager)
    serv, user, u_pass = input_service()
    edit_service(serv, user, u_pass, password_manager[identity[0] - 1])
    clear_cli()


def show_service_menu():

    """Mostra os dados dos serviços salvos no banco de dados."""

    clear_cli()
    show_title()
    list_service(password_manager)
    show_continue()


def main():

    clear_cli()
    show_title()

    main_menu = [
        '1 - Inserir',
        '2 - Buscar',
        '3 - Listar',
        '4 - Editar',
        '5 - Excluir',
        '6 - Sair'
    ]

    run = True
    while run:
        opt = show_menu(main_menu)
        if opt == 1:
            add_service_menu()
        elif opt == 2:
            search_service_menu(input('Serviço: '))
        elif opt == 3:
            show_service_menu()
        elif opt == 4:
            service_edit = input('Informe o nome do seriço que deseja editar: ')
            if search_for_service(service_edit, password_manager):
                edit_service_menu(service_edit)
            else:
                print('Não existe este serviço no banco de dados!')
                show_continue()
        elif opt == 5:
            serv_del = input('Informe o nome do serviço que deseja deletar: ')
            del_service_menu(serv_del)
        elif opt == 6:
            exit()


if __name__ == '__main__':
    # main()
    if master_login():
        main()
