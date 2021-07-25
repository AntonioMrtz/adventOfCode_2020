#include <iostream>
#include <string>
#include <fstream>
#include <list>

using namespace std;

list<string> lista;

int globalCounter = 0;
int globalCounter_v2 = 0;

struct Casos
{

    int num1;
    int num2;
    char letra;
    string cadena;
};

void lectura()
{

    ifstream archivo;
    string texto;

    archivo.open("input.txt", ios::in);

    while (!archivo.eof())
    {

        getline(archivo, texto);
        lista.push_back(texto);
    }

    archivo.close();
}

Casos tratarCadena(string s)
{ // 11-14 b: bbbbbbbbbbbbbbb // 5-6 w: wwwwnm

    int i = 0;
    string aux = "";
    Casos caso;

    while (s[i] != '-')
    {

        aux += s[i];
        i++;
    }

    i += 1;

    caso.num1 = stoi(aux);

    aux = "";

    while (s[i] != ' ')
    {

        aux += s[i];
        i++;
    }

    caso.num2 = stoi(aux);

    i += 1;

    caso.letra = s[i];

    i += 3;

    aux = "";

    for (int j = i; j < s.length(); j++)
    {

        aux += s[j];
    }

    caso.cadena = aux;

    return caso;
}

bool isValid(Casos c)
{

    int contador = 0;

    for (int i = 0; i < c.cadena.length(); i++)
    {

        if (c.cadena[i] == c.letra)
        {

            contador++;
        }
    }

    return contador >= c.num1 && contador <= c.num2;
}

bool isValid_v2(Casos c)
{

    return (c.cadena[c.num1 - 1] == c.letra && c.cadena[c.num2 - 1] != c.letra) || (c.cadena[c.num1 - 1] != c.letra && c.cadena[c.num2 - 1] == c.letra);
}

int mainFunction(string array[], int l)
{

    for (int i = 0; i < l; i++)
    {

        Casos caso = tratarCadena(array[i]);

        if (isValid(caso))
        {

            globalCounter += 1;
        }
    }

    return globalCounter;
}

int mainFunction_v2(string array[], int l)
{

    for (int i = 0; i < l; i++)
    {

        Casos caso = tratarCadena(array[i]);

        if (isValid_v2(caso))
        {

            globalCounter_v2 += 1;
        }
    }

    return globalCounter_v2;
}

int main()
{

    lectura();

    string array[lista.size()];
    std::copy(lista.begin(), lista.end(), array);

    int longitud = sizeof(array) / sizeof(array[0]);

    cout << mainFunction(array, longitud) << endl; // ** APARTADO 1
    cout << "" << endl;
    cout << mainFunction_v2(array, longitud) << endl; // ** APARTADO 2

    return 0;
}