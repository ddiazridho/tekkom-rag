import pandas as pd

from helpers import Helper
from config import NAMA_PRODI

def hapus_gelar(nama: str) -> str:
    gelar = {'Prof.', 'Dr.', 'Ir.', 'S.T.', 
             'M.T.', 'M.Sc.', 'M.Eng.', 'M.Kom.', 
             'S.Kom', 'S.Si', 'S.Si.', 'S.H', 'S.H.', 
             'Eng.', 'Dr.Eng.', 'Dra.', 'Drs.'}
    
    if not nama or nama.strip() == '':
        raise ValueError("Nama tidak boleh kosong")
    
    sampel = nama.split(',')[0].split()
    sampel = [nama for nama in sampel if nama not in gelar]
    return ' '.join(sampel)

def ubah_kolom_standar(kategori: str, df: pd.DataFrame) -> pd.DataFrame:
    kolom_khusus = 'keahlian' if kategori == 'dalam' else 'pengampu'
    df.columns = ['nama_dosen', kolom_khusus, 'foto_profil', 'profil_sinta', 'publikasi', 'profil_google_scholar']
    return df

def buat_meta_data(row: pd.DataFrame, *, kategori: str, nama_dosen: str, sumber_file: str) -> dict:
    meta = {"tipe": "profil_dosen", 
            "kategori_dosen": kategori, 
            "nama": nama_dosen,
            "sumber_file": sumber_file}
        
    for key in ('foto_profil', 'profil_sinta', 'publikasi', 'profil_google_scholar'):
        meta[key] = row[key] 

    return meta

def buat_dokumen_profil_dosen(df: pd.DataFrame, *, kategori:str , sumber_file: str, nama_prodi: str):
    # Merapikan semua isi di dalam Dataframe
    df = df.map(Helper.rapikan_teks)

    # Mengubah nama kolom menjadi seragam
    df = ubah_kolom_standar(kategori, df)

    # Membuat wadah untuk menampung dictionary data bersih
    dokumen = []

    for _, row in df.iterrows():
        # Simpan data nama ke variabel sementara
        nama_dosen = row['nama_dosen'] if row["nama_dosen"] != "" else ""

        if nama_dosen == "":
            continue

        # Simpan kategori pengampu atau keahlian ke variabel sementara
        kolom_khusus = 'pengampu' if kategori == 'luar' else 'keahlian'
        nilai_khusus = row[kolom_khusus]

        baris = (f"Nama: {nama_dosen},\n"
                f"Nama tanpa gelar: {hapus_gelar(nama_dosen)},\n"
                f"Kategori: Dosen {kategori}\n"
                f"Pengampu: {nilai_khusus}")
        
        teks = (f"{nama_dosen} adalah dosen {kategori} di Program Studi {nama_prodi} yang mengampu mata kuliah {nilai_khusus}.\n\n"
                + "\n".join(baris))

        # Membuat metadata untuk setiap data
        meta = buat_meta_data(row, 
                              kategori=kategori, 
                              nama_dosen=nama_dosen, 
                              sumber_file=sumber_file)

        # Menggabungkan data ke dokumen
        dokumen.append({"teks": teks, 
                        "meta": meta, 
                        "slug": f"dosen-{kategori}-{Helper.buat_slug(hapus_gelar(nama_dosen))}"})
        
    return dokumen
