# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class StitchedExample(CMakePackage):
    """Example package using the Stitched framework"""

    homepage = "https://github.com/code4hep/stitched-example"
    git = "https://github.com/code4hep/stitched-example.git"

    maintainers("makortel")

    license("Apache-2.0", checked_by="makortel")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("stitched@2026-08-19", when="@2026-08-21")
    depends_on("stitched@2026-09-19", when="@2026-08-19:")

    version("2026-08-21", commit="afce55fd2b990da192411886c70b83f5e06163ac")
    version("2026-09-19", commit="40932d3445d656e7edda9ad705aa37484a73e81b")

    variant(
        "cxxstd",
        default="20",
        values=("20", "23"),
        multi=False,
        description="C++ standard to use",
    )

    def cmake_args(self):
        return [
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value),
            self.define("CMAKE_CXX_STANDARD_REQUIRED", True),
        ]
