// crearemos una clase llamada Carrera
// que tendrá un método llamado CalcularTiempo
// que recibirá la distancia de la carrera en metros
// y la velocidad en metros por segundo
// y devolverá el tiempo que tardará en segundos

using System;
class Carrera
{
    public int CalcularTiempo(int distancia, int velocidad)
    {
        return distancia / velocidad;
    }
}