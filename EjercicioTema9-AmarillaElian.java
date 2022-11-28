/*
   ***************************************************
            Solución sin encapsulamiento
   ***************************************************
 */
public class Main{
    public static void main(String[] args){
        Cliente cliente = new Cliente("Elian", 21, "1133644825", 100);
        Trabajador empleado = new Trabajador("Elian", 21, "1133644825", (float)500.5);
        
        System.out.println("Cliente: ");
        System.out.println("Nombre: " + cliente.nombre + " tiene " + cliente.edad + " anios");
        System.out.println("Su numero de telefono es " + cliente.telefono + " y el credito es de $" + cliente.credito);
        
        System.out.println("\n\nTrabajador: ");
        System.out.println("Nombre: " + empleado.nombre + " tiene " + empleado.edad + " anios");
        System.out.println("Su numero de telefono es " + empleado.telefono + " y el salario es de $" + empleado.salario);
    }
}

class Persona{
    int edad;
    String nombre;
    String telefono;
}

class Cliente extends Persona{
    float credito;
    
    public Cliente(String nombre, int edad, String telefono, float credito){
        this.nombre = nombre;
        this.edad = edad;
        this.telefono = telefono;
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    float salario;
    
    public Trabajador(String nombre, int edad, String telefono, float salario){
        this.nombre = nombre;
        this.edad = edad;
        this.telefono = telefono;
        this.salario = salario;
    }
}

/* 
   ***************************************************
            Solución con encapsulamiento
   ***************************************************
*/

public class Main{
    public static void main(String[] args){
        Cliente cliente = new Cliente();
        Trabajador empleado = new Trabajador();
        
        cliente.setEdad(21);
        cliente.setNombre("Elian");
        cliente.setTelefono("1133644825");
        cliente.setCredito((float)100.0);
        
        empleado.setEdad(22);
        empleado.setNombre("Jorge");
        empleado.setTelefono("1134435512");
        empleado.setSalario((float)500.5);
     
        System.out.println("Cliente: ");
        System.out.println(cliente.getNombre() + " tiene " + cliente.getEdad() + " anios y su telefono es " + cliente.getTelefono() + " y posee un credito de $" + cliente.getCredito());
        
        System.out.print("\n\n");
        System.out.println("Empleado: ");
        System.out.println(empleado.getNombre() + " tiene " + empleado.getEdad() + " anios y su telefono es " + empleado.getTelefono() + " y posee un salario de $" + empleado.getSalario());
     
        
    }
}

class Persona{
    private int edad;
    private String nombre;
    private String telefono;
    
    public int getEdad(){
        return this.edad;
    }
    public void setEdad(int edad){
        this.edad = edad;
    }
    public String getNombre(){
        return this.nombre;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getTelefono(){
        return this.telefono;
    }
    public void setTelefono(String telefono){
        this.telefono = telefono;
    }
    
}

class Cliente extends Persona{
    private float credito;
    public float getCredito(){
        return this.credito;
    }
    public void setCredito(float credito){
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    private float salario;
    
    public float getSalario(){
        return this.salario;
    }
    
    public void setSalario(float salario){
        this.salario = salario;
    }
}
