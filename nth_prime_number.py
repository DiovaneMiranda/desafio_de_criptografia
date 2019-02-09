
def nth_prime_number(n):
    """ Uma função que retorna o enésimo número primo """
    # lista inicial de números primos
    prime_list = [2]
    # primeiro número para testar se é primo
    num = 3
    # continue gerando primos até que o enésimo seja alcançado
    while len(prime_list) < n:

        # cheque se o número é divisível por algum primo que o anteceda
        for p in prime_list:
            # se não há resto então o número não é primo
            if num % p == 0:
                # não é primo. Saia do loop e teste o próximo
                break
        # se é primo, adicione o número à lista após o loop
        else:
            prime_list.append(num)
    
        # otimização: não verifique números pares
        num += 2

    # retorne o último número primo da lista
    return prime_list[-1]