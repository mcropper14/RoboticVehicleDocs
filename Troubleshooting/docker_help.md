## Docker Commands

To get container id from container run: ```cat /proc/self/cgroup | grep "docker" | sed s/\\//\\n/g | tail -1 | cut -c 1-12```

Then open the docker container: ``` docker exec -it [id] /bin/bash ```

To commit changes to docker: ``` docker commit <id> <new_name> ```