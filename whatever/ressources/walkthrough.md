# whatever

In the file at `/robots.txt`, there is a reference to `/whatever` with a file
name `htpasswd` that contains
```
root:437394baff5aa33daa618be47b75cb49
```
This is formatted as follow `user:password`. The password id encrypted with
md5 and is `qwerty123@`.
On the same time, while testing frequently used url, we found the `/admin` page.
If we test the gained credentials, we got the flag.
