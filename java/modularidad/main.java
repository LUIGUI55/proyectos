public class main{
    public static void main(String[]args){
        calculadora calc = new calculadora();

        int resultadoSuma = calc.sumar(5,3);
        int resultadoResta = calc.restar(10,4);
        int resultadoMultiplicacion = calc.multiplicar (2, 6);
        double resultadoDivicion = calc.dividir(8,2);

        System.out.println("SUMA" + resultadoSuma);
        System.out.println("RESTA" + resultadoResta);
        System.out.println("MULTIPLICACION" + resultadoMultiplicacion);
        System.out.println("DIVICION" + resultadoDivicion);

    }
}

