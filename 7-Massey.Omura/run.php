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

?>
<h2>Immagine iniziale:</h2>
<? printTga("lena.tga"); ?>
<br/><br/>
<? pythonRun("python main.py lena.tga 99999999999 8000 9000"); ?>
<br/><br/>
<h2>Immagine criptata da A:</h2>
<? printTga("lena_eA.tga"); ?>
<br/><br/>
<h2>Immagine criptata da B:</h2>
<? printTga("lena_eB.tga"); ?>
<br/><br/>
<h2>Immagine decriptata da A:</h2>
<? printTga("lena_dA.tga"); ?>
<br/><br/>
<h2>Immagine decodificata: </h2>
<? printTga("lena_dec.tga"); ?>

