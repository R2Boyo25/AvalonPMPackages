if go
then
    :
else
    echo "Go is not installed!"
    echo "please follow the guide at https://golang.org/doc/install"
    echo "I attempted to get avalon to compile and install go but it just segfaults, sorry"
    exit
fi

if make build
then
    :
else
    cp .avalon/Makefile Makefile
    make build
fi