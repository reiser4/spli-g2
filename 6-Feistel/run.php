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

$key = mt_rand(0,1023);
$bdec = decbin($key);
$pad = str_pad($bdec,16,"0",STR_PAD_RIGHT);
$binkey = substr($pad,0,4);

?>
<h2>Immagine iniziale:</h2>
<? printTga("lena.tga"); ?>
<br/><br/>
<h2>Eseguo crittografia con chiave <?=$binkey ?><h2>
<br/>
<? pythonRun("python marco.py encrypt $binkey lena.tga"); ?>
<h2>Immagine paddata:</h2>
<? printTga("file-padded.tga"); ?>
<h2>Immagine crittografata:</h2>
<? printTga("file-crypted.tga"); ?>
<h2>Ricerca della chiave: </h2>
<? pythonRun("python bruteforce.py 4 file-padded.tga file-crypted.tga"); ?>
<h2>Decodifica dell'immagine: </h2>
<? pythonRun("python marco.py decrypt $binkey file-crypted.tga"); ?>
<br/>
<? printTga("file-decrypted.tga"); ?>

