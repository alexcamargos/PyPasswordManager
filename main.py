import os

# Variáveis
_TITLE = 'Py Password Manager'
_AUTHOR = 'Alex'
__version__ = '0.0.1'

master_user = 'alex'
master_pass = '123456'

# Dicionário de dados temporário.
# Dados no padrão:
# {'NomeServiço':'Nome do Servido', 'Usuario':'Nome do Usuário', 'Senha':'Senha do Usuário', 'Data':'Data de Gravação'}
password_manager = {'Service#1': {'Service': 'YouTube', 'User': 'alcamargos', 'Password': '123456'},
                    'Service#2': {'Service': 'DropBox', 'User': 'camargos', 'Password': '7895644'},
                    'Service#3': {'Service': 'Google', 'User': 'lopescamargos', 'Password': 'camargos123456'},
                    'Service#4': {'Service': 'Hotmail', 'User': 'sanders', 'Password': '654321'}
                    }


def show_title():
    print(f'\n{_TITLE :>40}, by {_AUTHOR}\n')


def show_continue():
    return input('\nPressione <ENTER> para continuar.')


def clear_cli():

    """Limpa o terminar."""

    os.system('cls') or None


def master_login():
    user = input('\nLOGIN: ')
    u_pass = input('Password: ')

    if user == master_user and u_pass == master_pass:
        return True
    else:
        print('\n\nInformações erradas, encerrando aplicação!!!\n')
        show_continue()
        return False


def show_menu(menu):

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
        dicionário

    """
    serv = input('Serviço: ')
    user = input('Usuário: ')
    u_pass = input('Senha: ')

    return {'Service': serv, 'User': user, 'Password': u_pass}


def add_service():
    n = len(password_manager)

    password_manager[f'Service#{n}'] = input_service()

    show_continue()


def check_services_exist(serv, pm):

    """Checa se um serviço ja esta no banco de dados."""

    return [True for data in pm.values() if serv in data.values()]


def search_service_menu(name):

    if check_services_exist(name, password_manager):
        print('\nServiço existe no banco de dados!!!')
    else:
        print('\nServiço no existe no banco de dados!!')
    show_continue()


def delete_service_menu(service):

    for i in range(1, len(password_manager) + 1):
        if service in password_manager[f'Service#{i}'].values():
            del password_manager[f'Service#{i}']


def edit_service_menu(service, db):

    for i in range(1, len(db) + 1):
        if service in db[f'Service#{i}'].values():
            new_data = input_service()
            db[f'Service#{i}']['Service'] = new_data['Service']
            db[f'Service#{i}']['User'] = new_data['User']
            db[f'Service#{i}']['Password'] = new_data['Password']


def show_service_menu():

    """Mostra os dados dos serviços salvos no banco de dados."""

    clear_cli()

    for service in password_manager.items():
        print(service[0])
        print(f"\tServiço: {service[1]['Service']}")
        print(f"\tUsuário: {service[1]['User']}")
        print(f"\tSenha: {service[1]['Password']}")
    show_continue()


def insert_menu():
    print('Insira as informações do serviço.\n')
    add_service()


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
            insert_menu()
        elif opt == 2:
            search_service_menu(input('Serviço: '))
        elif opt == 3:
            show_service_menu()
        elif opt == 4:
            serv_edit = input('Informe o nome do seriço que deseja editar: ')
            if check_services_exist(serv_edit, password_manager):
                edit_service_menu(serv_edit, password_manager)
            else:
                print('Não existe este serviço no banco de dados!')
                show_continue()
        elif opt == 5:
            serv_del = input('Informe o nome do serviço que deseja deletar: ')
            delete_service_menu(serv_del)
        elif opt == 6:
            exit()


if __name__ == '__main__':
    show_title()

    if master_login():
        main()
