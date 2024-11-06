const cintaElement = document.querySelector('.cinta');
const entradaInput = document.getElementById('entrada');
const salidaElement = document.getElementById('salida');

// ... (resto de la implementación de la máquina de Turing)

function actualizarCinta() {
  cintaElement.innerHTML = '';
  for (let i = 0; i < maquina_turing.cinta.length; i++) {
    const celda = document.createElement('div');
    celda.classList.add('celda');
    if (i === maquina_turing.cabeza) {
      celda.classList.add('cabeza');
    }
    celda.textContent = maquina_turing.cinta[i];
    cintaElement.appendChild(celda);
  }
}

function ejecutar() {
  const cintaEntrada = entradaInput.value;
  maquina_turing.ejecutar(cintaEntrada);
  actualizarCinta();
  salidaElement.textContent = 'Resultado: ' + maquina_turing.cinta.join('');
}

function paso() {
  maquina_turing.paso();
  actualizarCinta();
}