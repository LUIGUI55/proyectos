let email = "ejemplo@dominio.com";
let patron = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

if (patron.test(email)) {
    console.log("Correo electrónico válido");
} else {
    console.log("Correo electrónico no válido");
}
