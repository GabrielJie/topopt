#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from topopt.boundary_conditions import LBracketBoundaryConditions
from topopt.guis import StressGUI, GUI
from topopt.problems import VonMisesStressProblem
import topopt.filters
from topopt.solvers import TopOptSolver
from topopt import cmd_helper

if __name__ == "__main__":
    def run():
        # Default input parameters
        nelx, nely, volfrac, penal, rmin, ft = cmd_helper.parse_sys_args(
                nelx=120, nely=120, volfrac=0.3, penal=12, rmin=1.2)
        bc = LBracketBoundaryConditions(
            nelx, nely, 2 * nelx // 5, 3 * nelx // 5)
        problem = VonMisesStressProblem(nelx, nely, penal, bc)
        gui = StressGUI(problem, title="Stress on L Bracket")
        filter = [topopt.filters.SensitivityBasedFilter,
                  topopt.filters.DensityBasedFilter][ft](nelx, nely, rmin)
        solver = TopOptSolver(
            problem, volfrac, filter, gui, maxeval=4000, ftol=1e-5)
        topopt.cmd_helper.main(
            nelx, nely, volfrac, penal, rmin, ft, solver=solver)
    run()