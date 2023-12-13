import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os
#import kelas_lebih_dari_threshold
#import hasil prediksi
from load_survey import kelas_lebih_dari_threshold, hasil_prediksi
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


with open('survey.pickle', 'rb') as file:
  loaded_data = pickle.load(file)
penyakit_gambar = ["Scabise/LSD", "Masitis", "Normal","PMK"]

for i in kelas_lebih_dari_threshold:
  #print("\nSapi anda memiliki gejala ", [loaded_data.classes_[i]])
  if loaded_data.classes_[i] in penyakit_gambar:
    def preprocess_image(file_path):
      img = image.load_img(file_path, target_size=(150, 150))  # Set your desired image size
      img_array = image.img_to_array(img)
      img_array = np.expand_dims(img_array, axis=0)
      return img_array

    def normalize_image(img_array):
      # Normalize pixel values to the range [0, 1]
      normalized_img = img_array / 255.0
      return normalized_img


    def predict_with_model(model, image_path):
      processed_image = preprocess_image(image_path)
      normalized_image = normalize_image(processed_image)
      predictions = model.predict(normalized_image)
      predicted_class = np.argmax(predictions, axis=1)
      return predicted_class


    model = load_model('cnn_penyakit.h5')  # Model CNN
    image_path = 'data/penyakitsapi/sapi/test/masitis'  # Gambar user disini

    for filename in os.listdir(image_path):
      f = os.path.join(image_path, filename)
    # checking if it is a file
      if os.path.isfile(f):
        predicted_class = predict_with_model(model, f)
        if penyakit_gambar[predicted_class[0]] in hasil_prediksi:
          print("Berdasarkan data dan gambar sapi anda memiliki gejala tinggi terkena ", penyakit_gambar[predicted_class[0]])  #kalo prediksi gambar sesuai dengan penyakit dari survey
          print("Cara pengobatan untuk penyakit " ,penyakit_gambar[predicted_class[0]], "adalah ", pengobatan[penyakit_gambar[predicted_class[0]]])
        else:
          for i in kelas_lebih_dari_threshold:
            print("\nBerdasarkan data dan gambar sapi anda memiliki gejala terkena:", [loaded_data.classes_[i]]) #kalo prediksi gambar tidak sesuai dengan penyakit dari survey
            print("Cara pengobatan untuk penyakit ", penyakit_gambar[predicted_class[i]], "adalah ", pengobatan[penyakit_gambar[predicted_class[i]]])
  else:
    print("\nBerdasarkan data dan gambar sapi anda memiliki gejala terkena:", [loaded_data.classes_[i]])
    print("Cara pengobatan untuk penyakit ",loaded_data.classes_[i], "adalah ",pengobatan[loaded_data.classes_[i]])









