using System;

// Laboratorio 01 - Fundamentos de Programación (C#)
// Programa de saludo simple implementado en la rama de funcionalidad.
class Programa
{
    static void Main()
    {
        Console.Write("Ingresa tu nombre: ");
        string? nombre = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(nombre))
        {
            nombre = "estudiante";
        }

        Console.WriteLine($"¡Hola, {nombre.Trim()}! Bienvenido al curso de Fundamentos de Programación.");
        Console.WriteLine($"Fecha de ejecución: {DateTime.Now:dd/MM/yyyy HH:mm}");
    }
}
