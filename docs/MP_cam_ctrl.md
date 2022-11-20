# [Mission Planner](https://ardupilot.org/planner/) survey flight plan using [camera control](https://ardupilot.org/copter/docs/mission-command-list.html#do-digicam-control)

## What is [camera control](https://ardupilot.org/copter/docs/mission-command-list.html#do-digicam-control)?

[Camera control](https://ardupilot.org/copter/docs/mission-command-list.html#do-digicam-control) 
is the `Trigger Method` selected in [Mission Planner](https://ardupilot.org/planner/).
This creates a waypoint for each image to be taken.
The [camera control](https://ardupilot.org/copter/docs/mission-command-list.html#do-digicam-control) waypoints 
are calculated based on the camera, the flight height and the overlap.
The [camera control](https://ardupilot.org/copter/docs/mission-command-list.html#do-digicam-control) waypoints 
can be configured to have a delay. The delay stops the aircraft for the configured time, captures the image 
after that delay and continues with the flight-plan afterwards.
The delay is meant to stabilize the aircraft and to capture the image without any blur due to movement. That way
the flight speed can be much higher than in the 
[trigger distance](https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/MP_trigger_dist) 
mode.

### Example

The [camera control](https://ardupilot.org/copter/docs/mission-command-list.html#do-digicam-control) 
waypoints are configured to have a delay time of 1 second.
The aircraft will travel to the next 
[camera control](https://ardupilot.org/copter/docs/mission-command-list.html#do-digicam-control) 
waypoint, wait for 1 second, capture an image 
and continue to the next waypoint.

## What are the advantages and disadvantages?

### Pro

- Avoids image blur
  - at low altitudes
  - during high exposure time / low light conditions
  - flight speed is 0 while capturing the image
- Altitude above ground remains constant between images (each waypoint is set to AGL)

### Con

- Lots of waypoints
- Longer mission duration

# Workflow
To create a flight-plan in [Mission Planner](https://ardupilot.org/planner/) and import it 
into [Litchi Mission Hub](https://flylitchi.com/hub), follow these steps.

## [Mission Planner](https://ardupilot.org/planner/)

Start [Mission Planner](https://ardupilot.org/planner/) and select `Plan` in the top left corner.

### Set Home Point
Right-click on the location you want to set the home point and select `Set Home Here`.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/set_home.JPG?raw=true">

### Draw polygon

Left-click on the polygon icon in the top left corner and select `Draw Polygon`. Then draw the polygon area
by left-clicking on the map.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/draw_polygon.JPG?raw=true">

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/polygon.JPG?raw=true">

### Start survey tool

Right-click on the map and select `Auto WP` -> `Survey (Grid)`.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/survey_grid.JPG?raw=true">

### Settings for `Simple` tab

Select the `Camera`, set the `Altitude` and `Flying Speed`. Make sure to set `Use speed for this mission` 
and `Advanced Options`.

If your camera is not in the list, then you can load an image in the `Camera Config` tab. 
The camera settings will be set automatically using the metadata in the image.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/cam_ctrl/survey_grid_simple.JPG?raw=true">

### Settings for `Grid Options` tab

Set the `Overlap` (front-overlap) and the `Sidelap` (side-overlap) to your needs. Make sure to set `Delay at WP` to at 
least the time that the aircraft needs to stabilize. This depends on the aircraft, wind conditions and flight speed.

Also, if you need a cross-grid (e.g. 3D models or better DEMs), then set `Cross Grid` as well.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/cam_ctrl/survey_grid_grid_options.JPG?raw=true">

### Settings for `Camera Config` tab

Make sure to select `DO_DIGICAM_CONTROL` as the `Trigger Method`.

Also, you can click `Load Sample Photo` if your camera was not listed. You can then click `Save` to add it to 
the list of cameras.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/cam_ctrl/survey_grid_camera_config.JPG?raw=true">

### Save Grid

Navigate back to the `Simple` tab and click `Accept` in the bottom right corner.

### Export flight-plan as `.waypoints` file

Press `ctrl + s` to export the flight-plan.

## MissionPlanner-to-Litchi

Open `MissionPlanner-to-litchi` and click `Select files to convert`.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/mp2litchi_gui.JPG?raw=true">

### Select File or Files

Select the file you exported from [Mission Planner](https://ardupilot.org/planner/) and click `Open`.
MissionPlanner-to-Litchi will create a `.csv` file in the same directory.

In this example the file is named `diamonhead.waypoints` so the converted file will be `diamonhead.waypoints.csv`.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/mp2litchi_file_select.JPG?raw=true">

## [Litchi Mission Hub](https://flylitchi.com/hub)

Go to the [Litchi Mission Hub](https://flylitchi.com/hub) and log in to your account (top right corner).

### Set global settings

Clink on `SETTINGS` in the bottom left corner. Make sure that the marked settings are set as shown in the image 
then click `Close`.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/litchi_settings_menu.JPG?raw=true">

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/litchi_settings.JPG?raw=true">

### Import file

Click on `MISSIONS` in the bottom left corner.

Then select `Import...`. 

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/litchi_mission_menu.JPG?raw=true">

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/litchi_import.JPG?raw=true">

Select the `.csv` file. In this example it is the `diamonhead.waypoints.csv`.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/litchi_import_csv.JPG?raw=true">

Click `Import to new Mission` to import the flight-plan to the [Litchi Mission Hub](https://flylitchi.com/hub).

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/litchi_import_confirm.JPG?raw=true">

### Imported flight-plan

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/cam_ctrl/litchi_import_success.JPG?raw=true">

### Save the mission

You need to save the mission to be able to sync it to your control device (mobile phone / tablet).

To do this you click on `Missions` in the bottom left corner and select `Save...`.

<img src="https://github.com/YarostheLaunchpadder/MissionPlanner-to-Litchi/blob/main/docs/images/litchi_save_mission.JPG?raw=true">

Enter a name for your mission and click on `Save`.