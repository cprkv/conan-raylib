
test:
	conan create . ckristen/master --build=missing

export:
	conan export . ckristen/master && conan test test_package raylib/2.0.0@ckristen/master 

upload:
	conan upload raylib/2.0.0@ckristen/master -r ckristen --all