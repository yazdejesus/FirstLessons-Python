from redo115.lib.interface import *
from redo115.lib.arquivo import *

doc = 'ex115CeV_doc.txt'

opcoes = ["ver pessoas registradas", "registrar pessoas", "sair"]

existe_file(doc)
menu(opcoes, doc)
