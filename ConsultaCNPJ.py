import ctypes
print("início do exemplo")
# Carregando a DLL ACBrLibConsultaCNPJ
acbr_lib = ctypes.cdll.LoadLibrary(r'C:\ACBrLibConsultaCNPJPython\ACBrConsultaCNPJ64.dll')
print("dll carregada")
print(acbr_lib)
inicializa = acbr_lib.CNPJ_Inicializar(r'C:\ACBrLibConsultaCNPJPython\ACBrConsultaCNPJ.INI'.encode("utf-8"),"".encode("utf-8"))
print(inicializa)
sResposta = r"".encode("utf-8")

Tamanho = 0

# Realizando a consulta do CNPJ
resultado = acbr_lib.CNPJ_Consultar(r'18.760.540/0001-39'.encode("utf-8"), 
                                    2,
                                    sResposta,
                                    Tamanho)

print(resultado)
print(sResposta.decode("utf-8"))

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