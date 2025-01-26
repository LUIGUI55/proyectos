const express = require('express');
const app = express();

// Middleware para log de solicitudes
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

app.get('/', (req, res) => {
    res.send('Middleware funcionando');
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});