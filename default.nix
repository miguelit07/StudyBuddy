let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in 
with pkgs;

mkShell {
  name = "media-devices";
  nativeBuildInputs = [
    pkg-config python3 sqlite
  ];
  buildInputs = [
  ];
  dbus = pkgs.dbus;
  shellHook = ''
    # Tells pip to put packages into $PIP_PREFIX instead of the usual locations.
    # See https://pip.pypa.io/en/stable/user_guide/#environment-variables.
    export PIP_PREFIX=$(pwd)/_build/pip_packages
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    unset SOURCE_DATE_EPOCH

    if [ -d "./env" ]; then
      source ./env/bin/activate
    else
      if [ -d "./venv" ]; then
        source ./venv/bin/activate
      else
        python -m venv env
        source ./env/bin/activate
      fi
    fi
  '';
}
