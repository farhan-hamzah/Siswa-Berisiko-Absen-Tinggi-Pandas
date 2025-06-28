import pandas as pd
data = {
    'nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka', 'Farah', 'Gilang', 'Hana'],
    'umur': [16, 17, 16, 17, 16, 15, 17, 15],
    'jenis_kelamin': ['L', 'L', 'P', 'P', 'L', 'P', 'L', 'P'],
    'nilai_matematika': [78, 65, 90, 80, 55, 88, 70, 95],
    'nilai_bahasa': [85, 70, 92, 78, 60, 89, 68, 94],
    'nilai_inggris': [88, 60, 95, 82, 50, 90, 75, 93],
    'absen': [2, 5, 1, 3, 8, 0, 4, 1]
}
dataKelas = pd.DataFrame(data)
laki = dataKelas[dataKelas['jenis_kelamin'] == 'L']
perempuan = dataKelas[dataKelas['jenis_kelamin'] == 'P']
rerataLaki = (laki['nilai_matematika'].mean() + laki['nilai_bahasa'].mean() + laki['nilai_inggris'].mean()) / 3
rerataPerempuan = (perempuan['nilai_matematika'].mean() + perempuan['nilai_bahasa'].mean() + perempuan['nilai_inggris'].mean()) / 3

