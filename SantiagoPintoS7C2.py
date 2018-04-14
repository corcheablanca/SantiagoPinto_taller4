
import numpy as np
import matplotlib.pyplot as plt


#codigo para la transformada de fourier.
N=128 #numero de puntos
f=200.0 #frecuencia en Hz
dt=1.0/(f*32.0)
t = np.linspace( 0.0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )
furier=[]
ts=np.linspace(0.0,N,N)

def func(y):
	for i in range(N):
		suma=0
		c= ((1j)*(-2.0)*(np.pi)*(ts)*(float(i)/(N)))
		suma = np.sum((y*(np.exp(c))))
		furier.append((suma))
	return np.array(furier)


from scipy.fftpack import fft,fftfreq
freq=fftfreq((N),dt)
f=func(y)/N
#f=fft(y)/N
plt.plot(freq, abs(f))
plt.show()

		
#codigo para cargar la imagen.
imagen=plt.imread("imagen.png")
plt.figure()
#plt.imshow(imagen)
#plt.show()
#print np.shape(imagen)

"""#codigo para generar un kernel gaussiano
t=np.linspace(-10,10,20)
bump=(0.1*t**2)
bump=bump/np.trapz(bump)
kernel=bump[:,np.mewaxis]*bump[np.newaxis,:]"""


#codigo para poner la transformada en dos dimesiones.
"""tsu=np.linspace(0.0,N,N)
tsv=np.linspace(0.0,M,M)
matrix=[]
def func(y):
	for i in range(N):
		for z in range (M)
		suma=0
		c= (1j)*(-2.0)*(np.pi)*((tsu)*((float(i)/float(N))+(tsv)*((float(z)/float(M)))

		suma = np.sum(y*(np.exp(c)))

		matrix[N,M]=((suma)/float(N))
		
	
	#para recuperar las frecuencias
	return furier"""




	
