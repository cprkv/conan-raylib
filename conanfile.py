from conans import ConanFile, CMake, tools


class RaylibConan(ConanFile):
    name = "raylib"
    version = "2.0.0"
    license = "MIT"
    url = "https://github.com/veyroter/conan-raylib"
    description = "conan raylib package"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        src_full_path = "%s/src" % self.source_folder
        build_full_path = "%s/build" % src_full_path
        tools.mkdir(build_full_path)
        cmake.configure(source_folder=src_full_path, cache_build_folder=build_full_path)
        cmake.build(build_dir=build_full_path)

    def package(self):
        self.copy("*.h", src="include", dst="include", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.so.*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libraylib.a"]

        if self.settings.os == "Linux":
            self.cpp_info.libs.extend(["dl", "m"])
        # tcc -o core_basic_window.exe core_basic_window.c -std=c99 -Wall -lmsvcrt -lraylib -lopengl32 -lgdi32 -lkernel32 -lshell32 -luser32 -Wl,-subsystem=gui
