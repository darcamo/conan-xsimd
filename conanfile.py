from conans import ConanFile, CMake, tools
import shutil
import os


class XtensorxsimdConan(ConanFile):
    name = "xtensor-xsimd"
    version = "6.0.0"
    license = "BSD-3"
    url = "https://github.com/darcamo/conan-xsimd"
    description = "Modern, portable C++ wrappers for SIMD intrinsics and parallelized, optimized math implementations "
    no_copy_source = True
    homepage = "https://github.com/QuantStack/xsimd"
    generators = "cmake"
    # No settings/options are necessary, this is header only

    def requirements(self):
        self.requires("gtest/1.8.0@bincrafters/stable")

    def source(self):
        tools.get("https://github.com/QuantStack/xsimd/archive/{0}.zip".format(self.version))
        shutil.move("xsimd-{0}".format(self.version), "sources")

        tools.replace_in_file("sources/CMakeLists.txt", "project(xsimd)",
                              """project(xsimd)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()""")

    def build(self):
        cmake = CMake(self)
        os.mkdir("build")
        shutil.move("conanbuildinfo.cmake", "build/")
        cmake.configure(source_folder="sources", build_folder="build")
        cmake.install()

    # def package(self):
    #     self.copy("*.h", "include")
