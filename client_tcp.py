import socket

# 1. Cria o socket IPv4 e TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Conecta ao servidor (Host, Porta)
cliente.connect(("192.168.1.80", 8080))

# 3. Envia dados (é necessário codificar em bytes)
valor = 10.0

# Converte o float para string e depois para bytes
cliente.sendall(str(valor).encode('utf-8'))

# 4. Recebe a resposta (buffer de 1024 bytes)
resposta = cliente.recv(1024)
print("Recebido:", resposta.decode("utf-8"))

# 5. Fecha a conexão
cliente.close()