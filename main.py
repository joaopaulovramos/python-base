#!python3

""" Hello World multi languages 

Dependendo da lingua configurada do ambiente o programa exibe a mensagem
correspondente.

Usage:
    LANG in env, e:
    export LANG=pt_BR

Execution:

    python3 hello.py
"""

__version__ = "0.0.1"
__author__ = "Joao Paulo"
__license__ = "Unlicense"


import os


current_language = os.getenv("LANG")[:5]

msg = "Hello, World"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"

print(msg)
