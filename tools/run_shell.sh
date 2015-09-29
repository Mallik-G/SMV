#!/bin/bash

SMV_TOOLS="$(cd "`dirname "$0"`"; pwd)"
source $SMV_TOOLS/_env.sh

APP_SHELL_INIT=""
if [ -r "conf/shell_init.scala" ]; then
    APP_SHELL_INIT="-i conf/shell_init.scala"
else
    echo "WARNING: app level conf/shell_init.scala not found."
    echo
fi

spark-shell --executor-memory 6G --jars "$APP_JAR" -i "${SMV_TOOLS}/conf/smv_shell_init.scala" $APP_SHELL_INIT
