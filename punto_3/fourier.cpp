#include <iostream> 
#include <fstream> 
#include <string>
#include <math.h>
#include <stdio.h>
using namespace std;


//saca el numero de filas de los datos

void F(char* txt, int& filas);

void F(char* txt, int& filas)
{
  ifstream dat(txt);
  string n;
  filas = 0;
  while( !dat.eof() )
{
    getline(dat, n);
   filas +=1;
}

}

//obtiene el numero de columnas de los datos 
void C(char* txt, int& columnas);

void C(char* txt, int& columnas)
{

  ifstream dat(txt);
  string linea;
  getline(dat, linea);
  columnas = 0;
  int i;
  int M = linea.size();
    for(i = 0; i<M; i++)
{
     columnas += ( linea[i] != ' ' )? 1 : 0;
}

}

//Funciones para inicializar una matriz y borrarla par aque no ocupe espaco en memoria.   
double** inicializar( int M);

double** inicializar( int M)
{
    double **dat;
    dat = new double*[M];
    for(int i=0; i < M; i++)
        dat[i] = new double[M];
    return dat;
}

void quitar(double** arreglo, int N );

void quitar(double** arreglo, int N )

{
    for(int i = 0; i < N; i++)
        delete[] arreglo[i];
    delete[] arreglo;
}


//carga datos

void load( char* nombre, double **dat, int columnas, int filas);
void load( char* nombre, double **dat, int columnas, int filas )
{
    ifstream txt(nombre);
   
    double x[columnas*filas];

    for( int i = 0; i < filas*columnas; i++)
{
        txt >> x[i];
}
    
    for( int i = 0; i < filas; i++)
{
       for( int j = 0; j < columnas; j++)
{
	 dat[i][j] = x[i*columnas +j];
}
    
}
  
}
// imprime 2 columnas de datos del txt
void llena( char* nombre, double **dat, int columnas, int filas);
void llena( char* nombre, double **dat, int columnas, int filas)
{
  dat = inicializar(filas);
  load(nombre, dat, columnas, filas);
  for(int i = 0; i<filas-1; i++)
{
    for(int j =0; j<columnas; j++)
{
     cout<<dat[i][j]<< " " ;
}
    cout<<endl;
}
  quitar(dat, filas);
  
}


double* linspace(double*line, int a, int b, int N)
{
    double dt =(b-a)/(N-1.0);
    for (int i=0; i<N; i++)
{
    line[i] = (i*dt);
}

    return line;

}

//hace la interpolacion de lagragne

double* Plagrange( double*col1, double* col2, double *x_mod, double* y_mod, int filas ){
  for (int k =0; k<filas; k++)
{
      double n= 1.0;
      for (int i= 0; i<filas; i++)
{
	  double v = col2[i];
	  for (int j=0; j<filas; j++)
{
	    if (i != j)
{
		  v = v*(x_mod[k] - col1[j])/(col1[i] - col1[j]);
		  n += v;
}
}
}
      y_mod[k] = n-1.0;
}
  return y_mod;
}
		  
		 
// Funcion para la transformada de Fourier separando real de iamginario 

double * fourier(double* Preal, double* Pimaginaria, double* x_nuevo, double*y_nuevo, int filas)
{
  for (int i = 0; i<filas;i++)
{
    double P_real = 0.0;
    double P_imaginario = 0.0;
    for (int j =0; j< filas;j++)
{
      P_real += y_nuevo[j] * cos((-2*3.1415*i*j)/filas);
      P_imaginario += y_nuevo[j] * sin((-2*3.1415*i*j)/filas);
      Preal[j]= P_real;
      Pimaginaria[j]= P_imaginario;
      cout<<Preal[j]<<"  " << " " << Pimaginaria[j] <<endl;
}
    
}
  return Preal, Pimaginaria;
}

// metodo para conseguir las frecuencias		  
double* frecuencias_f(double*frec, double*Preal, double*Pimaginaria, int F)
{
  for(int i=0; i<F;i++)
{
      double raiz  = (Preal[i] * Preal[i]) + ( Pimaginaria[i] *  Pimaginaria[i]);
      double norma = pow(raiz,0.5);
      frec[i] = norma;
      cout<<Pimaginaria[i]<<" "<<endl;
}
  return frec;
}
// main, corre todo el programa en orden					  
int main(int argc, char * argv[] ){
    int m=0, n=0;
    F(argv[1],n);
    C(argv[1],m);
    double **dat;
    dat = inicializar(n);
    load(argv[1],dat,m,n);
   

    double x[n];
    double y[n];
    for (int i = 0; i<n-1; i++)
{
      x[i] = dat[i][0];
      y[i] = dat[i][1];
}
    int filas = n-1;
    double a = x[0];
    double b = x[filas-1];
    double x_mod[n];
    linspace(x_mod, a, b, filas);
    double y_mod[n];
    Plagrange( x, y, x_mod, y_mod, filas );
    double Preal[filas];
    double Pimaginaria[filas];
    double frecuencias[filas];
    cout<< "parte real" << "  " << "parte imaginaria"<<endl; 
    fourier(Preal,Pimaginaria, x_mod, y_mod, filas);
    cout<< "Frecuencias"<<endl;
    frecuencias_f(frecuencias, Preal, Pimaginaria, filas);

}
