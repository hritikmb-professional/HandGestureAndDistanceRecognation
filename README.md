# HandGestureAndDistanceRecognation
Real-time hand gesture recognition using OpenCV and Mediapipe. Detects Thumbs Up, Thumbs Down, and Peace Sign while estimating hand distance. Built with Python for interactive applications. 
Hand gesture recognition is a crucial aspect of human-computer interaction, enabling intuitive control in various applications such as sign language interpretation, gaming, virtual reality, and robotics. This project implements real-time hand detection, gesture recognition, and distance estimation using OpenCV and Mediapipe. The system detects hand gestures such as Thumbs Up, Thumbs Down, and Peace Sign, while also estimating the distance of the hand from the camera.  

The main objectives of this project are to develop a real-time hand detection system using Mediapipe and OpenCV, recognize specific hand gestures including Thumbs Up, Thumbs Down, and Peace Sign, estimate the distance of the hand from the camera based on the bounding box size, and provide an intuitive user interface with real-time feedback.  

For implementation, Python is used as the programming language along with libraries such as OpenCV, Mediapipe, and NumPy. A webcam is used for real-time video processing.  

The approach consists of several key steps. The first step is hand detection, where the Mediapipe Hands module is used to detect hands and track key landmarks. It processes frames in real-time and extracts twenty-one landmark points per detected hand.  

The second step is gesture recognition, where the system classifies gestures based on the position of the landmarks. A Thumbs Up gesture is detected when the thumb is raised higher than the other fingers. A Thumbs Down gesture is identified when the thumb is positioned lower than the other fingers. A Peace Sign is recognized when the index and middle fingers are raised while the other fingers remain down.  

The third step is distance estimation. A bounding box is calculated around the detected hand, and the relative size of the bounding box is used to estimate the distance of the hand from the camera. A larger bounding box indicates that the hand is closer to the camera, while a smaller bounding box suggests that the hand is farther away.  

In terms of visualization, a bounding box is drawn around the detected hand, and the recognized gesture along with the estimated distance is displayed on the screen.  

The implementation follows a structured approach. The Mediapipe Hands model is initialized with confidence thresholds. Video frames are captured using OpenCV and processed to detect hands and extract landmark positions. A bounding box is then computed around the detected hand, and distance is estimated using the bounding box size. The system classifies hand gestures based on landmark positions, and the results, including the bounding box, recognized gesture, and estimated distance, are displayed on the screen.  

The project demonstrates strong performance in real-time hand tracking with high accuracy. Gestures are correctly classified with minimal errors, and distance estimation provides approximate values based on the size of the hand in the frame. The bounding box and gesture classification text are clearly displayed.  

However, the project has some limitations. Distance estimation is approximate and can vary based on camera specifications. Poor lighting conditions or cluttered backgrounds may reduce accuracy, and the system works best when the hand is clearly visible to the camera.  

In conclusion, this project successfully implements real-time hand detection, gesture recognition, and distance estimation using OpenCV and Mediapipe. It lays the foundation for gesture-based interfaces that can be integrated into robotics, gaming, and sign language recognition applications. Future improvements include fine-tuned distance measurement using depth sensors and expanding gesture recognition to more complex signs.  

Potential future enhancements include improving distance estimation using depth cameras, expanding the gesture vocabulary to support additional hand signals, integrating the system with IoT devices for smart home control, and deploying it as a mobile or web application for wider usability.  
