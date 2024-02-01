# Questset

![vr_teaser](https://github.com/signetlabdei/questset/assets/156791134/ad7bd1e4-ec09-47a9-b160-1c3a2225202f)


The dataset is organized in two folders: complete and incomplete data. 
The former corresponds to the data collected from 60 participants who experienced at least 10 minutes for each of the two VR games and could complete the entire experiment.
The latter stores the data of 10 additional participants who felt sick during the experiment and could not complete it.
The corresponding traces are thus either shorter than 10 minutes or partial, and some participants only played the first game before they withdrew. 

The data for each user is saved in a directory named group\<G\>\_order\<O\>\_user\<u\> according to the group\<G\>\_order\<O\>\_user\<u\>\_\<g\>\_\<t\> format, where

* 𝐺 ∈ {1, 2} is the group ID, with 1 and 2 representing the two groups;
* 𝑂 ∈ {1, 2} indicates whether the slow game was played first (1) or second (2);
* 𝑢 ∈ {0, 1, . . . , 𝑁𝑢𝑠𝑟 − 1} is the user ID, with 𝑁𝑢𝑠𝑟 corresponding to the number of users per group-order combination. 𝑁𝑢𝑠𝑟 = 15 for all the groups in the Complete dataset, whereas the number of users in the Incomplete part varies;
* 𝑔 ∈ {slow, fast} indicates whether the game is fast or slow;
* 𝑡 ∈ {movement, traffic} is the type of data.

The traffic files contain the following information:

* time - timestamp in seconds from the beginning of recording
* size - size of the packet in bytes (including 27 bytes of USBPcap pseudoheader)
* direction - direction of the packet (DL: downlink, UL: uplink)

A packet is considered to be a downlink packet if it is sent from the PC to the HMD, and an uplink packet if it is sent from the HMD to the PC.

The movement files contain the following information: 

* TouchButtons - provides information about whether the  Right thumbstick, A, B, Left thumbstick, X, Y, and Menu buttons are pressed
* LeftIndexTrigger - provides information about the level of pressure applied on the left trigger buttons in a 0 to 1 scale
* RightIndexTrigger - provides information about the level of pressure applied on the right trigger buttons in a 0 to 1 scale
* LeftHandTrigger - provides information about the level of pressure applied on the left grip buttons in a 0 to 1 scale
* RightHandTrigger - provides information about the level of pressure applied on the right grip buttons in a 0 to 1 scale
* LeftTouchPosX, LeftTouchPosY, LeftTouchPosZ - provide information about the position of the left controller, with respect to the intial position
* LeftTouchOrientationW, LeftTouchOrientationX, LeftTouchOrientationY, LeftTouchOrientationZ - provide information about the orientation of the left controller, in quaternions, with respect to the inital pose
* RightTouchPosX, RightTouchPosY, RightTouchPosZ - provide information about the position of the right controller, with respect to the intial position
* RightTouchOrientationW, RightTouchOrientationX, RightTouchOrientationY, RightTouchOrientationZ - provide information about the orientation of the right controller, in quaternions, with respect to the inital pose
* HeadPosX, HeadPosY, HeadPosZ - provide information about the position of the headset, with respect to the intial position
* HeadOrientationW, HeadOrientationX, HeadOrientationY, HeadOrientationZ - provide information about the orientation of the headset, in quaternions, with respect to the inital pose
* time - timestamp in seconds from the beginning of recording 

For the position information, the x coordinate is associated the horizontal direction, the y coordinate is associated to the vertical direction, and the z coordinate is associated to the depth direction.

The TouchButton column contains a numerical value which indicates which button is pressed according to the following rule:

* A - 1
* B - 2
* Thumb - 4
* X - 256
* Y - 512
* Menu - 1048576
* Thumb - 1024

When two or more buttons are pressed at the same time, the TouchButton column contains the sum of the corresponding values.

The complete and incomplete data folder additionally store:

* The SSQ.csv file
* The Intial survey.csv file
* The dataset_info.csv file

The SSQ file contains 4 rows for each user correspnding to the SSQ answers provided before and after each game. Each row contains the ratings (None, Slight, Moderate and Severe) for each cybersickness symptom [1]. Additionally, there is a column for optional notes.
The Intial survey contains age, gender, preivious VR experience (in a 1 to 5 scale), and previous general gaming experience (in a 1 to 5 scale).
The dataset_info.csv file contains the following columns:

* Traffic filepath - the path of the traffic traces file
* Movement filepath - the path of the movement file
* Group - group ID
* Order - game order
* Game speed - game velocity
* Game name - name of the game
* User - user ID
* Duration (Traffic) - duration of the traffic data in seconds
* Duration (Movement) - duration of the movement data in seconds
* N Samples (Traffic) - number of samples in the traffic data
* N samples (Movement) - number of samples in the movemet data

The "Position and orientation sample plots" folder contains two sample codes (Matlab: "sample_plot.m", Python: "sample_plot.py") to parse the movement data file and convert from quaternions to euler angles.
In the same folder, we provide the file "sample_movement_data.csv" which has been recorded while performing the following actions:

One step back (z +)
One step forward (z -)
One step left (x -)
One step right (x +)
Crouch (y -)
Tiptoe (y +)
Look down (pitch -)
Look up (pitch +)
Look left (yaw +)
Look right (yaw -)
Tilt head left (roll +)
Tilt head right (roll -)

References

[1] R. S. Kennedy, N. E. Lane, K. S. Berbaum, and M. G. Lilienthal. 1993. Simulator Sickness Questionnaire: An Enhanced Method for Quantifying Simulator Sickness. The International Journal of Aviation Psychology 3, 3 (1993), 203–220.
