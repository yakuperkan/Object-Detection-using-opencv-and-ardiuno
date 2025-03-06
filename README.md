# Object-Detection-using-opencv-and-ardiuno
# Savunma Sanayi için Yapay Zeka ve Servo Kontrol Projesi

Bu repo, savunma sanayi uygulamaları için geliştirilmiş iki temel projeyi içermektedir: 
1. **Nesne Tespiti ve Takibi** (object_detection.py)
2. **Servo Motor Kontrolü** (servo2.ino)

---

## 🎯 Proje 1: Nesne Tespiti ve Takibi

### 📄 **Açıklama:**
Bu proje, OpenCV kullanarak kameradan alınan görüntüde kırmızı renkli nesneleri tespit eder ve merkez koordinatlarını belirler. Belirlenen koordinatlar, Arduino'ya gönderilerek servo motor kontrolü sağlanır.

### 🚀 **Kullanılan Teknolojiler:**
- **Python**
- **OpenCV**
- **Arduino** (Serial haberleşme)
- **Kamera** (Webcam kullanımı)

### 📂 **Dosya:**
- `object_detection.py`: Görüntü işleme ve seri haberleşme kodunu içerir.

### ⚙️ **Kurulum ve Kullanım:**
1. Gerekli kütüphaneleri yükleyin:
```bash
pip install opencv-python pyserial numpy
```
2. Arduino'yu `COM4` portuna bağlayın ve servo motorun bağlantılarını yapın.
3. `object_detection.py` dosyasını çalıştırın:
```bash
python object_detection.py
```
4. Kırmızı renkli nesneyi kameraya gösterin ve servo motorun hareketini gözlemleyin.

---

## 🔧 Proje 2: Servo Motor Kontrolü

### 📄 **Açıklama:**
Bu proje, Arduino üzerinde servo motorun belirli koordinatlara göre hareket etmesini sağlar. Görüntü işleme projesi ile entegre çalışarak, nesne tespit edildiğinde servo motor pozisyonunu otomatik olarak ayarlar.

### 🚀 **Kullanılan Teknolojiler:**
- **Arduino IDE**
- **Servo Kütüphanesi**
- **Serial Haberleşme**

### 📂 **Dosya:**
- `servo2.ino`: Arduino tarafında servo motor kontrolünü sağlayan kodu içerir.

### ⚙️ **Kurulum ve Kullanım:**
1. Arduino IDE'yi açın ve `servo2.ino` dosyasını yükleyin.
2. Arduino'nun `COM4` portuna bağlı olduğundan emin olun.
3. Servo motorun doğru bağlantılarını kontrol edin (PWM pinine bağlayın).

---

## 📧 İletişim
- **Geliştirici:** Yakup Erkan Kaymaz
- **E-posta:** kaymazyakuperkan@gmail.com

Eğer bu projeyi kullanırken bir sorunla karşılaşırsanız veya katkı sağlamak isterseniz, benimle iletişime geçmekten çekinmeyin!
