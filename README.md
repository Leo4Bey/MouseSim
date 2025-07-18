# MouseSim

🎯 **MouseSim**, insan benzeri fare hareketlerini Python ile gerçekleştiren basit ve esnek bir simülasyon kütüphanesidir. Fare hareketlerine rastgelelik (noise), hızlanma/yavaşlama (easing), sapmalar ve tıklama işlevleri ekleyerek doğal görünen etkileşimler sağlar. / It is a simple and flexible simulation library in Python that performs human-like mouse movements. It adds randomness (noise), acceleration/deceleration (easing), deviations, and clicking functions to mouse movements to create natural-looking interactions.

## 🧠 Özellikler / Features

### Türkçe

- Hedefe doğrusal olmayan, insan benzeri fare hareketleri
- Easing (hızlanma ve yavaşlama) efektleri
- Ufak rastgele sapmalar (noise) — *insansı efektler*
- Hem **sol** hem **sağ** tıklama desteği
- Delay (gecikme) kontrolü
- Kütüphane içinde rahat kullanım için nesne yönelimli (OOP) yapı

### English

- Human-like mouse movement toward a target
- Easing effects for acceleration and deceleration
- Subtle randomness (noise) to simulate human error
- Left and right click support
- Control over delay and movement speed
- Object-oriented structure for clean integration

---

## 📦 Kurulum / Installation

> PyPI’ye yüklendiğinde:  
```bash
pip install MouseSim
```


---

## 🧪 Kullanım Örnekleri / Usage Examples

```python
from mice_sim import MouseSim
import time, random, math

# MouseSim objesini oluşturun / Create a MouseSim instance
ms = MouseSim(noise_range=3, base_delay=0.01)

# 1. Move the cursor / İmleci Hareket Ettirme
# Türkçe: İmleci (500, 300) koordinatlarına yumuşakça taşı
# English: Move the cursor to (500, 300) smoothly
ms.move(500, 300, steps=120)

# 2. Single Click / Tek Tıklama
# Türkçe: Mevcut imleç konumunda sol tıklama yap
# English: Perform a left click at current cursor position
ms.left_click()

# 3. Double Click / Çift Tıklama
# Türkçe: 0.2 saniye aralıkla çift tıklama yap
# English: Perform a double click with 0.2 seconds interval
ms.double_click(interval=0.2)

# 4. Right Click / Sağ Tıklama
# Türkçe: Sağ tıklama yap
# English: Perform a right click
ms.right_click()

# 5. Middle Click / Orta Tıklama
# Türkçe: Orta (tekerlek) tıklaması yap
# English: Perform a middle (wheel) click
ms.middle_click()

# 6. Click and Hold / Tıklayıp Basılı Tutma
# Türkçe: Sol fare tuşuna basılı tut
# English: Press and hold the left mouse button
ms.left_click_and_hold()
# English: Release the left mouse button
# Türkçe: Sol fare tuşunu bırak
ms.left_release_click()

# 7. Scroll / Kaydırma
# Türkçe: Kaydırma yap, pozitif yukarı, negatif aşağı
# English: Scroll up or down, positive for up, negative for down
ms.scroll(amount=120)  # Scroll up
ms.scroll(amount=-120) # Scroll down

# 8. Drag and Drop / Sürükle ve Bırak
# Türkçe: (100, 200) noktasından (400, 500) noktasına sürükle ve bırak
# English: Drag from (100, 200) to (400, 500)
ms.drag_and_drop(100, 200, 400, 500, steps=150)
```

---

## 📚 Parametreler Açıklaması / Parameters Explained

### `duration: float`
- Fare hareketinin kaç saniyede tamamlanacağını belirler.
- Varsayılan: `1.0` saniye

### `noise_range: int`
- Her adımda koordinata eklenen rastgele ± değer.
- Örnek: `noise_range=2` ⇒ her adımda `-2` ile `+2` arasında sapma olur.
- İnsan elinin hassasiyetini taklit eder.

### `easing: bool`
- True olarak ayarlanırsa fare hareketi başta yavaş, ortada hızlı, sonda tekrar yavaş olur.
- Daha doğal bir hareket görünümü sağlar.

---

## 🖱️ "Notch" nedir?

**Notch**, fare hareketinde kullanılan küçük adımlardır. Örneğin:
- 1 "notch" = 1 piksel'lik hareket anlamına gelir.
- Kod içinde, fare her "notch"’ta bir konum değiştirir.
- Çok küçük değerler fareyi yavaş ve hassas, büyük değerler hızlı yapar.

---

## 📄 Lisans / License

MIT License. Tüm hakları saklıdır.

---

## 🧑‍💻 Geliştirici / Developer

**Kemal Sayıt**  
📍 Türkiye  
🔗 [https://www.linkedin.com/in/kemal-sayit/]

---

## 🇹🇷 Açıklama Notu

Bu kütüphane, bot programlamaları, otomasyon testlerindeki robot tespitini zorlaştırmak ve masaüstü etkileşimleri için kullanılabilir. Lütfen etik dışı alanlarda kullanmaktan kaçının.

---

## 🇬🇧 Disclaimer

This library can be used for bot programming, making automation tests harder to detect as robots, and for desktop interaction simulations. Please avoid using it in unethical contexts.
