import ctypes
print("início do exemplo")
# Carregando a DLL ACBrLibConsultaCNPJ
acbr_lib = ctypes.WinDLL(r'C:\ACBrLibConsultaCNPJPython\ACBrConsultaCNPJ64.dll')
print("dll carregada")
inicializa = acbr_lib.CNPJ_Inicializar(r'C:\ACBrLibConsultaCNPJPython\ACBrConsultaCNPJ.INI'.encode("utf-8"),"".encode("utf-8"))
print(inicializa)

sResposta = saida = ctypes.create_string_buffer(256)
Tamanho = ctypes.c_int()

# Realizando a consulta do CNPJ
# 65708551000150
# 18760540000139
resultado = acbr_lib.CNPJ_Versao(sResposta,Tamanho)
print('Resultado')
print(resultado)
print(Tamanho)
print(sResposta.value.decode('utf-8'))

# CNPJ = r'"65708551000150"'.encode("utf-8")

# resultado = acbr_lib.CNPJ_Consultar(CNPJ, 
#                                     2,
#                                     sResposta,
#                                     Tamanho)

# print(resultado)
# print(sResposta.decode("utf-8"))

if resultado == 0:
    resultado = acbr_lib.CNPJ_UltimoRetorno( sResposta,
                                         Tamanho)
    # Verificando se a consulta foi bem sucedida
    if resultado == 0:
        # Extraindo os dados do CNPJ consultado
        sResposta = sResposta.decode("utf-8")
        dados = sResposta.split("|")

        # Exibindo os dados do CNPJ consultado
        print("Razão social: ", dados[1])
        print("Nome fantasia: ", dados[2])
        print("Endereço: ", dados[4])
    else:
        # Exibindo o erro ocorrido na consulta
        print("Erro na consulta: ", resultado)

acbr_lib.CNPJ_Finalizar()