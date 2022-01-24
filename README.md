# Computer-Vision-Mouse-

Computer Vision based Mouse 

The Computer Vision - Mouse, is an interactive virtual mouse that uses only the webcam of a computer to control the cursor of a computer.

# Background + Theory:  

A state of art review of the field of study, including current developments, controversies and breakthroughs, previous research and relevant background theory. There may possibly be two literature-based chapters, one on methodological issues, which demonstrates knowledge of the advantages and disadvantages, and another on theoretical issues relevant to the topic/problem.
* the wider context of the project;
* the anticipated benefits of the system;
* likely users of the system;
* any theory associated with the project;
* the software development method(s) used;
* any special diagramming conventions used;
* existing software (or hardware) that is relevant to the system;
and so on.

The primary concept applied in this project is computer vision. Computer vision is the subfield of Artificial Intelligence that involves the ability of computers and systems to derive information from images and videos. The information can then be used to make recommendations and other actions. Here, the video is received from the camera(webcam)and vision is used to move the mouse cursor based on the movement of users hands in the viewing angle.

According to the 2016 global information technology report upwards of 90% of UK households own a computer. The report highlighted the importance of owning a computer for living in society. The mouse is a fundamental component of the user experience in computers and it is vital that its usability offers alternatives. This project is essentially a computer mouse. It's important to create a product that creates an alternative human-computer experience. This mouse uses finger gestures to control and requires no physical component. 

This project aims to create a virtual device that can give the user the ability to control the cursor of a computer. It is using nothing but a camera that connects to the computer system. Here, the camera is the webcam of the laptop or PC that will act as an intermediate between the user and system. 

THe project is aimed at a specific niche of potential customers/users. This includes primarily users who can’t use a physical mouse because of grip problems such as people with arthritis or tunnel syndrome. The project is also aimed at children as well who may want a more interactive and playful experience with devices. The device is finally also can just be used for fun to provide an alternative mouse solution to the one that most users are accustomed to,  

The project is developed in Python. Python is a programming language that is dynamically typed and has a strong connection with object oriented principles. It also has extensive compatibility with powerful libraries that are important for the development of a project of this scale. These factors make python the most logical choice in developing the project. The main core packages used in this product are Media Pipe, OpenCV and NumPy.

Media pipe is an open-source media library that offers machine learning solutions to live media such as videos. Here it is used for the hands functionality i.e. tracking of the hand. Tracking the hand movements is an important aspect of the project that defines the movement of the cursor as well as the clicking functionality. The left click is defined by touching the index and middle finger together and the right click is defined as touching the index,middle and ring fingers together. 

The hand landmark model is the model used from Media Pipe to track the hand. 



This model provides 21 key points inside the hand as coordinates. These coordinates have been annotated using thirty thousand images of unique hands in different angles making it an accurate model for tracking the various points of the hand. The most important coordinates of the hand are the tips of each finger. They are divisible by 4 and we'll be important for later on in the development.. Another point is that all the fingers are pointing in the same direction except the thumb this will be important as well.

The other library used here is OpnCV. OpenCV is a machine learning library used for carrying out computer vision functions. Since computer vision is at the core of what the project is doing, the use of openCV is handy in developing such a system. 

Numpy is a python library that supports the use of arrays in python. PyAutoGui is a python library that helps in controlling the mouse. 

There are some constraints that this development has . Since the project is software based it is limited by the computational power of the system it runs on. Hence, the product is more efficient on more advanced modern systems like an i7 over older systems like an i3. The product is also deployed as a windows application .exe file. Although it could be run in Anaconda, a data science platform, on a Mac it is not as efficient. Also the camera quality is another factor that helps since the project uses webcam footage.    

When it comes to the software development and design of the project the Waterfall Method was used with an emphasis on testing.

The waterfall method consists of :

* Requirement Analysis 
* System Design 
* Implementation 
* Testing 
* Deployment 

Here, testing is a phase that is continuously used throughout and played a big part in the completion of the project. 

A programming principle used is modular programming which consists of breaking down the program into smaller modules. This helps in testing the system periodically rather than testing after completing the entire development phase. 

To help plan out the code various design  

In order to demonstrate the achievement of the stated aims the project will need to create an application that controls the functionalities of the mouse: moving the cursor, left clicking the mouse and right clicking the mouse.The application also needs to show a Graphic User Interface in the manner of a trackpad. All these need to be done without sacrificing the efficiency of the application and maintaining a relative ease of use while obviously working in real time without lag.
