# 🛰️ Small Body Mission Simulation with KSP + SPICE

This project is a starter template for designing, simulating, and executing a small body mission in Kerbal Space Program, augmented with SPICE-based trajectory planning and GNC logic using `kOS`.

## 🔧 Project Overview
- Mission: Rendezvous with a Bennu-like asteroid
- Tools: KSP + Kopernicus + kOS + Python + SPICE Toolkit
- Objective: Plan and simulate asteroid intercept, autonomous attitude alignment, and surface sample attempt

## 🗂️ Directory Structure
```
project-root/
├── spice/               # SPICE kernels and trajectory planning
├── ksp/                 # KSP craft files, kOS scripts
├── notebooks/           # Python tools for planning and simulation
├── README.md
```

## 🔗 Setup Instructions

### 1. KSP Environment
- Install KSP (v1.12.x recommended)
- Install mods: Kopernicus, kOS, SCANsat, Trajectories, Kerbalism (optional)
- Add asteroid using `ksp/asteroid_config.cfg` and Kopernicus

### 2. Python Environment
```bash
pip install numpy scipy matplotlib spiceypy
```

## 🚀 Suggested Workflow
1. Generate ephemeris using SPICE (`notebooks/spice_ephemeris_planner.ipynb`)
2. Convert orbit to Kopernicus format (`ksp/asteroid_config.cfg`)
3. Design intercept trajectory in KSP
4. Use `kOS` scripts to autonomously align and navigate
5. Record mission attempt and generate report

Happy simulating!
