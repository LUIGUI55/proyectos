const express = require('express');
const usuariosRouter = require('./rutas/usuarios');

const app = express();
app.use(express.json());
app.use('/usuarios', usuariosRouter);

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});
