<html>
<head>
    <title>Weather</title>
</head>
<body>
<table align="center" border="1">
<?php
    $cnx = new mysqli('localhost', 'root', 'password', 'weather');

    if ($cnx->connect_error)
        die('Connection failed: ' . $cnx->connect_error);

    $query = 'SELECT * FROM weather';
    $cursor = $cnx->query($query);
    while ($row = $cursor->fetch_assoc()) {
        echo '<tr>';
        echo '<td>' . $row['state'] . '</td><td>' . $row['city'] . '</td><td align="right">' . $row['weather'] . '</td><td>' . $row['temp'] . '</td><td>' . $row['humidity'] . '</td><td>' . $row['pres'] . '</td>';
        echo '</tr>';
    }

    $cnx->close();
?>
</table>
</body>
</html>
