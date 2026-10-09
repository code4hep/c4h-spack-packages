# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Code4hep(CMakePackage):

    homepage = "https://github.com/code4hep/Code4hep"
    git = "https://github.com/code4hep/Code4hep.git"

    #maintainers("")

    #license("")
    version("main", branch="main")
    version("2026-10-09", commit="628f3172203e1b3e6602fdbe6c9f35f6df657e9b")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.23:", type="build")
    depends_on("python@3:", type=("build", "link"))

    depends_on("root +geom +math")
    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("geant4")
    depends_on("stitched@2026-09-30:", when="@2026-10-09:")
    depends_on("k4geo")
    depends_on("lcio")
    depends_on("boost +program_options")
    depends_on("catch2")
    depends_on("py-pybind11")
    depends_on("hepmc3")
    depends_on("pythia8")

    def cmake_args(self):
        return [
            # Code4hep links Geant4::Geant4 and Pythia8::Pythia8. Geant4's CMake
            # config only sets variables (no imported target) and Pythia8 is an
            # Autotools package with no CMake config, so the find modules in
            # cmake-modules/ create these two targets.
            self.define("CMAKE_MODULE_PATH", os.path.join(self.package_dir, "cmake-modules")),
            # FindPythia8.cmake locates Pythia8 through this prefix.
            self.define("PYTHIA8_ROOT", self.spec["pythia8"].prefix),
        ]
