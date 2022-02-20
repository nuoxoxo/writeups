## Vous n'avez pas les bases
- method 1 
  - use [gchq](http://gchq.github.io/CyberChef)
- method 2
```scala
$ brew install coreutils  # in order to use base32

$ cat message_9XpaGRS.txt | base64 -d | base32 -d | xxd -r -p
```
