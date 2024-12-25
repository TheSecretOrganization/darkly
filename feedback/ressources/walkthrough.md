# xss

At the page `/?page=feedback` there is two input. We can check if there are
protected against xss injections with a message that contains
```
<script>alert</script>
```
Here the flag appear in the comments
