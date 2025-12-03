<?php
// 1. Receber dados da requisição (metodo GET)
$cidade = $_GET['cidade'] ?? '';

// 2. Montar URL para fazer nova requisição HTTP para a intenet
$url = "https://wttr.in/" . urlencode($cidade) . "?format=3";

// 3. Fazer requisição HTTP externa (GET) ao servidor wttr.in
$reponsta = file_get_contents($url);

// 4. Exibir no navegador o que veio do servidor
echo "<h2>Resultado da requisição</h2>";
echo "<p><strong>Cidade consultada:</strong> $cidade</p>";
echo "<p><strong>Clima:</strong> $reponsta</p>";

?>