# Item Catalog Application
This is a web Application that provides a list of items within a variety of categories as well as provide a third party authentication and authorization service. Registered users will have the ability to post, edit and delete their own items.

## Prepare the Application
* You should have the virtual machine `VirtualBox` and `Vagrant` installed on your device.
* Clone the fullstack-nanodegree-vm [here](https://github.com/udacity/fullstack-nanodegree-vm)
* Download Vagrant and go to the same directory where you downloaded vagrant and put the downloaded the project folder `ItemCatalogApp`
* Bring up the virtual machine with `vagrant up` and log into it with `vagrant ssh`.
* Run the Application.py file `python application.py`
* Go to localhost:5000/catalog to try the Application
* First login, then you can create your own items and you can modify them or delete them.
* You can add more categories and items in `fill_categories.py` file and uncomment it and add more categories if you like.
* Go to 'localhost:5000/catalog.json' and 'localhost:5000/catalog/<int:category_id>/<title>.json' or add '.json to the end of the route for a specific item to access JSON endpoints.
* Go to this [link](https://console.developers.google.com/) and create a project to use Google API for Google accounts to have your own client_id and client_secret to replace these in 'application.py' in line 
## References
* https://developers.google.com/identity/protocols/OpenIDConnect
* I used some code from Udaciy lessons under Third party authentication section.
* I also mostly refer to Stackoverflow if I get confused about something or to get more info.
* Google sign in button [here](https://stackoverflow.com/questions/46654248/how-to-display-google-sign-in-button-using-html)
