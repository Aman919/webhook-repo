# webhook-repo
This repository contains 2 python files namely server.py, and util.py and a template folder which contains ui.html for UI.

# server
Here server.py is the main file containing all the routes and their definition and used mongodb cluster for storing data.
I have stored the values related to push and pull request in dictionary and stored it in mongodb cluster.

# UI
For UI, I have used javascript in ui.html, fetching value from the database in every 15 minutes and updating the same on the screen as been asked in the document. 

# Ngrok
I have used ngrok for real-time web UI where I can introspect all HTTP traffic running over my tunnels.
