## Vous n'avez pas les bases
- method 1 
  - use [gchq](http://gchq.github.io/CyberChef)
- method 2
```scala
$ brew install coreutils  # in order to use base32

$ cat message_9XpaGRS.txt | base64 -d | base32 -d | xxd -r -p
```
## We need a pattern
letter frequency in english
```erlang
╝±╩ ¥║£║ ╗═ ┴±╔£ ¤╬╣╦:
now here is your flag
42┼¿¤{®±_╝±¿_╔═║_©±╝±╣╬Ø¥╣█║¿╗┼_═╔█═¿╗¿╔¿╗±╝}
42ctf{do_not_use_monoalphabetic_substitution}
. . .
# First hint
┼ ¿ ¤
c t f

# Frequency
║: 1095
¿: 874
±: 704
╣: 683
¥: 594
╗: 569
╝: 566
═: 512
£: 458
╬: 422
®: 390
╔: 254
╩: 252
╦: 203
¤: 192
,: 179
┼: 175
┴: 168
©: 145
█: 139
Ø: 133
≡: 96
×: 68
': 66
↵: 51
.: 45
```
