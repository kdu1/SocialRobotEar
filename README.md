`rosrun ear ear.py`

#Send message from Ear_angle node:
`rostopic pub -1 /Ear_angle std_msgs/Float32 -- AngleValueFloat`

#Send message from personality node:
`rostopic pub -1 /Shown_personality std_msgs/String "data: 'smirk'"`
