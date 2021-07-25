#include <iostream>
#include <string>
#include <fstream>
#include <list>

using namespace std;

list<string> lista;

struct Pasaporte
{

    string ecl, hcl, hgt, pid, eyr, byr, iyr, cid;
};

void lectura()
{

    ifstream archivo;
    string texto;

    archivo.open("input3.txt", ios::in);

    while (!archivo.eof())
    {

        getline(archivo, texto);
        lista.push_back(texto);
    }

    archivo.close();
}

bool check_byr(string s)
{ // * four digits; at least 1920 and at most 2002.

    return s.length() == 4 && stoi(s) >= 1920 && stoi(s) <= 2002;
}

bool check_iyr(string s)
{ // * four digits; at least 2010 and at most 2020.

    return s.length() == 4 && stoi(s) >= 2010 && stoi(s) <= 2020;
}

bool check_eyr(string s)
{ // * four digits; at least 2020 and at most 2030.

    return s.length() == 4 && stoi(s) >= 2020 && stoi(s) <= 2030;
}

bool check_hgt(string s)
{ // * acabado en cm entre 150 y 193 o acabado en in entre 59 y 76 o solo

    if (s[s.length() - 2] == 'c' && s[s.length() - 1] == 'm' && s >= "150cm" && s <= "193cm")
    {

        return true;
    }

    else if (s[s.length() - 2] == 'i' && s[s.length() - 1] == 'n' && s >= "59in" && s <= "76in")
    {

        return true;
    }

    return false;
}

bool check_ecl(string s)
{ // * ser una de esas cadenas

    return s == "amb" || s == "blu" || s == "brn" || s == "gry" || s == "grn" || s == "hzl" || s == "oth";
}

bool check_pid(string s)
{ // * numeros de 9 cifras

    return s.length() == 9 && s >= "000000000" && s <= "999999999";
}

bool check_hcl(string s)
{ // * # + cadenas de numeros o letras

    return s[0] = '#' && s >= "#000000" && s <= "#ffffff" && s.length() == 7;
}

bool acceptPassport(Pasaporte p)
{

    // PROBLEMA 1

    if (p.ecl.empty() || p.hcl.empty() || p.hgt.empty() || p.pid.empty() || p.eyr.empty() || p.byr.empty() || p.iyr.empty())
    {

        return false;
    }

    // PROBLEMA 2

    if (check_byr(p.byr) && check_iyr(p.iyr) && check_eyr(p.eyr) && check_hgt(p.hgt) && check_ecl(p.ecl) && check_pid(p.pid) && check_hcl(p.hcl))
    {

        return true;
    }

    return false;
}

int mainFunction()
{

    int total = 0;

    list<string>::iterator it = lista.begin();

    Pasaporte pas;

    while (it != lista.end())
    {

        string aux = *it;

        if (*it == "" || it == lista.end())
        { // si cadena vacia o final lista -> creamos nuevo pasaporte y comprobamos el actual

            if (acceptPassport(pas))
                total += 1;

            pas.byr = "";
            pas.cid = "";
            pas.ecl = "";
            pas.eyr = "";
            pas.hcl = "";
            pas.hgt = "";
            pas.iyr = "";
            pas.pid = "";
        }

        else
        { // si no es cadena vacia -> tratamos los campos de la linea y los añadimos al pasaporte actual

            int i = 0;
            string actual = "";
            string actual_val = "";

            while (i + 1 < aux.length())
            {

                while (aux[i] != ':')
                {

                    actual += aux[i];
                    i++;
                }

                i++;

                while (aux[i] != ' ' && i < aux.length())
                {

                    actual_val += aux[i];
                    i++;
                }

                if (i + 1 < aux.length())
                    i++;

                if (actual == "ecl")
                    pas.ecl = actual_val;
                else if (actual == "pid")
                    pas.pid = actual_val;
                else if (actual == "eyr")
                    pas.eyr = actual_val;
                else if (actual == "hcl")
                    pas.hcl = actual_val;
                else if (actual == "byr")
                    pas.byr = actual_val;
                else if (actual == "iyr")
                    pas.iyr = actual_val;
                else if (actual == "cid")
                    pas.cid = actual_val;
                else if (actual == "hgt")
                    pas.hgt = actual_val;

                actual = "";
                actual_val = "";
            }
        }

        *it++;
    }

    return total;
}

int main()
{

    lectura();
    cout << mainFunction() << endl;
    return 0;
}