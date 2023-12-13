import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os


with open('survey.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

# Prediksi penyakit berdasarkan gejala yang diberikan pengguna
gejala_pengguna = [0] * 61
for i in range(1):

  #Penyakit 2 Masitis
  a=input("Apakah Anda pernah mengamati perubahan warna pada air susu sapi menjadi kekuning-kuningan? ")
  if a == "y":
    gejala_pengguna[52]=1
    a=input("Apakah frekuensi pernafasan sapi meningkat, di luar rentang normal 24-42 kali/menit? ")
    if a == "y":
      gejala_pengguna[2]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    a=input("Apakah sapi mengalami dehidrasi? ")
    if a == "y":
      gejala_pengguna[4]=1
    a=input("Apakah sapi terlihat lemah dan kurang aktif? ")
    if a == "y":
      gejala_pengguna[5]=1
    a=input("Apakah sapi gelisah, sering bangun dan duduk kembali secara berulang, serta sensitif terhadap interaksi dengan manusia? ")
    if a == "y":
      gejala_pengguna[6]=1
    a=input("Apakah produksi susu sapi menurun di bawah normal sekitar 12-15 liter/hari? ")
    if a == "y":
      gejala_pengguna[14]=1
    a=input("Apakah sapi mengalami demam? ")
    if a == "y":
      gejala_pengguna[0]=1
    a=input("Apakah pernah ada kasus susu sapi yang menggumpal pada sapi Anda? ")
    if a == "y":
      gejala_pengguna[53]=1
    a=input("Apakah ada keluhan pada puting sapi, seperti keluarnya darah dan nanah? Apakah ada tanda-tanda infeksi?" )
    if a == "y":
      gejala_pengguna[54]=1
    a=input("Apakah ada perubahan pada bentuk / ukuran pada ambing sapi? Apakah ada tanda-tanda peradangan? ")
    if a == "y":
      gejala_pengguna[55]=1
    a=input("Apakah ambing sapi terasa sakit dan panas saat disentuh? ")
    if a == "y":
      gejala_pengguna[56]=1
    break

  #Penyakit 3 Pneumonia
  a=input("Apakah sapi mengalami batuk? ")
  if a == "y":
    gejala_pengguna[13]=1
    a=input("Apakah sapi mengalami demam? ")
    if a == "y":
      gejala_pengguna[0]=1
    a=input("Apakah frekuensi pernafasan sapi meningkat, di luar rentang normal 24-42 kali/menit? ")
    if a == "y":
      gejala_pengguna[2]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    a=input("Apakah sapi mengalami dehidrasi? ")
    if a == "y":
      gejala_pengguna[4]=1
    a=input("Apakah sapi terlihat lemah dan kurang aktif? ")
    if a == "y":
      gejala_pengguna[5]=1
    a=input("Apakah sapi gelisah, sering bangun dan duduk kembali secara berulang, serta sensitif terhadap interaksi dengan manusia?")
    if a == "y":
      gejala_pengguna[6]=1
    a=input("Apakah terdapat keluarnya cairan atau lendir dari hidung sapi? ")
    if a == "y":
      gejala_pengguna[7]=1
    break

  #Penyakit 4 Hipocalcemia
  a=input("Apakah suhu tubuh sapi rendah? ")
  if a == "y":
    gejala_pengguna[1]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    a=input("Apakah sapi gelisah, sering bangun dan duduk kembali secara berulang, serta sensitif terhadap interaksi dengan manusia?")
    if a == "y":
      gejala_pengguna[6]=1
    a=input("Apakah sapi terlihat beringas? ")
    if a == "y":
      gejala_pengguna[12]=1
    a=input("Akhir-akhir ini, Apakah  sapi Anda pernah tidak buang air kecil dan buang air besar sama sekali? ")
    if a == "y":
      gejala_pengguna[26]=1
    a=input("Apakah sapi Anda sulit bergerak dan berdiri(terlihat pincang)? ")
    if a == "y":
      gejala_pengguna[30]=1
    a=input("Apakah kaki belakang sapi Anda terlihat lemah dan sulit bergerak? ")
    if a == "y":
      gejala_pengguna[31]=1
    a=input("Apakah kaki dan telinga sapi Anda dingin? ")
    if a == "y":
      gejala_pengguna[32]=1
    a=input("Akhir-akhir ini, Apakah sapi Anda tertidur/beristirahat dengan berbaring pada salah satu sisi? ")
    if a == "y":
      gejala_pengguna[37]=1
    a=input("Apakah kepala sapi Anda mengarah ke belakang membentuk huruf “S”?")
    if a == "y":
      gejala_pengguna[38]=1
    a=input("Apakah Anda mengamati bahwa sapi kurang responsif terhadap lingkungan sekitar dan ada perubahan perilaku yang mencolok? ")
    if a == "y":
      gejala_pengguna[46]=1
    break

  #Penyakit 7 Diare
  a=input("Apakah bulu sapi terlihat kusam?")
  if a == "y":
    gejala_pengguna[18]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    a=input("Apakah sapi mengalami dehidrasi? ")
    if a == "y":
      gejala_pengguna[4]=1
    a=input("Apakah sapi terlihat lemah dan kurang aktif? ")
    if a == "y":
      gejala_pengguna[5]=1
    a=input("Apakah terdapat keluarnya cairan atau lendir dari hidung sapi? ")
    if a == "y":
      gejala_pengguna[7]=1
    a=input("Apakah sapi mengalami keluarnya cairan dari mata? ")
    if a == "y":
      gejala_pengguna[8]=1
    a=input("Apakah sapi mengalami bulu rontok? ")
    if a == "y":
      gejala_pengguna[16]=1
    a=input("Apakah kulit dan bulu sapi terasa kaku? ")
    if a == "y":
      gejala_pengguna[17]=1
    a=input("Apakah tubuh sapi anda terlihat kurus (tulang rusuk hampir terlihat) ? ")
    if a == "y":
      gejala_pengguna[21]=1
    a=input("Akhir-akhir ini, Apakah  sapi Anda buang air besar lebih sering dari biasanya? ")
    if a == "y":
      gejala_pengguna[25]=1
    a=input("Apakah kotoran sapi Anda lembek,berwarna gelap, disertai lendir sampai cair? ")
    if a == "y":
      gejala_pengguna[27]=1
    a=input("Apakah ada darah atau cacing di kotoran sapi Anda? ")
    if a == "y":
      gejala_pengguna[28]=1
    a=input("Apakah sapi Anda sering merengek atau merintih? ")
    if a == "y":
      gejala_pengguna[29]=1
    a=input("Akhir-akhir ini, Apakah sapi Anda berjalan sempoyongan bahkan sampai pernah ambruk? ")
    if a == "y":
      gejala_pengguna[33]=1
    a=input("Apakah punggung sapi terlihat melengkung? ")
    if a == "y":
      gejala_pengguna[43]=1
    break

  #Penyakit 10 Cacingan
  a=input("Apakah mulut sapi kering? ")
  if a == "y":
    gejala_pengguna[10]=1
    a=input("Apakah frekuensi pernafasan sapi meningkat, di luar rentang normal 24-42 kali/menit? ")
    if a == "y":
      gejala_pengguna[2]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    a=input("Apakah sapi mengalami dehidrasi? ")
    if a == "y":
      gejala_pengguna[4]=1
    a=input("Apakah sapi terlihat lemah dan kurang aktif? ")
    if a == "y":
      gejala_pengguna[5]=1
    a=input("apakah10")
    if a == "y":
      gejala_pengguna[9]=1
      a=input("Apakah detak jantung sapi meningkat di luar rentang normal sekitar 60-70 kali/menit? ")
    if a == "y":
      gejala_pengguna[11]=1
    a=input("Apakah sapi mengalami suhu tubuh naik dan turun? ")
    if a == "y":
      gejala_pengguna[15]=1
    a=input("Apakah sapi mengalami bulu rontok? ")
    if a == "y":
      gejala_pengguna[16]=1
    a=input("Apakah kulit dan bulu sapi terasa kaku? ")
    if a == "y":
      gejala_pengguna[17]=1
    a=input("Apakah tubuh sapi anda terlihat kurus (tulang rusuk hampir terlihat) ? ")
    if a == "y":
      gejala_pengguna[21]=1
      a=input("Akhir-akhir ini, Apakah  sapi Anda buang air besar lebih sering dari biasanya? ")
    if a == "y":
      gejala_pengguna[25]=1
    a=input("Akhir-akhir ini, Apakah sapi Anda berjalan sempoyongan bahkan sampai pernah ambruk? ")
    if a == "y":
      gejala_pengguna[33]=1
    a=input("Apakah telinga sapi Anda terkulai(Tergantung lemah)? ")
    if a == "y":
      gejala_pengguna[34]=1
    a=input("Akhir-akhir ini, Apakah mata sapi Anda terlihat mengantuk (mata suram dan cekung) ? ")
    if a == "y":
      gejala_pengguna[35]=1
    break

  #Penyakit 9 Kembung
  a=input("Apakah dibagian perut sapi anda terlihat cekung(legok) ? ")
  if a == "y":
    gejala_pengguna[22]=1
    a=input("Apakah frekuensi pernafasan sapi meningkat, di luar rentang normal 24-42 kali/menit? ")
    if a == "y":
      gejala_pengguna[2]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    a=input("Apakah sapi terlihat lemah dan kurang aktif? ")
    if a == "y":
      gejala_pengguna[5]=1
    a=input("Apakah sapi gelisah, sering bangun dan duduk kembali secara berulang, serta sensitif terhadap interaksi dengan manusia? ")
    if a == "y":
      gejala_pengguna[6]=1
    a=input("apakah10")
    if a == "y":
      gejala_pengguna[9]=1
    a=input("Apakah akhir-akhir ini sapi anda berat badannya menurun ? ")
    if a == "y":
      gejala_pengguna[20]=1
    a=input("Apakah dibagian perut sapi anda terlihat cekung(legok) ? ")
    if a == "y":
      gejala_pengguna[22]=1
    a=input("Akhir-akhir ini, Apakah sapi anda pernah muntah ? ")
    if a == "y":
      gejala_pengguna[23]=1
    a=input("Akhir-akhir ini, Apakah  sapi anda buang air kecil lebih sering dari biasanya? ")
    if a == "y":
      gejala_pengguna[24]=1
    a=input("Akhir-akhir ini, Apakah sapi Anda sering menghentakkan kakinya dan sering mengais-ais perutnya? ")
    if a == "y":
      gejala_pengguna[36]=1
    a=input("Apakah sapi sering bernafas dengan mulut terbuka dan ada tanda-tanda kesulitan bernafas? ")
    if a == "y":
      gejala_pengguna[44]=1
    a=input("Apakah  sapi lebih cenderung melakukan perilaku memanjangkan leher? ")
    if a == "y":
      gejala_pengguna[45]=1
    break

  #Penyakit  Skabies/LSD
  a=input("Apakah sapi Anda sering menggigit bagian tubuhnya? ")
  if a == "y":
    gejala_pengguna[39]=1
    a=input("Apakah sapi mengalami bulu rontok? ")
    if a == "y":
      gejala_pengguna[16]=1
    a=input("Apakah kulit dan bulu sapi terasa kaku? ")
    if a == "y":
      gejala_pengguna[17]=1
    a=input("Apakah Anda pernah melihat sapi menggosok-gosokkan badannya pada kandang dan ada area tertentu yang tampak sakit atau gatal? ")
    if a == "y":
      gejala_pengguna[40]=1
    a=input("Apakah ada bagian tubuh sapi yang mengeluarkan nanah? ")
    if a == "y":
      gejala_pengguna[41]=1
    a=input("Apakah Anda pernah melihat sapi dengan gejala timbulnya kerak berwarna abu-abu atau keropeng pada kulit? ")
    if a == "y":
      gejala_pengguna[42]=1
    break

  #Penyakit 5 BEF
  a=input("Apakah sapi anda terlihat gemetaran ? ")
  if a == "y":
    gejala_pengguna[19]=1
    a=input("Apakah sapi mengalami demam? ")
    if a == "y":
      gejala_pengguna[0]=1
    a=input("Apakah frekuensi pernafasan sapi meningkat, di luar rentang normal 24-42 kali/menit? ")
    if a == "y":
      gejala_pengguna[2]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    a=input("Apakah sapi mengalami dehidrasi? ")
    if a == "y":
      gejala_pengguna[4]=1
    a=input("Apakah sapi terlihat lemah dan kurang aktif? ")
    if a == "y":
      gejala_pengguna[5]=1
    a=input("Apakah terdapat keluarnya cairan atau lendir dari hidung sapi? ")
    if a == "y":
      gejala_pengguna[7]=1
    a=input("Apakah sapi mengalami keluarnya cairan dari mata? ")
    if a == "y":
      gejala_pengguna[8]=1
    a=input("Apakah detak jantung sapi meningkat di luar rentang normal sekitar 60-70 kali/menit? ")
    if a == "y":
      gejala_pengguna[11]=1
    a=input("Apakah produksi susu sapi menurun di bawah normal sekitar 12-15 liter/hari? ")
    if a == "y":
      gejala_pengguna[14]=1
    a=input("apakah20")
    if a == "y":
      gejala_pengguna[19]=1
    a=input("Apakah sapi Anda sulit bergerak dan berdiri(terlihat pincang)? ")
    if a == "y":
      gejala_pengguna[30]=1
    break

  #Penyakit PMK
  a=input("apakah59")#KG04
  if a == "y":
    gejala_pengguna[58]=1
    a=input("Apakah sapi mengalami demam? ")
    if a == "y":
      gejala_pengguna[0]=1
    a=input("Apakah sapi anda mengalami melepuh pada mulut dan kaki? ") #KG10
    if a == "y":
      gejala_pengguna[59]=1
    a=input("Apakah sapi anda mengalami luka pada kuku dan kukunya lepas? ") #KG08
    if a == "y":
      gejala_pengguna[60]=1
    a=input("Apakah sapi mengalami penurunan nafsu makan? ")
    if a == "y":
      gejala_pengguna[3]=1
    break


  #Penyakit 1 Brucellosis
  a=input("pada sapi betina, Apakah pernah terjadi kejadian di mana sapi kehilangan kehamilan pada usia 6-9 bulan? ")
  if a == "y":
    gejala_pengguna[47]=1
    a=input("Apakah Anda pernah melihat pendarahan keluar dari vagina sapi? ")
    if a == "y":
      gejala_pengguna[28]=1
    a=input("Apakah ada kasus kehilangan kehamilan berulang pada sapi dalam kurun waktu 2 tahun setelah kehilangan kehamilan sebelumnya?" )
    if a == "y":
      gejala_pengguna[49]=1
    a=input("Apakah Anda pernah mengamati ada tanda-tanda gangguan pada alat reproduksi sapi? ")
    if a == "y":
      gejala_pengguna[50]=1
    a=input("Apakah Anda pernah mengamati adanya pembesaran pada kantong persendian sapi, atau gejala yang dikenal sebagai higroma? dan apakah terdapat tanda-tanda peradangan atau ketidaknyamanan pada area tersebut? ")
    if a == "y":
      gejala_pengguna[51]=1
    break


  #Penyakit 8 Paratubercolosis
  a=input("apakah61")
  if a == "y":
    gejala_pengguna[57]=1
    a=input("Apakah sapi gelisah, sering bangun dan duduk kembali secara berulang, serta sensitif terhadap interaksi dengan manusia? ")
    if a == "y":
      gejala_pengguna[6]=1
    a=input("Apakah produksi susu sapi menurun di bawah normal sekitar 12-15 liter/hari? ")
    if a == "y":
      gejala_pengguna[14]=1
    a=input("Apakah akhir-akhir ini sapi anda berat badannya menurun ? ")
    if a == "y":
      gejala_pengguna[20]=1
    a=input("Akhir-akhir ini, Apakah  sapi Anda buang air besar lebih sering dari biasanya? ")
    if a == "y":
      gejala_pengguna[25]=1
    break

#Pengobatan
pengobatan = {
  "BEF" : "Pengobatan dilakukan simtomatik dan pencegahan terhadap infeksi sekunder dengan antibiotik yang dilakukan oleh petugas yang berwenang.",
  "Brucellosi" : "Dilakukan vaksinasi terhadap ternak yang terjangkit brucellosis Dilakukan uji Red Bengal Test (RBT) dan uji Complement Fixation Test (CFT). Apabila kedua tes mendapatkan hasil positif, maka dilakukan Test and Slaughter.",
  "Cacingan" : "Obat yang biasanya digunakan oleh dokter hewan adalah dalam jenis benzimidazol, Imida-thiazol dan Avermectin (konsultasi dengan dokter hewan sebelum menggunakan).",
  "Masitis" : "Menjaga kandang untuk tetap bersih. Memakai antiseptik guna pencelupan puting susu saat sebelum dan setelah pemerahan. Memberikan antibiotik berspek trum misalnya peniciline - streptomicine atau Suanovil (spiramycine).",
  "Pneumonia" :"Pencegahan yang dapat dilakukan dengan melakukan sanitasi kandang yang benar, dan pisahkan sapi yang sakit pada kandang karantina. Pengobatan dilakukan dengan memberikan vaksin antibiotik untuk memutus siklus pertumbuhan penyebab pneumonia seperti vaksin Ca boroglukonat dan vitamin C, sulfonamid.",
  "Hipocalcemi" : "Pengobatan dilakukan dengan cara menyuntikkan garam berkalsium lengkap seperti larutan kalsium klorida 10%, larutan kalsium boroglukonat 20-30%, dan campuran berbagai sediaan kalsium seperti Calphon Forte, Calfosal atau Calcitad-50.",
  "Skabies/LSD" : "Memberikan minyak kelapa dicampur dengan kapur barus kemudian digosokkan pada kulit yang terkena skabies.",
  "Diare" : "Untuk menggantikan cairan tubuh yang hilang akibat diare pada ternak dapat diberikan cairan elektrolit terutama air, bikarbonat, sodium, dan potassium atau larutan garam agar tidak terjadi dehidrasi yang lebih lanjut.",
  "Paratubercolosis" : "Hewan-hewan yang positif MAP harus diafkir sesegera mungkin dan seluruh hewan harus dilakukan pengujian kembali dengan kombinasi uji yang berbeda.",
  "Kembung" : "Memberikan anti bloat yang mengandung dimethicone serta minyak nabati yang berasal dari kacang tanah. Minyak nabati bisa disuntikkan pada sapi yang terkena bloat. Atau dapat di konsultasikan pada dokter hewan untuk pemakaian obat yang cocok.",
  "PMK" : "masih ksg"
}

#label_penyakit = ['Brucellosis', 'Masitis', 'Pneumonia', 'Hipocalcemi', 'BEF', 'Skabies/LSD', 'Diare', 'Paratubercolosis', 'Kembung', 'Cacingan']

#urutan_kelas = loaded_data.classes_
#print("Urutan Kelas:", urutan_kelas)
"""# **Hasil**"""

hasil_prediksi = loaded_data.predict([gejala_pengguna])
#print("matrix gejala: ",gejala_pengguna)
#print("Berdasarkan gejala yang dimasukkan, kemungkinan Anda mengalami:", hasil_prediksi, "dengan akurasi ", clf.predict_proba([gejala_pengguna]))
# Misalkan probabilitas_prediksi adalah hasil dari clf.predict_proba([gejala_pengguna])
n=0
for i in gejala_pengguna:
  n +=i
if n >2:
  probabilitas_prediksi=loaded_data.predict_proba([gejala_pengguna])
  threshold = 0.2  # Tentukan threshold yang diinginkan

  # Ambil indeks kelas yang memiliki nilai probabilitas > threshold
  kelas_lebih_dari_threshold = [i for i, prob in enumerate(probabilitas_prediksi[0]) if prob > threshold]
else:
  kelas_lebih_dari_threshold = []
  print("\nMaaf gejala tidak menunjukkan adanya penyakit pada sapi anda")  # kalo gejala kurang dari 2



