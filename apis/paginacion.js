const express = require('express');
const app = express();

const usuarios = Array.from({ length: 50 }, (_, i) => ({ id: i + 1, nombre: `Usuario ${i + 1}` }));

app.get('/usuarios', (req, res) => {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 10;
    const startIndex = (page - 1) * limit;
    const endIndex = page * limit;

    res.json({
        total: usuarios.length,
        page,
        usuarios: usuarios.slice(startIndex, endIndex),
    });
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});
