# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Extends the builtin recipe only to add Geant4 11.5.0.beta, which Code4hep needs.
from spack_repo.builtin.packages.geant4.package import Geant4 as BuiltinGeant4

from spack.package import *


class Geant4(BuiltinGeant4):
    git = "https://github.com/Geant4/geant4.git"

    version("11.5.0.beta", tag="v11.5.0.beta")
