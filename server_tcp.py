import socket
import random
# 1. Cria o socket IPv4 e TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Associa o IP e a Porta (bind)
servidor.bind(("0.0.0.0", 8080))

# 3. Coloca em modo de escuta (fila de conexões pendentes)
servidor.listen(5)
print("Servidor aguardando conexões na porta 8080...")

# 4. Aceita uma conexão recebida
conexao, endereco = servidor.accept()
print(f"Conectado por: {endereco}")

# 5. Recebe e envia dados
dados = conexao.recv(1024)
valor = float(dados.decode('utf-8')) # Retorna 10.5

cotacao = random.uniform(0, 10)

if dados:
    print("Mensagem recebida:", dados.decode("utf-8"))
    moeda = valor * cotacao
#    conexao.sendall(b"Mensagem recebida com sucesso!")
    mensagem = f"Valor da conversão = {moeda} e o valor da cotação do dólar é {cotacao}"
    conexao.sendall(mensagem.encode('utf-8'))
    #conexao.sendall(b"A cotação atual é:")
    #conexao.sendall(str(cotacao).encode('utf-8'))
    print(f'Valor total após conversão: {moeda} | Valor do dólar: {cotacao}')

# 6. Encerra as conexões
conexao.close()
servidor.close()