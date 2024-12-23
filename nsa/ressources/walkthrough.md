# nsa

At the end of the page, we can observe an hidden link in the footer.
This page lead us to `/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`
In this page, some commentaries can give us somes hints.

> You must come from : "https://www.nsa.gov/".

And

> Let's use this browser : "ft_bornToSec". It will help you a lot.

We can assume the first one make a reference to the `Referer` header and the second one
to the `User-Agent` one.

If we add thoses header in the request to the page, we got the flag.
