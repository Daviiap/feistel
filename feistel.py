BLOCK_SIZE = 8

def encrypt(key: list, rounds: int, message: bytes):
    expanded_msg = expand_message(message)
    enc_msg = feistel(key, rounds, expanded_msg)
    return enc_msg

def decrypt(key: list, rounds: int, enc_msg: bytes):
    dec_msg = feistel(key, rounds, enc_msg)
    return dec_msg.strip()

def feistel(key: list, rounds: int, msg: bytes):
    mod_msg = bytes()

    for i in range(0, len(msg), BLOCK_SIZE):
        message_block = msg[i:i+BLOCK_SIZE]
        mod_block = feistel_round(key, rounds, message_block)
        mod_msg += mod_block
    
    return mod_msg


def feistel_round(key: list, rounds: int, block: bytes):
    splitted_block_len = len(block)//2
    lBlock = block[:splitted_block_len]
    rBlock = block[splitted_block_len:]
    
    if rounds == 0:
        return rBlock + lBlock
    else:
        tmp = shuffle(rBlock, key)
        return feistel_round(key, rounds-1, rBlock+xor(tmp, lBlock))

def xor(block1: list, block2: list):
    xor_block = []
    
    for i in range(len(block1)):
        xor_block.append(block1[i]^block2[i])
        
    return bytes(xor_block)
    
def shuffle(block: bytes, key: list):
    new_block = []

    for i in range(len(block)):
        new_block.append(block[key[i]])

    return bytes(new_block)

def expand_message(message: bytes):
    msg_padding = (BLOCK_SIZE - (len(message) % BLOCK_SIZE)) % BLOCK_SIZE

    expanded_msg = message + (" " * msg_padding).encode('ascii')
    
    return expanded_msg