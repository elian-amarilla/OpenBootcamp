public class Main{
    public static void main(String[] args){
        Persona persona = new Persona();
        String salida;
        
        persona.setEdad(21);
        persona.setNombre("Elian");
        persona.setTelefono("1133644825");
        
        salida = "La persona se llama " + persona.getNombre() + " y tiene " + persona.getEdad() + " y su telefono es " + persona.getTelefono();
        System.out.print(salida);
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
