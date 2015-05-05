#!/bin/sh

php run.php > out.html

## per MAC
if [ "$(uname)" = "Darwin" ]
then
	open -a "Google Chrome" out.html
else
	google-chrome out.html
fi
