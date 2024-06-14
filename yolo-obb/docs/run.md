# Running Containers

Let's say that you found a container image from the [DockerHub](https://hub.docker.com/repositories/leehoanzu), or [built your own container](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/docs/build.md) - the normal way to run an interactive Docker container on your Jetson would be using [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) like this:

``` bash
$ sudo docker run --runtime nvidia -it --rm --network=host CONTAINER:TAG
```

The [`jetson-containers run`](https://github.com/leehoanzu/angle-detection/blob/main/run.sh) launcher can be run from any directory and forwards its command-line to [`docker run`](https://docs.docker.com/engine/reference/commandline/run/), with some added defaults - including the above flags mounting various devices for display, audio, and video (like V4L2 and CSI cameras)

``` bash
$ jetson-containers run CONTAINER:TAG                   # run with --runtime=nvidia, default mounts, ect
$ jetson-containers run CONTAINER:TAG my_app --abc xyz  # run a command (instead of interactive mode)
$ jetson-containers run --volume /path/on/host:/path/in/container CONTAINER:TAG  # mount a directory
```

The flags and arguments to [`jetson-containers run`](https://github.com/leehoanzu/angle-detection/blob/main/run.sh) are the same as they are to [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) - anything you specify will be passed along.