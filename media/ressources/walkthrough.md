# media

In the page `/?page=media&src=nsa`, we can assume that
the `src` field is used in the `object` element in the page.

We can try to specify a [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types).

We can use the `text/html` type and pass value in base64 with `text/html;base64,`
and passing the encoded value of `<script>alert(42)</script>` that is 
`PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=` with the request
`/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=`.

The result is the flag.
