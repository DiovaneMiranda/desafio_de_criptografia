from nth_prime_number import nth_prime_number


def encrypt(*args):
    """ 
    Função que recebe strings e as retorna criptografadas
    utilizando a criptografia Prime-Scramble
    """
    encrypted_string_list = []
    encrypted_char_list = []
    n = 1
    for arg in args:
        for char in arg:
            # Converta o caracter em código ASCII
            char_ascii = ord(char)
            # Soma o valor ASCII do caracter ao número primo de mesmo índice
            encrypted_char_ascii = char_ascii + nth_prime_number(n)
            # enquanto soma for maior que 125, comece novamente a partir do
            # limite inferior
            while encrypted_char_ascii > 125:
                encrypted_char_ascii = 33 + (encrypted_char_ascii - 126)
            # converta o valor ASCII criptografado em caractere
            encrypted_char = str(chr(encrypted_char_ascii))
            encrypted_char_list.append(encrypted_char)
            n += 1
        encrypted_string = ''.join(encrypted_char_list)
        encrypted_string_list.append(encrypted_string)
    return encrypted_string_list