"""
K-MEANS
Kümeleme yönteminin bir parçasıdır.

K-means, kaç küme olacağını kullanıcıdan parametre alarak seçer.
X-means ise biz seçmeden algoritma kendi kendine küme x tane küme oluşturur.

k-means, rastgele k tane merkez noktası seçer.
Uzayda rastgele 2 nokta belirler.

Bu seçilen merkez noktasından sonra bu noktalara en yakın komşu veriler
küme oluşturmaya başlar.Yani bütün noktalar en yakın değere atanır.

Daha sonra merkezler nokatalara yaklaştırmak adına ağırlık merkezlerinin olduğu
yere yani ortalarına doğru merkezi kaydırır.

Tekrardan uzaklık hesaplanabiliyor ve buna göre noktaların kümeleri değiştirilebilir.

Bu olaydan sonra tekrardan merkez kaydırılır. tekrar küme elemanları değiştirilir.
Stable yani kararlı olana kadar bu işlem devam etmektedir.
"""
