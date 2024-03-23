from socket import *
import feistel

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

enc_key = [2,0,3,1]
rounds = 4

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
  connectionSocket, addr = serverSocket.accept()
  enc_sentence = connectionSocket.recv(1024)

  sentence = feistel.decrypt(enc_key, 
                             rounds, 
                             enc_sentence)
  
  capitalizedSentence = sentence.upper()
  connectionSocket.send(feistel.encrypt(enc_key,
                                        rounds,
                                        capitalizedSentence))
  connectionSocket.close()
