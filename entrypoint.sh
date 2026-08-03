#!/bin/sh
node /app/reset.cjs
exec node /app/bundle.cjs
