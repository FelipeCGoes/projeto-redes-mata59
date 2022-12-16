import socket
import threading

"CRIA SOCKET"

"ENVIA VALOR DO SOCKET PARA SERVIDOR CENTRAL? (A decidir)"

"LISTEN (Aguarda mensagens do servidor central)"

""" 
Mensagem.op == 0 {

Armazenar a cópia do arquivo e o id do usuário dono sobreescrevendo se ela já existe

SEND STATUS OK
}

"""

"LISTEN"

"""
Mensagem.op == 1 {

Busca arquivo e manda arquivo

SEND arquivo STATUS OK

}
"""
