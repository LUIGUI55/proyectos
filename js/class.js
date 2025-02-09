class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar() {
        console.log("Hola, mi nombre es " + this.nombre);
    }
}

let persona1 = new Persona("Carlos", 28);
persona1.saludar();  // "Hola, mi nombre es Carlos"


