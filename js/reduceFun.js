let numeros = [1, 2, 3, 4, 5];
let suma = numeros.reduce(function(total, num) {
    return total + num;
}, 0);
console.log(suma);  // 15