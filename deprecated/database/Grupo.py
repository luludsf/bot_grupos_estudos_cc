# -*- coding: utf-8 -*-
"""
class Grupo:
    Guarda informações como:
        Nome do grupo
        Link do grupo
"""
class Grupo:
    #
    def __init__(self, nome_grupo, link_grupo):
        self.nome_grupo = nome_grupo
        self.link_grupo = link_grupo
    pass
    #
    def __repr__(self):
        return "Grupo('{}', '{}')".format(self.nome_grupo,self.link_grupo)
    pass
pass