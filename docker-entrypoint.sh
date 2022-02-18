#!/bin/sh

make devserver PORT=9090

exec "$@"
