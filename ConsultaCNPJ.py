import ctypes
from PIL import Image

# Carregando a DLL ACBrLibConsultaCNPJ
acbr_lib = ctypes.windll.LoadLibrary(r'D:\ACBrLibConsultaCNPJ\ACBrConsultaCNPJ64.dll')

inicializa = acbr_lib.CNPJ_Inicializar(r'D:\ACBrLibConsultaCNPJ\ACBrConsultaCNPJ.INI'.encode("utf-8"),"".encode("utf-8"))

retorno = acbr_lib.CNPJ_ConsultarCaptcha(r'D:\ACBrLibConsultaCNPJ'.encode("utf-8"),"".encode("utf-8"),"".encode("utf-8"))

img = Image.open("CaptchaCNPJ.png")
img.show()

eCAPCHA = input('Digite o captcha:')

sResposta = "".encode("utf-8")

# Realizando a consulta do CNPJ
resultado = acbr_lib.CNPJ_Consultar(r'18760540000139'.encode("utf-8"), eCAPCHA.encode("utf-8"), sResposta,0)

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
