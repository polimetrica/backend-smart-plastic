import os
import pandas as pd
from ftplib import FTP
import os

FTP_HOST = os.getenv("FTP_HOST", "ftp.seuservidor.com")
FTP_USER = os.getenv("FTP_USER", "seu_usuario")
FTP_PASS = os.getenv("FTP_PASS", "sua_senha")
FTP_DEST_DIR = os.getenv("FTP_DEST_DIR", "/receitas/")

def send_order_file(order):
    df = pd.DataFrame([{
        "Cliente": order.client,
        "Tipo de Filme": order.film_type,
        "Largura": order.width,
        "Espessura": order.thickness,
        "Peso": order.weight,
        "Componente 1 (%)": order.component1,
        "Componente 2 (%)": order.component2
    }])

    filename = f"receita_{order.client}_{order.film_type}.csv"
    filepath = os.path.join("/tmp", filename)
    df.to_csv(filepath, index=False)

    try:
        ftp = FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FTP_DEST_DIR)
        with open(filepath, "rb") as f:
            ftp.storbinary(f"STOR {filename}", f)
        ftp.quit()
        print(f"Arquivo {filename} enviado com sucesso!")
    except Exception as e:
        print(f"Erro no envio FTP: {e}")
