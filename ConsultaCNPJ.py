import ctypes

# Carregando a DLL ACBrLibConsultaCNPJ
acbr_lib = ctypes.windll.LoadLibrary(r'D:\ACBrLibConsultaCNPJ\ACBrConsultaCNPJ64.dll')

inicializa = acbr_lib.CNPJ_Inicializar(r'D:\ACBrLibConsultaCNPJ\ACBrConsultaCNPJ.INI'.encode("utf-8"),"".encode("utf-8"))

# Definindo o tipo de retorno da função CNPJ_Consultar
acbr_lib.CNPJ_Consultar.restype = ctypes.c_char_p

# Definindo os tipos dos parâmetros da função CNPJ_Consultar
acbr_lib.CNPJ_Consultar.argtypes = [ctypes.c_char_p, ctypes.c_bool, ctypes.c_char_p, ctypes.c_int]

eCNPJ = b"18760540000139"

retorno = acbr_lib.CNPJ_ConsultarCaptcha(r'D:\ACBrLibConsultaCNPJ'.encode("utf-8"),"".encode("utf-8"),"".encode("utf-8"))

eCAPCHA = b"2qh6ps"

# Realizando a consulta do CNPJ
resultado = acbr_lib.CNPJ_Consultar(eCNPJ, eCAPCHA, b"", 0)

# Verificando se a consulta foi bem sucedida
if resultado.startswith(b"OK"):
    # Extraindo os dados do CNPJ consultado
    resultado = resultado.decode("utf-8")
    dados = resultado.split("|")

    # Exibindo os dados do CNPJ consultado
    print("Razão social: ", dados[1])
    print("Nome fantasia: ", dados[2])
    print("Endereço: ", dados[4])
else:
    # Exibindo o erro ocorrido na consulta
    print("Erro na consulta: ", resultado.decode("utf-8"))
