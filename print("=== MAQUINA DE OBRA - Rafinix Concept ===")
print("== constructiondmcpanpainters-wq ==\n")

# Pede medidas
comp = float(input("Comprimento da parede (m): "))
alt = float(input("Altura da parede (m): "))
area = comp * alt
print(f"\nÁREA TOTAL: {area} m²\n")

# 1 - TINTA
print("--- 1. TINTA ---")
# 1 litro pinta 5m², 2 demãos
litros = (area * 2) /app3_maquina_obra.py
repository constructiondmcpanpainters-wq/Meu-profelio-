<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maquina de Obra - Rafinix</title>
<style>
body{font-family:Arial;background:#111;color:#fff;padding:20px}
.card{background:#222;padding:20px;border-radius:15px}
input{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:none}
button{width:100%;padding:15px;background:#00ff88;color:#000;font-weight:bold;border:none;border-radius:10px;font-size:18px}
.result{background:#333;padding:15px;border-radius:10px;margin-top:15px}
</style>
</head>
<body>
<h2>🏗️ MAQUINA DE OBRA<br><small>@Rafinix_Concept01</small></h2>
<div class="card">
Comprimento (m):<input id="c" type="number" value="4">
Altura (m):<input id="a" type="number" value="3">
Preço por m² (MT):<input id="p" type="number" value="250">
<button onclick="calc()">CALCULAR TUDO</button>
<div id="res" class="result"></div>
</div>
<script>
function calc(){
let comp=parseFloat(document.getElementById('c').value)
let alt=parseFloat(document.getElementById('a').value)
let preco=parseFloat(document.getElementById('p').value)
let area=comp*alt
let litros=(area*2)/5
let tijolos=area*27
let cimento=area*5
let total=area*preco
document.getElementById('res').innerHTML=`
ÁREA: ${area} m²<br><br>
🎨 TINTA: ${litros.toFixed(1)} litros (${(litros/18).toFixed(1)} latas 18L)<br>
🧱 TIJOLOS: ${tijolos.toFixed(0)} unid.<br>
💰 CIMENTO: ${cimento.toFixed(0)}kg (${(cimento/50).toFixed(1)} sacos)<br><br>
<b>💵 TOTAL: ${total.toFixed(2)} MT</b>`
}
</script>
</body>
</html>