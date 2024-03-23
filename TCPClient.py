from socket import *
import feistel

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

enc_key = [2,0,3,1]
rounds = 4

#Conecta ao servidor
clientSocket.connect((serverName,serverPort))

#Recebe mensagem do usuario e envia ao servidor
message = input('Digite uma frase: ')

enc_msg = feistel.encrypt(key=enc_key, 
                          rounds=rounds, 
                          message=message.encode('ascii'))

clientSocket.send(enc_msg)

#Aguarda mensagem de retorno e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)
print("Retorno do Servidor:",feistel.decrypt(enc_key,
                                             rounds,
                                             modifiedMessage).decode())

clientSocket.close()
