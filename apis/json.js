const express = require('express');
const app = express();

app.use(express.json());

app.post('/datos', (req, res) => {
    const { nombre, edad } = req.body;
    res.send(`Nombre: ${nombre}, Edad: ${edad}`);
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});
