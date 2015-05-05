<?
error_reporting(E_ALL);

function printTga($filename) {
	system("convert $filename $filename.jpg");
	?><img src="<?=$filename?>.jpg"><?
}

function pythonRun($cmdline) {
	?>$ <?=$cmdline ?><?
	$out = array();
	$run = exec("$cmdline 2>&1",$out);
	foreach ($out as $l) {
	?><br/>&gt;&gt;&gt; <?=$l ?><?
	}
}

$immage = "lena.tga";
$immagedec = "lena_dec.tga";

?>
<h2>Immagine iniziale:</h2>
<? printTga("lena.tga"); ?>
<br/><br/>
<? pythonRun("python main.py $immage 100000000 1000 1200"); ?>
<h2>Immagine decodificata: </h2>
<? printTga($immagedec); ?>

