const express = require('express');
const app = express();

app.use(express.json());

let usuarios = [];

// Crear usuario
app.post('/usuarios', (req, res) => {
    const usuario = { id: usuarios.length + 1, ...req.body };
    usuarios.push(usuario);
    res.status(201).json(usuario);
});

// Leer todos los usuarios
app.get('/usuarios', (req, res) => {
    res.json(usuarios);
});

// Leer un usuario por ID
app.get('/usuarios/:id', (req, res) => {
    const usuario = usuarios.find(u => u.id === parseInt(req.params.id));
    if (!usuario) return res.status(404).send('Usuario no encontrado');
    res.json(usuario);
});

// Actualizar un usuario
app.put('/usuarios/:id', (req, res) => {
    const usuario = usuarios.find(u => u.id === parseInt(req.params.id));
    if (!usuario) return res.status(404).send('Usuario no encontrado');

    usuario.nombre = req.body.nombre;
    res.json(usuario);
});

// Eliminar un usuario
app.delete('/usuarios/:id', (req, res) => {
    usuarios = usuarios.filter(u => u.id !== parseInt(req.params.id));
    res.send('Usuario eliminado');
});

app.listen(3000, () => {
    console.log('CRUD en http://localhost:3000');
});
