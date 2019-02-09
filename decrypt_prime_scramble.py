from nth_prime_number import nth_prime_number


def decrypt(*args):
    """ 
    Função que recebe uma string cryptografada e a retorna descriptografada.
    Criptografia Prime-Scramble. 
    Pode ser informada qualquer quantidade de strings como input,
    apenas separe-as por vírgula
    """
    decrypted_char_list = []
    decrypted_string_list = []
    n = 1

    for arg in args:
        for encrypted_char in arg:
            # subtraia o número primo de mesma ordem do valor ascii do caractere
            decrypted_char_ascii = ord(encrypted_char) - nth_prime_number(n)
            # se o valor ascii resultante for menor que o limite inferior,
            # comece a partir do limite superior de forma decrescente
            if decrypted_char_ascii < 33:
                decrypted_char_ascii = 126 - (33 - decrypted_char_ascii)
            # converta o ascii descriptografado para caractere
            decrypted_char = str(chr(decrypted_char_ascii))
            decrypted_char_list.append(decrypted_char)
            n += 1
        decrypted_string = ''.join(decrypted_char_list)
        decrypted_char_list = []
        decrypted_string_list.append(decrypted_string)
    return decrypted_string_list




