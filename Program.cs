using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Ingresa la cantidad en metros:");
        
        string textoIngresado = Console.ReadLine();
        double metros = Convert.ToDouble(textoIngresado);

        double centimetros = metros * 100;

        Console.WriteLine("La cantidad en centímetros es: " + centimetros);
    }
}