import matplotlib.pyplot as plt

epochs = list(range(1, 21))
rmse_bias = [1.0048, 0.9776, 0.9654, 0.9585, 0.9540, 0.9509, 0.9486, 0.9469, 0.9456, 0.9446, 0.9438, 0.9432, 0.9427, 0.9423, 0.9420, 0.9420, 0.9420, 0.9420, 0.9420, 0.9420]
rmse_uv = [2.5289, 1.2730, 1.0827, 1.0265, 1.0027, 0.9898, 0.9814, 0.9749, 0.9695, 0.9647, 0.9605, 0.9567, 0.9533, 0.9504, 0.9477, 0.9453, 0.9432, 0.9412, 0.9394, 0.9377, ]
rmse_pmf = [1.5873, 1.2634, 1.1537, 1.0965, 1.0609, 1.0367, 1.0192, 1.0062, 0.9961, 0.9881, 0.9817, 0.9765, 0.9721, 0.9684, 0.9652, 0.9624, 0.9600, 0.9578, 0.9557, 0.9539]

plt.plot(epochs, rmse_bias, label="Biais uniquement")
plt.plot(epochs, rmse_uv, label="U/V uniquement")
plt.plot(epochs, rmse_pmf, label="PMF complet")
plt.xlabel("Époques")
plt.ylabel("RMSE (validation)")
plt.legend()
plt.title("Comparaison des modèles")
plt.grid(True)
plt.show()
