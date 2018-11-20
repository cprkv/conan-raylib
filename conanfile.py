from conans import ConanFile, CMake, tools
import os


class RaylibConan(ConanFile):
    name = "raylib"
    version = "2.0.0"
    license = "MIT"
    url = "https://github.com/veyroter/conan-raylib"
    description = "conan raylib package"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src%s*" % os.sep
    requires = "glfw/3.2.1@bincrafters/stable"

    def build(self):
        print("self.dir_bld(): %s" % self.dir_bld())
        print("self.dir_src(): %s" % self.dir_src())
        cmake = CMake(self)
        tools.mkdir(self.dir_bld())
        cmake.configure(source_folder=self.dir_src(),
                        cache_build_folder=self.dir_bld())
        cmake.build(build_dir=self.dir_bld())

    def package(self):
        self.copy("*.h", src="%s%ssrc" % (self.dir_src(), os.sep), dst="include", keep_path=False)
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

    def dir_src(self):
        try:
            return self.src_full_path
        except:
            self.src_full_path = "%s%ssrc" % (self.source_folder, os.sep)
            return self.src_full_path

    def dir_bld(self):
        try:
            return self.build_full_path
        except:
            self.build_full_path = "%s%sbuild" % (self.dir_src(), os.sep)
            return self.build_full_path        

        # tcc -o core_basic_window.exe core_basic_window.c -std=c99 -Wall -lmsvcrt -lraylib -lopengl32 -lgdi32 -lkernel32 -lshell32 -luser32 -Wl,-subsystem=gui