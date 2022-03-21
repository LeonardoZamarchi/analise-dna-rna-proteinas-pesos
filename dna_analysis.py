from cv2 import normalize 


cd_gen = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "GGG": "G", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "CAA": "Q", "AAA": "K", "GAA": "E", "CAG": "Q", 
    "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R",
    "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", 
    "AGC": "S", "GGC": "G", "CGA": "R", "AGA": "R", 
    "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R", 
    "AUG": "M", "UGA": "Stop", "UAG": "Stop", "UAA": "Stop"}

def cria_dna_complementar(dna):
    base_complementar = {"A": "T",
                        "T": "A",
                        "G": "C",
                        "C": "G"}
    dna_complementar = ""
    for base in dna:
        dna_complementar += base_complementar[base]
    return dna_complementar

def cria_rna(dna):
    rna = dna.replace("T", "U")
    return rna

def cria_proteina(rna,cd_gen):
    proteina = ""
    for pos in range(0, len(rna), 3):
        codon = rna[pos:pos+3]
        aminoacido = cd_gen[codon]
        if aminoacido != "Stop":
            proteina += aminoacido
        else:
            break
    return proteina

def compara_proteinas(proteina,proteina_referencia):
    for i in range (len(proteina)):
        if proteina[i] != proteina_referencia[i]:
            print('Variância na posição: '+str([i]))
            n = 1
        
    if n == 0:
        print('Não existe variância entre as proteínas')
        
    massa_aminoacido = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
                    "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406, 
                    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293, 
                    "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203, 
                    "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}
    massa_proteina, massa_referencia = 0,0
    for i in proteina:
        massa = massa_aminoacido[i]
        massa_proteina += massa
    for i in proteina_referencia:
        massa = massa_aminoacido[i]
        massa_referencia += massa
    
    if massa_proteina != massa_referencia:
        print('As massas das proteínas são diferentes')
    else:
        print('As massas das proteínas são iguais')
    
    print('Proteina base:       '+ massa_proteina)
    print('Proteina referencia: '+ massa_referencia)

    print('Variação de massa: ' + str(massa_proteina - massa_referencia))


    


dna = "ATGGTGCATCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAA"
proteina_referencia = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"

def run(dna):
    print('###################################')
    print('1 - Retornar fita complementar')
    print('2 - Retornar RNA')
    print('3 - Retornar proteina')
    print('4 - Valida variação entre proteinas')
    print('###################################')
    print('Informe o menu desejado: ')
    acao = int(input())
    if acao == 1:
        print(cria_dna_complementar(dna))
    elif acao ==2:
        print(cria_rna(dna))
    elif acao ==3:
        rna = cria_rna(dna)
        print(cria_proteina(rna,proteina_referencia))
    elif acao ==4:
        rna = cria_rna(dna)
        proteina = cria_proteina(rna,proteina_referencia)
        print(compara_proteinas(proteina))

run(dna)