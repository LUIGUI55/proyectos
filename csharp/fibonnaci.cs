// crearemos la clase Fibonacci
// que tendrá un método llamado Calcular
// que recibirá un número entero n

using System;
class Fibonacci
{
    public int Calcular(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        else if (n == 1)
        {
            return 1;
        }
        else
        {
            return Calcular(n - 1) + Calcular(n - 2);
        }
    }
}