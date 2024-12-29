const express = require('express');
const router = express.Router();

let usuarios = [];

router.get('/', (req, res) => {
    res.json(usuarios);
});

router.post('/', (req, res) => {
    const usuario = { id: usuarios.length + 1, ...req.body };
    usuarios.push(usuario);
    res.status(201).json(usuario);
});

module.exports = router;
