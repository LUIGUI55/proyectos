let promesa = new Promise(function(resolve, reject) {
    let exito = true;
    if (exito) {
        resolve("Operación exitosa");
    } else {
        reject("Ocurrió un error");
    }
});

promesa.then(function(resultado) {
    console.log(resultado);
}).catch(function(error) {
    console.log(error);
});