
import numpy as np
import matplotlib.pyplot as plt


#codigo para la transformada de fourier.
N=128 #numero de puntos
f=200.0 #frecuencia en Hz
dt=1.0/(f*32.0)
t = np.linspace( 0.0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )
furier=[]
frecuencias=[]
ts=np.linspace(0.0,N-1,N)

def func(y):
	
	for i in range(N):
		suma=0
		c= ((1j)*(-2.0)*(np.pi)*(ts)*(float(i)/(N)))
		suma = np.sum((y*(np.exp(c))))
		furier.append((suma))

		#recuperar la frecuencia
		if (i<N/2):
			frecuencias.append((float(i)/N*32*200))	
		if (i>=N/2):
			frecuencias.append((float(i)/N*32*200)-(32*200))	
	return np.array(furier)

fr= frecuencias
f = (func(y)/N)
#plt.plot(fr,abs(f))
#plt.show()


#importa la imagen y la pasa a blanco y negro
from PIL import Image
def black_and_white():
   image = Image.open("imagen.png")
   bw = image.convert('L')
   bw.save("imagenbw.png")

#importa la imagen en blanco y negro
black_and_white()
imagen=plt.imread("imagenbw.png") #variable que guardala imagen en blanco y nego


#codigo para la transformada en dos dimesiones.
def transformada(imagen):
	#aplica la transformada
	M=(np.shape(imagen)[0])
	N=(np.shape(imagen)[1])
	n=np.linspace(0.0,N-1,N)
	m=np.linspace(0.0,M-1,M)
	Mat=np.zeros((M,N), dtype= complex)
	for k in range(M):
		for l in range(N):
			suma=0
			e=1j*-2.0*np.pi
			c= e*(n*(float(k)/N))+(m*(float(l)/M))
			suma=np.sum((imagen[k,:]*(np.exp(c))))
			print (suma)
			Mat[k,l]=(suma)
	return (Mat)

#TRANSFORMADA INVERSA
def transformadai(F):
	#aplica la transformada inversa
	M=(np.shape(F)[0])
	N=(np.shape(F)[1])
	n=np.linspace(0.0,N-1,N)
	m=np.linspace(0.0,M-1,M)
	Mat=np.zeros((M,N), dtype= float)
	for k in range(M):
		for l in range(N):
			suma=0
			e=1j*2.0*np.pi
			c= e*(n*(float(k)/N))+(m*(float(l)/M))
			suma=np.sum((F[k,:]*(np.exp(c))))
			Mat[k,l]=(suma)
	return (Mat)

from scipy import fftpack
#a= (transformada(imagen))
fft=fftpack.fft2(imagen,axes=(0,1))
#print (fft)
# (a)
#b= (transformadai(a))
#plt.figure()
#plt.imshow(b, cmap="gray")
#plt.show()

#transformada fft


# TEST
# Recreate input image from 2D DFT results to compare to input image
image = (DFT2D(Image.open("imagenbw.png")))
image.save("output.png", "PNG")




