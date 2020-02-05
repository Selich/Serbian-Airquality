if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed.' >&2
  exit 1
fi
 
pip install --user virtualenv

source ./env/bin/activate

pip install -r requirements.txt
clear