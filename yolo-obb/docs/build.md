# Building Containers

The normal way to build container on your Jetson would be using [`docker build`](https://docs.docker.com/reference/cli/docker/image/build/) like this:

```bash
$ sudo docker build -t image .
```

## Changing the Base Image

By default, the base container image used at the start of the build chain will be [`l4t-base`](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-base) on JetPack 4, [`l4t-jetpack`](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-jetpack) on JetPack 5.  However, if you want to add packages to a container that you already have, you can specify your own base image:

```bash
FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3 # add pytorch to your container
```