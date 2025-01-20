class calculadora{
    public int sumar( int a, int b){
        return a + b;
    }
    public int restar( int a, int b){
        return a - b;
    }
    public int multilplicacion(int a, int b){
    return a*b;
    }
    public int divicion(double a, double b,){
        if (b==0){
            System.out.println("Error divicion por cero");

            return Double.NaN;
        }
        return a/b;
    }

}