#!/bin/sh

echo "Richiede imagemagick: "
echo "$ sudo apt-get install imagemagick"


php run.php | tee out.html

## per MAC
if [ "$(uname)" = "Darwin" ]
then
	open -a "Google Chrome" out.html
else
	google-chrome out.html
fi
