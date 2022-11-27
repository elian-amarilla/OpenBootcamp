public class Main{
    public static void main(String[] args){
        int numeroIf = 0;

        determinarSigno(numeroIf);
        cicloWhile();
        cicloDoWhile();
        cicloFor();
        sentenciaSwitch();
    }
    
    public static void determinarSigno(int numeroIf){
        if(numeroIf > 0){
            System.out.println("Es positivo.");
        }
        else if(numeroIf < 0){
            System.out.println("Es negativo.");
        }
        else{
            System.out.println("Es cero.");
        }
    }
    
    public static void cicloWhile(){
        int numeroWhile = 0;
        System.out.println("\nEjecucion del ciclo While: \n");
        while(numeroWhile < 3){
            System.out.print("Vuelta ");
            System.out.println(numeroWhile);
            numeroWhile++;
        }
    }
    public static void cicloDoWhile(){
        int numeroWhile = 0;
        System.out.println("\nEjecucion del ciclo Do While:");
        do{
            System.out.print("Vuelta ");
            System.out.println(numeroWhile);
            numeroWhile++;
        }while(numeroWhile < 1);
    }
    public static void cicloFor(){
        System.out.println("\nEjecucion del ciclo For:");
        for(int numeroFor = 0; numeroFor<= 3; numeroFor++){
            System.out.print("Vuelta ");
            System.out.println(numeroFor);
        }
    }
    public static void sentenciaSwitch(){
        var estacion = "Verano";
        System.out.println("\nUso de la sentencia switch con las estaciones del anio.");
        switch(estacion.toUpperCase()){
                case "VERANO":
                System.out.println("Estamos en verano");
                break;
            case "INVIERNO":
                System.out.println("Estamos en invierno");
                break;
            case "OTONIO":
                System.out.println("Estamos en otonio");
                break;
            case "PRIMAVERA":
                System.out.println("Estamos en la primavera");
                break;
            default: 
                System.out.println("Ingreso una estacion incorrecta.");
        }
        /* Creo que otra solucion puede ser esta: 
        
        switch(estacion.toUpperCase()){
            case "VERANO":
            case "INVIERNO":
            case "OTONIO":
            case "PRIMAVERA":
                System.out.print("Estamos en ");
                System.out.println(estacion);
                break;
            default: 
                System.out.println("Ingreso una estacion incorrecta.");
        }
        */
    }
}