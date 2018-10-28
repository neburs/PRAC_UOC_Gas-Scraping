#!/bin/bash

if [[ "$(docker images -q uoc-tipologia-prac1:latest 2> /dev/null)" == "" ]]; then
  docker build --tag uoc-tipologia-prac1:latest --force-rm docker/.
fi

docker run -ti --rm -v "`pwd`/":/data uoc-tipologia-prac1:latest /bin/bash -c "cd /data && python $@"