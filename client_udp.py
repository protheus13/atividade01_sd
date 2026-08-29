import socket

# Cria o socket UDP
cliente_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

valor = 10.0

mensagem = f"{valor}".encode('utf-8')
# Envia direto para a origem/porta
servidor_destino = ("192.168.1.80", 9000)
cliente_udp.sendto(mensagem, servidor_destino)

# Recebe os dados e o endereço do remetente
dados, endereco = cliente_udp.recvfrom(1024)
print(f"Resposta de {endereco}: {dados.decode('utf-8')}")

cliente_udp.close()