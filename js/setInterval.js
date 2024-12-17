let contador = 0;
let temporizador = setInterval(function() {
    contador++;
    console.log(contador);
    if (contador === 5) {
        clearInterval(temporizador);
    }
}, 1000);
