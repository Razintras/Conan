from conan import ConanFile, tools 
from conan.tools.files import copy
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class HelloConan(ConanFile):
    name = "hello"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"
    exports_sources = "*"
    url = "svn+ssh://build-com-lin-01/svn/JenkinsTestClaude/trunk/Hello"
    
    def layout(self):
        # Specify where the source files are located and where to build
        self.folders.source = "."
        self.folders.build = "build"
    
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        
        
    def copy_sources(self):
        # Copy all source files to the build folder
        copy(self, "*", self.source_folder, self.build_folder)

    def build(self):
        self.copy_sources()  # Call the copy_sources method before configuring
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
