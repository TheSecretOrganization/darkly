# file_upload

In the page `/?page=upload`, we can observe the option of upload a file.
What if we upload a wrong type of file ? For this, we will use this curl command

```bash
curl -F "uploaded=@file.txt;type=image/jpg" -F Upload=Upload 'http://<ip>/?page=upload'
```

> The  `-F` option specify an input attended by the backend.

> A local file to upload is needed, here `file.txt`

This gave us the flag.
