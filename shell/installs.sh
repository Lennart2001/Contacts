#!/bin/bash

INSTALL_NAMES=("opencv-python" "pillow" "numpy" "prompt_toolkit")
IMPORT_NAMES=("cv2" "PIL" "numpy" "prompt_toolkit")

length=4

for ((x=0; x<$length; x++)); do
  import_name=${IMPORT_NAMES[$x]}
  echo "Checking for $import_name..."

  python3 -c "import $import_name" 2> /dev/null

  if [ $? -ne 0 ]; then
    install_name=${INSTALL_NAMES[$x]}
    echo "$import_name is not installed. Installing now..."
    pip3 install "$install_name"
  else
    echo "$import_name is already installed."
  fi
done
