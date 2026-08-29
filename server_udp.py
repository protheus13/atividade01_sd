import socket
import random

# 1. Configurações de IP e Porta
HOST = "0.0.0.0"  
PORTA = 9000

# 2. Cria o socket UDP (AF_INET para IPv4, SOCK_DGRAM para UDP)
servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. Associa o socket ao endereço e porta (bind)
servidor_udp.bind((HOST, PORTA))

print(f"Servidor UDP rodando e aguardando pacotes em {HOST}:{PORTA}...")


# 4. Recebe os dados e o endereço de origem do cliente (buffer de 1024 bytes)
dados, endereco_cliente = servidor_udp.recvfrom(1024)
        
valor = float(dados.decode("utf-8"))
cotacao = random.uniform(0, 10)

print(f"Pacote recebido de {endereco_cliente}: {valor}")
print(f"Cotação atual para conversão: {cotacao}")

moeda = valor * cotacao
# 5. Envia uma resposta de volta para o endereço de onde o pacote veio
resposta = f"Valor convertido: {moeda:.2f}".encode("utf-8")
servidor_udp.sendto(resposta, endereco_cliente)


# 6. Fecha o socket
servidor_udp.close()