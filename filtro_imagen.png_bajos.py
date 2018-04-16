import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cmath
pi = np.pi * 2.0

from PIL import Image
def black_and_white():
	image = Image.open("imagen.png")
	bw = image.convert('L')
	bw.save("imagenbw.png")
#comvierte la imagen en blanco y negro
black_and_white()
image=plt.imread("imagenbw.png")
M=(np.shape(image)[0])
N=(np.shape(image)[1])

#codigo para la transformada, retorna la transformada en formato matricial 
def FT(image):
	global M, N
	M=(np.shape(image)[0])
	N=(np.shape(image)[1])
	dft2d_b = Mat=np.zeros((M,N), dtype= complex)
	pixels = image
	for k in range(M):
		for l in range(N):
			suma = 0.0
			for m in range(M):
				for n in range(N):
					e = cmath.exp(-1j*pi*(float(k*m)/M + float(l*n)/N))
					suma = suma + pixels[m, n]* e
			dft2d_b[l][k] = suma / M /N 
	return (dft2d_b)

#codigo para la transformada inversa, retorna la imagen en formato matricial
def IFT(dft2d_b):
	global M, N 
	pixels = Mat=np.zeros((M,N), dtype= float)
	for m in range(M):
		for n in range(N):
			suma = 0.0
			for k in range(M):
				for l in range(N):
					e = cmath.exp(1j*pi*(float(k*m)/M + float(l*n)/N))
					suma = suma + dft2d_b[l][k] * e
			black= (suma.real)
			pixels[m,n]=black
	return (pixels)


#codigo para pelar frecuencias
def pasa_bajos(transformada):
	global M, N
	for m in range(M):
		for n in range(N):
			if (abs(transformada[m,n])>0.02):
				transformada[m,n]=0
	return (transformada)

#cogifo de gaussiana
def gauss():
	global M, N
	x, y = np.meshgrid(np.linspace(0.0,N-1,N), np.linspace(0.0,M-1,M))
	d = np.sqrt(x*x+y*y)
	sigma, mu = 1.0, 0.0
	g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )	
	return (g)


imagen = pasa_bajos(FT(image))
kernel= FT(gauss())

transform=IFT(imagen*kernel)
plt.figure()
plt.imshow(transform, cmap="gray")
plt.show()
plt.imsave("pasa_bajos.png",transform[:,:], cmap= plt.cm.gray)

