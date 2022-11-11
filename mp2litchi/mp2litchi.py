"""
Mission Planner to Litchi Converter by https://github.com/YarostheLaunchpadder
"""
import os


def welcome():
    """
    Welcome messages
    """
    print("WELCOME TO MISSION PLANNER TO LITCHI CONVERTER!\n")
    print("Converted files will be saved to the same directory the source file is in.\n")


def convert(filename: str):
    """
    Converts a single file
    :param filename: The path to the file. e.g.: /home/user/any/file.waypoints
    """
    while not os.path.exists(filename):
        filename = input("\nCouldn't find path to Mission Planner file, please try again: ")

    if not filename.endswith(".waypoints"):
        filename += ".waypoints"

    file = open(filename, "r").read()
    file = str(file.split("\t"))
    file = file.replace("\\n", "', '")
    file = file.replace("'", "")
    file = file.strip('][').split(', ')

    file_list = file

    if file[1] == "0":
        del file_list[0:13]

    file_list = [file_list[x:x + 12] for x in range(0, len(file_list), 12)]

    waypoint_list = []

    for lst in file_list:
        try:
            if lst[3] == "16":
                waypoint_list.append(lst)

        except:
            pass

    output_string = "latitude,longitude,altitude(m),heading(deg),curvesize(m),rotationdir,gimbalmode,gimbalpitchangle,actiontype1,actionparam1,actiontype2,actionparam2,actiontype3,actionparam3,actiontype4,actionparam4,actiontype5,actionparam5,actiontype6,actionparam6,actiontype7,actionparam7,actiontype8,actionparam8,actiontype9,actionparam9,actiontype10,actionparam10,actiontype11,actionparam11,actiontype12,actionparam12,actiontype13,actionparam13,actiontype14,actionparam14,actiontype15,actionparam15,altitudemode,speed(m/s),poi_latitude,poi_longitude,poi_altitude(m),poi_altitudemode,photo_timeinterval,photo_distinterval\n"

    for row in waypoint_list:
        try:
            output_string = output_string + row[8] + "," + row[9] + "," + str(int(float(row[
                                                                                            10]))) + ",0,0,0,0,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,1,0,0,0,0,0,-1," + str(
                round(float(file_list[file_list.index(row) + 1][4]), 3)) + "\n"
        except:
            output_string = output_string + row[8] + "," + row[9] + "," + str(int(float(row[
                                                                                            10]))) + ",0,0,0,0,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,0,1,0,0,0,0,-1,-1,-1"
    with open(f"{filename}.csv", "w") as output_file:
        output_file.write(output_string)
        output_file.close()

    print(f"\nFile saved: {filename}.csv")
