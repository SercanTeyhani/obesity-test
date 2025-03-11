import pandas as pd
import joblib
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Modeli yükle
try:
    model = joblib.load('obesity_logistic_regression_model.pkl')  # .pkl uzantılı dosyayı joblib ile yükle
except FileNotFoundError:
    st.error("Model dosyası bulunamadı. Dosyanın mevcut olduğundan emin ol.")
except Exception as e:
    st.error(f"Model yüklenirken bir hata oluştu: {e}")

# Başlık
st.title('Obezite Tahmin Uygulaması')

# Kullanıcıdan veri girişi almak
age = st.number_input('Yaşınızı giriniz:', min_value=0.0, step=0.01, format="%.2f")
fcvc = st.number_input('Sebze Tüketim Sıklığı (1-3 arasında):', min_value=0.0, max_value=3.0, step=0.01, format="%.2f")
ch2o = st.number_input('Günlük Su Tüketimi (litre):', min_value=0.0, step=0.01, format="%.2f")
faf = st.number_input('Fiziksel Aktivite Sıklığı (saat):', min_value=0.0, step=0.01, format="%.2f")
bmi = st.number_input('BMI Değerini Girin:', min_value=0.0, step=0.01, format="%.2f")
tue = st.number_input('Düzenli Egzersiz Alışkanlıkları (saat):', min_value=0.0, step=0.01, format="%.2f")

# Kategorik değişkenler için seçim alanları
gender = st.selectbox('Cinsiyet:', ['Erkek', 'Kadın'])
family_history = st.selectbox('Ailede Aşırı Kilo Geçmişi Var mı?', ['Evet', 'Hayır'])
favc = st.selectbox('Yüksek Kalorili Yiyecek Tüketimi (FAVC):', ['Evet', 'Hayır'])
caec = st.selectbox('Öğün Aralarında Yiyecek Tüketimi (CAEC):', ['Sık Sık', 'Bazen', 'Hiç'])
smoke = st.selectbox('Sigara İçiyor Musunuz?', ['Evet', 'Hayır'])
scc = st.selectbox('Günlük Alınan Kalorileri Takip Ediyor musunuz?', ['Evet', 'Hayır'])
calcs = st.selectbox('Alkol Tüketimi (CALC):', ['Sık Sık', 'Bazen', 'Hiç'])
mtrans = st.selectbox('Kullandığınız Ulaşım Şekli:', ['Bisiklet', 'Motosiklet', 'Toplu Taşıma', 'Yürüyerek'])
ncp = st.number_input('Tüketim Alışkanlıkları (0-3 arasında):', min_value=0.0, max_value=3.0, step=0.01, format="%.2f")

# "Test Et" butonu ekle
if st.button('Test Et'):
    try:
        # Kullanıcıdan alınan verilerle bir DataFrame oluştur
        input_data = {
            'Gender': [1 if gender == 'Erkek' else 0],
            'Age': [age],
            'family_history': [1 if family_history == 'Evet' else 0],
            'FAVC': [1 if favc == 'Evet' else 0],
            'FCVC': [fcvc],
            'NCP': [ncp],
            'CAEC': [2 if caec == 'Sık Sık' else (1 if caec == 'Bazen' else 0)],
            'SMOKE': [1 if smoke == 'Evet' else 0],
            'CH2O': [ch2o],
            'SCC': [1 if scc == 'Evet' else 0],
            'FAF': [faf],
            'TUE': [tue],
            'CALC': [2 if calcs == 'Sık Sık' else (1 if calcs == 'Bazen' else 0)],
            'MTRANS': [0 if mtrans == 'Bisiklet' else (1 if mtrans == 'Motosiklet' else (2 if mtrans == 'Toplu Taşıma' else 3))],
            'BMI': [bmi],
        }

        input_df = pd.DataFrame(input_data)

        # Modeli kullanarak tahmin yap
        prediction = model.predict(input_df)[0]

        # Tahmin sonuçlarını eşle
        result_map = {
            0: 'Yetersiz Kilolu',
            1: 'Normal Kilolu',
            2: 'Obezite Tipi I',
            3: 'Obezite Tipi II',
            4: 'Obezite Tipi III',
            5: 'Aşırı Kilolu Seviye I',
            6: 'Aşırı Kilolu Seviye II'
        }

        st.success(f"Sonuç: {result_map.get(prediction, 'Bilinmeyen Tahmin')}")
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
