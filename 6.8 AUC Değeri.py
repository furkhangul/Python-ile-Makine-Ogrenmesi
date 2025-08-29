"""
AUC, ROC eğrisinin altında kalan alanı temsil eder ve modelin sınıflandırma başarısını tek bir
sayıyla özetler. 1'e yakın AUC değeri, modelin pozitif ve negatif sınıfları doğru şekilde
ayırabildiğini gösterir. 0.5 civarındaki AUC ise modelin rastgele tahmin yaptığı anlamına gelir.

AUC, modelin genel başarısını değerlendirmek için kullanışlıdır. Ancak sadece yüksek AUC değeri,
modelin güvenilir olduğu anlamına gelmez. Modelin neden o şekilde tahmin yaptığını anlayamazsak,
netlik paradoksu yine devreye girer. Bu nedenle AUC gibi metrikler, açıklanabilirlik yöntemleriyle
birlikte kullanılmalıdır.
"""
