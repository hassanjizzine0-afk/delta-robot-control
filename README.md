# delta-robot-control
5-DOF parallel robot control system - BMSTU course project





## 🎯 GENERAL ALGORITHM OF MY SYSTEM

```
┌─────────────────────────────────────────────────────────────────────┐
│                      COMPLETE SYSTEM ALGORITHM                       │
└─────────────────────────────────────────────────────────────────────┘

STEP 1: USER INPUT (Python GUI)
├── User enters: Number of points (N = 3)
├── User enters for EACH point:
│   ├── Point 1: X1, Y1, Z1, Alpha1, Beta1, Gamma1
│   ├── Point 2: X2, Y2, Z2, Alpha2, Beta2, Gamma2
│   └── Point 3: X3, Y3, Z3, Alpha3, Beta3, Gamma3
└── Click "Save" → Creates trajectory_points.txt

                    ↓

STEP 2: MATLAB READS DATA
├── Open trajectory_points.txt
├── Read all N points
├── For EACH point, calculate:
│   ├── Inverse Kinematics (X,Y,Z,Alpha,Beta,Gamma → Joint angles Q1-Q6)
│   ├── Dynamics (forces and torques needed)
│   ├── Velocities and accelerations
│   └── Check for singularities (special positions)
└── Save results → trajectory_calculated.mat

                    ↓

STEP 3: MATLAB GENERATES TRAJECTORY
├── For EACH point, create smooth path between points
├── Calculate intermediate positions (interpolation)
├── Generate time array for entire movement
└── Save → full_trajectory.json

                    ↓

STEP 4: PYTHON READS RESULTS
├── Load full_trajectory.json
├── Prepare commands for Arduino
└── Send via USB Serial

                    ↓

STEP 5: ARDUINO EXECUTES
├── Receive commands one by one
├── Convert commands to PWM signals
├── Control motors
├── Read encoders (feedback)
├── Adjust in real-time
└── Move the mechanism to desired positions

                    ↓

STEP 6: COMPLETE
└── Mechanism moves through ALL N points in sequence
```

---

## 📝 DETAILED EXAMPLE WITH NUMBERS

Let's say we want the mechanism to visit 3 points:

**INPUT (Your GUI):**

```
Number of points: 3

Point 1: X=10, Y=10, Z=5,  Alpha=0, Beta=0,  Gamma=0
Point 2: X=20, Y=15, Z=8,  Alpha=10, Beta=5,  Gamma=0
Point 3: X=30, Y=20, Z=10, Alpha=20, Beta=10, Gamma=0

Time per segment: 2 seconds
Total time: 4 seconds (Point1→Point2: 2s, Point2→Point3: 2s)
```

**MATLAB CALCULATIONS:**

```matlab
% For Point 1 (X=10,Y=10,Z=5)
→ Inverse Kinematics calculates:
   Q1 = 15°, Q2 = 25°, Q3 = 30°, Q4 = 10°, Q5 = 5°, Q6 = 0°

% For Point 2 (X=20,Y=15,Z=8, Alpha=10)
→ Inverse Kinematics calculates:
   Q1 = 30°, Q2 = 40°, Q3 = 45°, Q4 = 20°, Q5 = 15°, Q6 = 5°

% For Point 3 (X=30,Y=20,Z=10, Alpha=20)
→ Inverse Kinematics calculates:
   Q1 = 45°, Q2 = 55°, Q3 = 60°, Q4 = 30°, Q5 = 25°, Q6 = 10°

% Create smooth trajectory between points:
Time: 0s → Q = [15,25,30,10,5,0]    (Point 1)
Time: 1s → Q = [22,32,37,15,10,2]   (intermediate)
Time: 2s → Q = [30,40,45,20,15,5]   (Point 2)
Time: 3s → Q = [37,47,52,25,20,7]   (intermediate)
Time: 4s → Q = [45,55,60,30,25,10]  (Point 3)
```

**OUTPUT TO ARDUINO:**

```
Command 1: 15,25,30,10,5,0,0
Command 2: 22,32,37,15,10,2,1
Command 3: 30,40,45,20,15,5,2
Command 4: 37,47,52,25,20,7,3
Command 5: 45,55,60,30,25,10,4
```

---

## 🔄 FLOWCHART OF ALGORITHM

```
                    ┌─────────────────┐
                    │   START         │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ User inputs N   │
                    │ (number of      │
                    │  points)        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ For i = 1 to N  │
                    │ User inputs     │
                    │ Xi, Yi, Zi,     │
                    │ αi, βi, γi      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Save to file    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ MATLAB reads    │
                    │ all N points    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ For i = 1 to N  │
                    │ Calculate IK    │
                    │ (XYZαβγ → Q1..Q6)│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Create smooth   │
                    │ trajectory      │
                    │ between points  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Check for       │
                    │ singularities   │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
            ┌───────────┐      ┌───────────┐
            │ OK        │      │ Singularity│
            │ Continue  │      │ Adjust    │
            └─────┬─────┘      │ trajectory│
                  │            └─────┬─────┘
                  └──────────┬───────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Generate time   │
                    │ array and       │
                    │ commands        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Send to Arduino │
                    │ via Serial      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Arduino moves   │
                    │ through ALL     │
                    │ N points        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ END             │
                    └─────────────────┘
```
```

