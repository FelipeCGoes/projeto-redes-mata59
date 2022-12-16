import socket
import threading

...

"CRIAR SOCKET"

"Lança N threads que são N servidores"

"LISTEN? (pode ser fixo?) - preferência por manter as portas desses servidores fixas"

"Mantém lista com portas dos servidores"

"LISTEN (Aguarda por requisições do cliente)"

"""
if Mensagem.op == 0 {

Seleciona Mensagem.N servidores para enviar a cópia do arquivo

Busca se o arquivo já existe ou não

if nao existe {

    Salva nome do arquivo/servidores enviados

    for i in range N {
        SEND -> port = listaServer[i]
    }
    
} else {

    recupera lista de servidores que tem o arquivo

    if Mensagem.N >= listaArqServer.length() {
        Envia nova cópia para servidores da lista
        Envia para novos servidores
        Atualiza a lista
    } else {
        Seleciona Mensagem.N servidores e envia nova cópia
        Atualiza lista apenas com os Mensagem.N servidores que tem a nova cópia
    }
}

}
"""

"LISTEN"

"""
if Mensagem.op == 1 {

Busca na lista de arquivo/servidores se o arquivo está presente

if encontrado {

    if idUser == Mensagem.idUser {
        SEND -> port = listaServer[a]
        LISTEN (Aguarda o servidor devolver o arquivo)
        SEND cliente -> Arquivo STATUS OK
    } else {
        SEND cliente STATUS PERMISSAO NEGADA
    }

} else {
    SEND Cliente ARQUIVO NAO ENCONTRADO
}
"""