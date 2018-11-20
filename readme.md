# Conan raylib package

## Installation

Add remote to get ckristen packages from bintray:  
`conan remote add ckristen https://api.bintray.com/conan/ckristen/conan`

Add dependency to your project:  
`raylib/2.0.0@ckristen/master`

## Warning

Current package requires GLWF package from conan (bincrafters repo),
To install it you need to add another remote:  
`conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan`

With installation of GLFW package in ubuntu-like systems conan will run apt-get to install dependencies globally (that's bad, I will fix it later).

## ToDo

- Tests on Windows, MacOS
- flags in src/src/CMakeOptions.txt