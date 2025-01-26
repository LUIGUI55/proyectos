<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Ejemplo</title>
</head>
<body>
    <h1>Formulario de Ejemplo</h1>
    <form action="paf2.php" method="post">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <input type="submit" value="Enviar">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Recibir los datos del formulario
        $nombre = htmlspecialchars($_POST['nombre']);
        $email = htmlspecialchars($_POST['email']);
        
        // Mostrar los datos recibidos
        echo "<h2>Datos recibidos:</h2>";
        echo "Nombre: " . $nombre . "<br>";
        echo "Email: " . $email . "<br>";
    }
    ?>
</body>
</html>

