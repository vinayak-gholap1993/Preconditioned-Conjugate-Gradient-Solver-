import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt("residuals_64.csv", delimiter=",")
data2 = np.loadtxt("residuals_128.csv", delimiter=",")
data3 = np.loadtxt("residuals_192.csv", delimiter=",")
data4 = np.loadtxt("residuals_256.csv", delimiter=",")
data5 = np.loadtxt("residuals_320.csv", delimiter=",")
data6 = np.loadtxt("residuals_384.csv", delimiter=",")

plt.semilogy(data1[:,0], data1[:,1],'b',label='64*64')
plt.semilogy(data2[:,0], data2[:,1],'r',label='128*128')
plt.semilogy(data3[:,0], data3[:,1],'g',label='192*192')
plt.semilogy(data4[:,0], data4[:,1],'k',label='256*256')
plt.semilogy(data5[:,0], data5[:,1],'c',label='320*320')
plt.semilogy(data6[:,0], data6[:,1],'y',label='384*384')

plt.xlabel("Iteration")
plt.ylabel("Relative Residual")
plt.grid(True)
plt.legend()
#plt.show()
plt.savefig("RelativeResidualIteration.pdf")
