#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from password_manager import PasswordManager


def search_for_service(service, db):

    """Verifica se um serviço ja esta no banco de dados."""

    return [serv.identity for serv in db if serv.service == service][0]


def insert_service(service, user, password, time, db):

    return db.append(PasswordManager(len(db) + 1, service, user, password, time))


def list_service(db):

    for serv in db:
        print(serv)
        print()


def edit_service(service, user, password, db):

    db.service = service
    db.user = user
    db.password = password


def del_service(service, db):

    identity = search_for_service(service, db)
    if identity:
        del db[identity - 1]

        for serv in range(identity - 1, len(db)):
            db[serv].identity -= 1
