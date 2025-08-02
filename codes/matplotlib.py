import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf_backend
from scipy.stats import f

degrees_of_freedom = [[1, 2], [2, 1], [5, 2], [100, 1], [100, 100]]
x = np.linspace(0, 5, 1000)
plt.figure(figsize=(12, 6))

for df in degrees_of_freedom:
    label = f'df={df[0]},{df[1]}'
    pdf = f.pdf(x, df[0], df[1])
    cdf = f.cdf(x, df[0], df[1])

    plt.subplot(1, 2, 1)
    plt.plot(x, pdf, label=label)

    plt.subplot(1, 2, 2)
    plt.plot(x, cdf, label=label)

plt.subplot(1, 2, 1)
plt.title("PDF - F-distribution")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()

plt.subplot(1, 2, 2)
plt.title("CDF - F-distribution")
plt.xlabel("x")
plt.ylabel("Probability")
plt.legend()

plt.tight_layout()
with pdf_backend.PdfPages('F_distribution_plots.pdf') as pdf: # 保存为PDF文件
    pdf.savefig()