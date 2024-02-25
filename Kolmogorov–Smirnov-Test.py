from scipy.stats import expon, kstest
import numpy as np

# Örnek veri oluştur (üstel dağılıma uygun)
np.random.seed(42)
data = expon.rvs(scale=1/0.5, size=10000)

# KS testini gerçekleştir
lambd = 1 / np.mean(data)
ks_statistic, ks_p_value = kstest(data, 'expon', args=(0, 1/lambd))

# Sonuçları yazdır
print(f"KS Statistic: {ks_statistic}")
print(f"P-value: {ks_p_value}")

# H0 hipotezi test istatistiği ile P-değeri kullanılarak değerlendirilir
alpha = 0.05
if ks_p_value < alpha:
    print("The H0 hypothesis is rejected: The data set does not fit an exponential distribution.")
else:
    print("H0 hypothesis is accepted: The data set fits an exponential distribution.")
