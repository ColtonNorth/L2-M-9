# L2-M-9
Repository containing code for our Quality Flow project.

For this project, an Android app was created with the use of Android studio. The app is used to control 4 raspberri pi's and their corresponding sensors.

A user would sign in with a username and password, which are stored inside a database on the server raspberry pi. A thingspeak channel is updated with the entered username and password and the raspberry pi checks to ensure they match those inside the database. If they do, another thingspeak channel is updated to allow the user to sign into the app.

Once signed in, the user can enter an email to get notifications from the app, or they can check the various measurements that are being recorded by the sensors. If any of the values read by the sensors are at dangerous levels, the server raspberry pi will send emails to notify the user that they may be in danger. 

