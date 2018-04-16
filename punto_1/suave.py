import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cmath
import sys

sigma=sys.argv[2]
nombre_imagen=sys.argv[1]

pi = np.pi * 2.0


from PIL import Image
def black_and_white():
	global nombre_imagen
	image = Image.open(nombre_imagen)
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

#codigo para una gaussiana en dos dimensiones
def gauss():
	global sigma
	global M, N
	x, y = np.meshgrid(np.linspace(0.0,N-1,N), np.linspace(0.0,M-1,M))
	d = np.sqrt(x*x+y*y)
	mu = 0.0
	g = np.exp(-( (d-mu)**2 / ( 2.0 * float(sigma)**2.0 ) ) )
	return (g)

imagen = FT(image)
kernel= FT(gauss())

transform=IFT(imagen*kernel)
plt.figure()
plt.imshow(transform, cmap="gray")
plt.imsave("suave.png",transform[:,:], cmap= plt.cm.gray)
