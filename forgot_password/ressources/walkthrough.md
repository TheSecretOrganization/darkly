# forgot_password

Go to the `/?page=recover` page and inspect the elements.
You should find a `form` with an hidden input named `mail`.
Replace the value with anything you want, then press `Sumit`

## Reason

We can assume that the server will send an email to the `mail` input. So if we change it, we could receive the email with a new password
