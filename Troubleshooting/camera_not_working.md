## Camera Troubleshooting

If the camera will not open but the light is turned on:
    run ```ll /dev/astra*``` to see the ports of the camera
    Go into run_docker.sh file and include the correct ports from the output of the previous command

If that does not work:
    Double check camera connections, if there is not a green light on the camera, then something is not plugged in correctly

If you have problems running code to open the camera (camera will not stay on): 
    If the video port was busy, which can happen if the camera program wasn't closed or stopped abruptly to search for the next com port and open that port instead.    