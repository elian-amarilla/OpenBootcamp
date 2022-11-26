public class Main{
    public static void main(String[] args){
        System.out.println("Primer Parte - Funcion que sume tres argumentos:");
        suma(10, 20, 30);
        
        System.out.println("\nSegunda Parte - Cantidad de puertas:");
        Coche miCoche = new Coche();
        miCoche.agregarPuerta();
        System.out.println(miCoche.puertas);
    }

    public static void suma(int a, int b, int c){
        System.out.println(a+b+c);
    }
}

class Coche{
    public int puertas = 0;
    public void agregarPuerta(){
        this.puertas++;
    }
}