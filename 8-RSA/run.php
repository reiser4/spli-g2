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
<? pythonRun("python main.py lena.tga 998999999 9999999999 1000000"); ?>
<br/><br/>
<h2>Immagine criptata:</h2>
<? printTga("lena_encrypted.tga"); ?>
<br/><br/>
<h2>Immagine decriptata:</h2>
<? printTga("lena_decrypted.tga"); ?>
<br/><br/>
<h2>Immagine bruteforce:</h2>
<? printTga("lena_bruteforce.tga"); ?>
