Server(socketTest.py): Turn .dxf file (generated from AutoCad) into x,y coordinate's format and send data into client's side.
Client(IC_Testing.exe): Receive data from server, then display the output in the top-right box. 
When clicking the button, it generate the circles based on the given coordinate in the left box and parse the data in format such as data shown below:
Circle 1 - X: 54.53297, Y: 80.56892, Radius: 1.1
Circle 2 - X: 112.933, Y: 22.16893, Radius: 1.1
Depends on user's demand, if they don't want to insert probe into a specific hole, they can turn on and turn off the circles by just clicking the circle itself.



<img width="538" alt="Screenshot 2024-08-14 092438" src="https://github.com/user-attachments/assets/bbde2183-d403-47d2-8422-4f8d49552853">
