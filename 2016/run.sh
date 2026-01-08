gcc "day$1/part$2.c" -o "run.c"
if [[ "$3" = "test" ]]; then file="day$1/test.txt"; else file="day$1/source.txt"; fi
echo "$3"
echo "$file"
./run.c "$file"
