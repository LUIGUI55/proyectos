const express = require('express');
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/miapp', { useNewUrlParser: true, useUnifiedTopology: true });

const Usuario = mongoose.model('Usuario', { nombre: String, edad: Number });

const app = express();
app.use(express.json());

// Crear usuario
app.post('/usuarios', async (req, res) => {
    const usuario = new Usuario(req.body);
    await usuario.save();
    res.status(201).json(usuario);
});

// Leer usuarios
app.get('/usuarios', async (req, res) => {
    const usuarios = await Usuario.find();
    res.json(usuarios);
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});
