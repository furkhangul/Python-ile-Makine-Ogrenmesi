"""
Yanlış Pozitif (False Positive) ve Yanlış Negatif (False Negative) Nedir?

İkili sınıflandırmalarda test sonuçları 4 şekilde olabilir:
- Gerçek Pozitif (True Positive)
- Gerçek Negatif (True Negative)
- Yanlış Pozitif (False Positive)
- Yanlış Negatif (False Negative)

1. Yanlış Pozitif (False Positive - FP):
Test, olmayan bir durumu varmış gibi gösterir.
Örnek: Hamile olmayan bir kişiye pozitif hamilelik testi sonucu çıkması.
Bu durum Tip I hata olarak da bilinir.

2. Yanlış Negatif (False Negative - FN):
Test, olan bir durumu yokmuş gibi gösterir.
Örnek: Hamile olan bir kişiye negatif test sonucu çıkması.
Bu durum Tip II hata olarak da bilinir.

İstatistiksel Hipotez Testi ile İlişkisi:
- Tip I Hata (α): Gerçekte yanlış olan sıfır hipotezini reddetme. (Yanlış pozitif)
- Tip II Hata (β): Gerçekte doğru olan alternatif hipotezi reddetme. (Yanlış negatif)

Ölçüm Metrikleri:
- Yanlış Pozitif Oranı (False Positive Rate - FPR): 
  Gerçekte negatif olanlar arasında testin pozitif çıktığı oran.
  FPR = FP / (FP + TN)

- Yanlış Negatif Oranı (False Negative Rate - FNR):
  Gerçekte pozitif olanlar arasında testin negatif çıktığı oran.
  FNR = FN / (FN + TP)

- Özgüllük (Specificity) = 1 - FPR
- Duyarlılık (Sensitivity / Recall) = 1 - FNR
- Testin Gücü (Power) = 1 - β

Ekstra: Yanlış Pozitif Risk (False Positive Risk - FPR):
Bir sonucun yanlış pozitif olma olasılığı. p-değerinden farklıdır.
p = 0.001 bile olsa, öncül varsayımlar zayıfsa yanlış pozitif riski yüksek olabilir.

Colquhoun’un uyarısı:
p-değerleri, bir etkinin gerçekten var olduğu konusunda tek başına yeterli kanıt değildir.
Örnek: p = 0.05 gözlemlendiyse, %5’lik yanlış pozitif riski elde etmek için deneyden önce
gerçek etkinin %87 olasılıkla var olduğunu varsaymalıyız.
"""
