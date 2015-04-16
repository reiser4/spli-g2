<?php




if (count($argv) != 4) {
	echo "Uso: " . $argv[0] . " <server> <file> <key>\n";
	echo "Esempio: " . $argv[0] . " 127.0.0.1 pg100.txt 8\n";
	die();
}

function pulito($infile) {
	$out = "";
	$infile = strtolower($infile);
	for ($i = 0; $i < strlen($infile); $i++) {
		if ($infile[$i] == " " || $infile[$i] == "\n") {
			$out .= $infile[$i];
		} else {
			if (ord($infile[$i]) >= ord("a") && ord($infile[$i]) <= ord("z")) {
				$out .= $infile[$i];
			}
		}
	}
	return $out;
}

function cifrato($infile, $key) {
        $out = "";
        for ($i = 0; $i < strlen($infile); $i++) {
                if ($infile[$i] == " " || $infile[$i] == "\n") {
                        $out .= $infile[$i];
                } else {
                        $outchar = ord($infile[$i]) + $key;
			if ($outchar > ord("z")) {
				$outchar -= (ord("z") - ord("a") + 1);
			}
                        $out .= chr($outchar);
                }
        }
        return $out;
}



$address = $argv[1];
$service_port = 9999;

$file = $argv[2];
$key = $argv[3];

$infile = file_get_contents($file);
echo "Md5 file ingresso: " . md5($infile) . "\n";

$pulito = pulito($infile);
file_put_contents($file . "-pulito", $pulito);
echo "Md5 file pulito: " . md5($pulito) . "\n";

$cifrato = cifrato($pulito, $key);
file_put_contents($file . "-cifrato", $cifrato);
echo "Md5 file cifrato: " . md5($cifrato) . "\n";




/* Create a TCP/IP socket. */
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
} else {
    echo "OK.\n";
}

echo "Attempting to connect to '$address' on port '$service_port'...";
$result = socket_connect($socket, $address, $service_port);
if ($result === false) {
    echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
} else {
    echo "OK.\n";
}

echo "Sending text...\n";
socket_write($socket, $cifrato, strlen($cifrato));
echo "OK\n";

echo "Closing socket...\n";
socket_close($socket);
echo "OK.\n\n";
