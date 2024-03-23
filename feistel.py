def encrypt(key: list, rounds: int, message: bytes):
    expandedMsg = expandMessage(message)
    
    enc_msg = bytes()
    
    for i in range(0, len(expandedMsg), 8):
        messageBlock = expandedMsg[i:i+8]
        encryptedBlock = feistel(key, rounds, messageBlock)
        enc_msg += encryptedBlock

    return enc_msg

def decrypt(key: list, rounds: int, enc_msg: bytes):
    dec_msg = bytes()
    
    for i in range(0, len(enc_msg), 8):
        messageBlock = enc_msg[i:i+8]
        decryptedBlock = feistel(key, rounds, messageBlock)
        dec_msg += decryptedBlock

    return dec_msg.strip()

def feistel(key: list, rounds: int, block: bytes):
    splittedBlockLen = len(block)//2
    lBlock = block[:splittedBlockLen]
    rBlock = block[splittedBlockLen:]
    
    if rounds == 0:
        return rBlock + lBlock
    else:
        tmp = shuffle(rBlock, key)
        return feistel(key, rounds-1, rBlock+xor(tmp, lBlock))

def xor(block1: list, block2: list):
    xorBlock = []
    
    for i in range(len(block1)):
        xorBlock.append(block1[i]^block2[i])
        
    return bytes(xorBlock)
    
def shuffle(block: bytes, key: list):
    newBlock = []

    for i in range(len(block)):
        newBlock.append(block[key[i]])

    return bytes(newBlock)

def expandMessage(message: bytes):
    msgPadding = (8 - (len(message) % 8)) % 8

    expandedMsg = message + (" " * msgPadding).encode('ascii')
    
    return expandedMsg