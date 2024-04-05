`rosrun ear earwrapper.py`

#Send message from Ear_angle node:
`rostopic pub -1 /Ear_angle std_msgs/Int32 -- [angle value in int]`

#Send message from personality node:
`rostopic pub -1 /shown_personality std_msgs/String "data: 'smirk'"`
