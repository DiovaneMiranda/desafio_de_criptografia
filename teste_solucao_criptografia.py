"""
Solução do Desafio de Criptografia
Autor: Diovane Miranda
Data: 08/02/2019
"""
from decrypt_prime_scramble import decrypt


def main():
    # strings criptografadas
    strings_descriptografadas = {}
    email_criptografado = 'cqil}##$E3.79>AuKEXMMXW_mt8{u'
    assunto_criptografado = 'ohhvy$&t.!/->13>?COV'
    # descriptografe
    email_descriptografado = decrypt(email_criptografado)
    assunto_descriptografado = decrypt(assunto_criptografado)
    strings_descriptografadas.update({
        'emai':email_descriptografado[0],
        'assunto':assunto_descriptografado[0],
    })
    print(strings_descriptografadas)

if __name__ == "__main__":
    main()

