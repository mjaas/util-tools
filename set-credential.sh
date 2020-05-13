#!/bin/bash

input_env=$1

if [ "$input_env" = "dev" ]; then
  export AWS_ACCESS_KEY_ID="hoge-dev"
  export AWS_SECRET_ACCESS_KEY="hoge-sec-dev"
  echo "Set dev credential"
elif [ "$input_env" = "stg" ]; then
  export AWS_ACCESS_KEY_ID="hoge-stg"
  export AWS_SECRET_ACCESS_KEY="hoge-sec-stg"
  echo "Set stg credential"
elif [ "$input_env" = "prd" ]; then
  export AWS_ACCESS_KEY_ID="hoge-prd"
  export AWS_SECRET_ACCESS_KEY="hoge-sec-prd"
  echo "Set prd credential"
elif [ "$input_env" = "ci-prd" ]; then
  export AWS_ACCESS_KEY_ID="hoge-ci-prd"
  export AWS_SECRET_ACCESS_KEY="hoge-sec-ci-prd"
  echo "Set ci-prd credential"
else 
  echo "unknown env"
fi