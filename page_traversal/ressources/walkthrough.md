# page_traversal

On certains page we can see an url like `/?page=signin`, we can imagine that
the value of `page` is an relative path, it can enable us to access to
files like /etc/passwd. For this we can try to go backward until we found the file.
We can do this until we found the flag at `?page=../../../../../../../etc/passwd`.
