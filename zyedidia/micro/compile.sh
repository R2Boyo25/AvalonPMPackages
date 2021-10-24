pwd
if make build
then
    :
else
    cp .avalon/Makefile Makefile
    make build
fi