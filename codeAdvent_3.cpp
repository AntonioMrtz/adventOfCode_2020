#include <iostream>
#include <string>
#include <fstream>
#include <list>

using namespace std;

list<string> lista;

void lectura()
{

    ifstream archivo;
    string texto;

    archivo.open("input2.txt", ios::in);

    while (!archivo.eof())
    {

        getline(archivo, texto);
        lista.push_back(texto);
    }

    archivo.close();
}

string aumentar_tamano(string s, int longitud)
{

    string ret = s;

    while (ret.length() <= longitud)
    {

        ret += s;
    }

    return ret;
}

string *crear_array(string s[], string salida[], int l, int longitud)
{

    for (int i = 0; i < l; i++)
    {

        salida[i] = aumentar_tamano(s[i], longitud);
    }

    return salida;
}

int mainFunction_v1(string s[], int l, int avance)
{

    int total = 0;
    int longitud_sol;

    if (avance == 1) // caso 1,1
        longitud_sol = l;
    else // demas casos x,1
        longitud_sol = ((l - 1) * avance) + 1;

    string aux;
    string salida[l];

    string *def = crear_array(s, salida, l, longitud_sol);

    int i = 1;      // eje x
    int j = avance; // eje y

    for (i; i < l; i++)
    {

        aux = def[i];
        if (aux[j] == '#')
        {

            total += 1;
        }

        j += avance;
    }

    return total;
}

int mainFunction_v2(string s[], int l)
{

    int total = 0;
    int longitud_sol = 1 + ((l - 1) / 2);
    string aux;
    string salida[l];

    string *def = crear_array(s, salida, l, longitud_sol);

    int i = 2; // eje x
    int j = 1; // eje y

    for (i; i < l; i = i + 2)
    {

        aux = def[i];
        if (aux[j] == '#')
        {

            total += 1;
        }

        j += 1;
    }

    return total;
}

int main()
{

    lectura();

    string array[lista.size()];
    std::copy(lista.begin(), lista.end(), array);

    int l = sizeof(array) / sizeof(array[0]);

    cout << "------------" << endl;

    long a = mainFunction_v1(array, l, 1);
    long b = mainFunction_v1(array, l, 3);
    long c = mainFunction_v1(array, l, 5);
    long d = mainFunction_v1(array, l, 7);
    long e = mainFunction_v2(array, l);

    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout << d << endl;
    cout << e << endl;

    cout << endl;

    long long var = a * b; // *? Por alguna razón no se puede hacer la multiplicacion del tiron , no entiendo la razón ya que long en principio es suficiente
    var = var * c;
    var = var * d;
    var = var * e;
    cout << var << endl;

    cout << endl;

    return 0;
}






// *! A partir de aqui son funciones DEPRECATED , mantenidas simplemente como historial de progreso tras unificar las funciones principales de distintos casos

int mainFunction_1_1(string s[], int l)
{

    int total = 0;
    int longitud_sol = l;
    string aux;
    string salida[l];

    string *def = crear_array(s, salida, l, longitud_sol);

    int i = 1; // eje x
    int j = 1; // eje y

    for (i; i < l; i++)
    {

        aux = def[i];
        if (aux[j] == '#')
        {

            total += 1;
        }

        j += 1;
    }

    return total;
}

int mainFunction_3_1(string s[], int l)
{

    int total = 0;
    int longitud_sol = ((l - 1) * 3) + 1;
    string aux;
    string salida[l];

    string *def = crear_array(s, salida, l, longitud_sol);

    int i = 1; // eje x
    int j = 3; // eje y

    for (i; i < l; i++)
    { // empezamos en i=1 y j=3

        aux = def[i];
        if (aux[j] == '#')
        {

            total += 1;
        }

        j += 3;
    }

    return total;
}

int mainFunction_5_1(string s[], int l)
{

    int total = 0;
    int longitud_sol = ((l - 1) * 5) + 1;
    string aux;
    string salida[l];

    string *def = crear_array(s, salida, l, longitud_sol);

    int i = 1; // eje x
    int j = 5; // eje y

    for (i; i < l; i++)
    {

        aux = def[i];
        if (aux[j] == '#')
        {

            total += 1;
        }

        j += 5;
    }

    return total;
}

int mainFunction_7_1(string s[], int l)
{

    int total = 0;
    int longitud_sol = ((l - 1) * 7) + 1;
    string aux;
    string salida[l];

    string *def = crear_array(s, salida, l, longitud_sol);

    int i = 1; // eje x
    int j = 7; // eje y

    for (i; i < l; i++)
    {

        aux = def[i];
        if (aux[j] == '#')
        {

            total += 1;
        }

        j += 7;
    }

    return total;
}