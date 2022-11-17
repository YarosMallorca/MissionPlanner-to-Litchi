# Mission Planner to Litchi
#### Convert Mission Planner (ArduCopter) Waypoint Surveys to Litchi CSV Format to execute on DJI Drones

Litchi doesn't support Survey mode yet, but here is a workaround! You will need <a href=https://ardupilot.org/planner/docs/mission-planner-installation.html>Mission Planner</a> installed in order to plan your mission.

Warning: This script was tested successfully many times, should work stably. I'm not responsible for any damage of your drones by incorrect use of this software.

<a href="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/releases/download/Alpha/Mission.Planner.to.Litchi.exe">Click here to Download for Windows</a>

Mac version not available yet

<center>
<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/MissionPlanner_Screenshot.jpg?raw=true" height="300">
<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/Litchi_Screenshot.jpg?raw=true" height="300">
</center>

##### Here's how to use it:

1. Open Mission Planner
2. Go to the Plan tab in Mission Planner

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/1.jpg?raw=true" height="100">

3. Select `Absolute` as height reference. Do **not** check `Verify Height`. Let Litchi handle the AGL height adjustments.
   
<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/height_absolute.jpg?raw=true" height="100">

4. Click the Polygon Icon --> Draw a Polygon

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/2.jpg?raw=true" height="200">

5. Using clicks on the map, select the area you want to map

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/3.jpg?raw=true" height="250">

6. Right-click inside the polygon, select Auto WP --> Survey (Grid)

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/4.jpg?raw=true" height="350">

7. Adjust Settings like Altitude and Speed, also enable <b>Advanced Options</b>

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/5.jpg?raw=true" height="400">

8. In the Camera Config Tab, Set your camera settings, make sure the FOV values are correct after inputing all camera settings. You can save your camera preset by using the <b>Save</b> button. Also make sure the CAM_TRIGG_DIST is selected!

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/6.jpg?raw=true" height="400">

9. Go back to the Simple Tab, and click <b>Accept</b>

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/7.jpg?raw=true" height="450">

10. Make sure the layout on the map is correct. Example:

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/8.jpg?raw=true" height="400">

11. Save this mission as .waypoints file. Recommended save location is Desktop!

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/9.jpg?raw=true" height="300">
<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/10.jpg?raw=true" height="100">

12. Place the mission file and exe file on your Desktop

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/11.jpg?raw=true" height="200">

13. Open the script and select the files that you want to convert

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/mp2litchi_gui_main.jpg?raw=true" height="250">

14. The converted file (.csv) should be saved on your Desktop. Click <b>Enter</b> to exit the script.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/mp2litchi_gui_select.jpg?raw=true" height="250">

15. Go to Litchi Mission Settings and make sure that the selected in red settings (in the screenshot below) are set to desired values. Path Mode must be set to Straight Lines, otherwise the Auto-Photo mode will not work! `MissionPlanner to Litchi` sets the `photo capture interval` so the drone will take photos each **x** meters between the waypoints.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/14.jpg?raw=true" height="500">

16. Open <a href=https://flylitchi.com/hub>Litchi Mission Hub</a> and go to File --> Import

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/15.jpg?raw=true" height="250">

17. Select file and click <b>Import to new mission</b>

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/16.jpg?raw=true" height="200">

18. Review mission! 

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/Litchi_Screenshot.jpg?raw=true" height="400">

19. <b>Save</b> Mission!

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/Screenshots/17.jpg?raw=true" height="250">
