import re
import pandas as pd

class Helper:
    @staticmethod
    def rapikan_teks(teks: str) -> str:
        if pd.isna(teks):
            return ""
        return re.sub(r"\s+", " ", teks).strip()

    @staticmethod
    def rapikan_daftar(teks: str) -> str:
        if pd.isna(teks):
            return ""
        t = re.sub(r"[\r\n]+", ";", str(teks))
        return t.strip()

    @staticmethod
    def buat_slug(nama: str) -> str:
        if (nama == ""):
            raise ValueError("Nama tidak boleh kosong")
        
        slug = nama.lower().split(' ')
        return '-'.join(slug)

    @staticmethod
    def nama_tanpa_gelar(nama: str) -> str:
        gelar = {'Prof.', 'Dr.', 'Ir.', 'S.T.', 'M.T.', 'M.Sc.', 'M.Eng.', 'M.Kom.', 'S.Kom', 'S.Si', 'S.Si.', 'S.H', 'S.H.', 'Eng.', 'Dr.Eng.', 'Dra.', 'Drs.'}

        nama = nama.split(",")[0].split(" ")
        nama = [kata for kata in nama if kata not in gelar]
        return " ".join(nama)