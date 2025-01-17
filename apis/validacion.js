const express = require('express');
const Joi = require('joi');

const app = express();
app.use(express.json());

const esquemaUsuario = Joi.object({
    nombre: Joi.string().min(3).required(),
    edad: Joi.number().integer().min(1).required(),
});

app.post('/usuarios', (req, res) => {
    const { error } = esquemaUsuario.validate(req.body);

    if (error) return res.status(400).send(error.details[0].message);

    res.send('Usuario válido');
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});
