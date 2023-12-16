FROM ubuntu:latest
LABEL authors="elik1"

ENTRYPOINT ["top", "-b"]