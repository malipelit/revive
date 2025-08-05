# Smart Home Security System (Capstone Project)

This project is a smart home security system designed to enhance safety through affordable and easy-to-implement technology. It uses face recognition to identify residents and detect unknown individuals, notifying homeowners via mobile alerts. Motion within a 5-meter range is monitored using Passive-Infrared sensors, and suspicious actions like loitering or carrying a weapon trigger alarms. Residents can label visitors as residents, guests, or intruders, and all entries and exits are logged. The system, built with just two cameras, a Jetson Nano processor, and basic sensors, ensures privacy by keeping all data accessible only to the homeowner.

### Technologies Used
- **Jetson Nano** – Edge computing device for real-time processing
- **Cameras (x2)** – Used for face recognition and activity monitoring
- **Passive Infrared (PIR) Sensor** – Detects motion up to 5 meters
- **Ultrasonic Sensor (HC-SR04)** – Measures distance and proximity
- **Buzzer and Alarm System** – Triggers audible alerts during intrusions
- **Web Application** – Sends real-time notifications and allows user tagging
- **Database System** – Stores logs of entries, exits, and visitor tags

### Algorithms and Techniques
- **Face Recognition** – Identifies residents and detects unfamiliar faces
- **Image Processing** – Detects suspicious behaviors (e.g., loitering, weapon carrying)
- **Motion Detection Algorithm** – Processes PIR sensor data to detect movement
- **Intrusion Detection Logic** – Evaluates and classifies security threats
- **Notification System Logic** – Sends alerts via SMS, email, or app