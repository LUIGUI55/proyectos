const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

const SECRET_KEY = 'mi_clave_secreta';

app.post('/login', (req, res) => {
    const { usuario, contraseña } = req.body;

    if (usuario === 'admin' && contraseña === '1234') {
        const token = jwt.sign({ usuario }, SECRET_KEY, { expiresIn: '1h' });
        return res.json({ token });
    }

    res.status(401).send('Credenciales inválidas');
});

app.get('/perfil', (req, res) => {
    const token = req.headers['authorization'];

    if (!token) return res.status(401).send('Token requerido');

    try {
        const datos = jwt.verify(token, SECRET_KEY);
        res.json({ mensaje: `Hola ${datos.usuario}` });
    } catch {
        res.status(401).send('Token inválido');
    }
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});



