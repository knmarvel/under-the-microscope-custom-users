# under-the-microscope-custom-users
Implementing a Django custom user from the ground up

There are two ways to extend users in Django: the "profile" method and a custom user. We've already used the profile method for our first project, so now we'll cover the custom user.

This project is simply about implementing a custom user from the ground up so that you can use it in the next assignment.

# Your Task

Implement your own login and signup page (don't use the defaults) for the server that leads to a locked-down "homepage". The homepage should show:

    the username & display name of the person who is logged in
    output the value of `settings.AUTH_USER_MODEL`

NOTE: DO NOT name any part of your app "user" -- it will have conflict with the built-in user model and give you all sorts of errors that are really difficult to debug if you don't know what you're looking for. Use "custom_user", "myuser", "dudewheresmyuser"... literally anything but "user" will work.

# Extra credit (2 points):

Extend your custom user field so that it has the following nullable fields:

    Homepage (URLField)
    Display Name (CharField)
    Age (IntegerField)

(this is the hard part) Make the custom fields appear on the admin panel and available for editing. 1 additional bonus point if you make the superuser command ask for their age.
Submission

Submit a link to your repo

### The homepage displays the username & display name of currently logged-in user
### Implements functional custom user model
### Extra Credit: 
1) Extend your custom user field so that it has the following nullable fields:
Homepage (URLField)
Display Name (CharField)
Age (IntegerField)

2) Make the custom fields appear on the admin panel and available for editing.
### Extra Credit: 
Make the superuser command ask for their age.
### Repo contains pyproject.toml that includes all necessary dependencies to run application
### The homepage displays the output value of settings. AUTH_USER_MODEL
