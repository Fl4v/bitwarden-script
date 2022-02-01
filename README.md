# Bitwarden Script

Once upon a time, I moved all my passwords from Dashlane to Bitwarden. However, the site URIs weren't properly configured. In Dashlane, these appeard to be under the field `name`, in Bitwarden, these should be under `login_uri`.

Furthermore, not all the sites had a proper URL to resolve to. I could well open the exported passwords from Bitwarden in Excel and one by one copy all the URLs from one Column to the Other and give them proper name, but this wouldn't be fun. Instead, I wrote a simple script. Enjoy!
