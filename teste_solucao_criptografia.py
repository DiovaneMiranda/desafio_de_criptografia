"""
Solução do Desafio de Criptografia
Autor: Diovane Miranda
Data: 08/02/2019
"""
from encrypt_prime_scramble import encrypt
from decrypt_prime_scramble import decrypt


def main():
    
    strings_criptografadas = {
        'email':'cqil}##$E3.79>AuKEXMMXW_mt8{u',
        'assunto':'ohhvy$&t.!/->13>?COV',
    }
    strings_descriptografadas = {}
    print('Strings Criptografadas:    {}'.format(strings_criptografadas))
    # descriptografe
    resultado = decrypt(
        strings_criptografadas['email'], 
        strings_criptografadas['assunto'],
    )
    strings_descriptografadas.update({
        'email':resultado[0],
        'assunto':resultado[1],
    })
    print('Strings Descriptografadas: {}'.format(strings_descriptografadas))

if __name__ == "__main__":
    main()

