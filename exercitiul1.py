import numpy as np

# Matricea cu examenele
matrice = np.array([[9, 6, 9],
                    [9, 9, 3],
                    [6, 6, 6],
                    [6, 6, 9],
                    [3, 3, 3]])

# Matricea de covarianta
cov_matrice = np.cov(matrice, rowvar=False, bias=True)

print("Matricea de covarianta:")
print(cov_matrice)

print("\nLegenda: 1=Matematica\n2=Fizica\n3=Chimie")
for i in range(3):
    for j in range(0, i):
        if (cov_matrice[i][j] == 0):
            print("Examenele necorelate sunt:", i, j)
        if (cov_matrice[i][j] > 0):
            print("Examenele: ", i, j, " sunt corelate in acelasi sens.")
        if (cov_matrice[i][j] < 0):
            print("Examenele: ", i, j, " sunt corelate in sensuri opuse.")
