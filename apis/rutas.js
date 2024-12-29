const express = require('express');
const app = express();

app.get('/usuarios', (req, res) => {
    res.json([{ id: 1, nombre: 'Juan' }, { id: 2, nombre: 'Ana' }]);
});

app.post('/usuarios', (req, res) => {
    res.send('Usuario creado');
});

app.put('/usuarios/:id', (req, res) => {
    res.send(`Usuario con ID ${req.params.id} actualizado`);
});

app.delete('/usuarios/:id', (req, res) => {
    res.send(`Usuario con ID ${req.params.id} eliminado`);
});

app.listen(3000, () => {
    console.log('API REST en http://localhost:3000');
});
