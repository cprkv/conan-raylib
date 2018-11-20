
testing:
	conan create . ckristen/main

upload:
	conan upload raylib/2.0.0@ckristen/main -r ckristen --all