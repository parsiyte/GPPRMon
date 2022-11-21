Detailed documentation on what GPGPU-Sim models, how to configure it, and a
guide to the source code can be found here: <http://gpgpu-sim.org/manual/>.
Instructions for building doxygen source code documentation are included below.
Detailed documentation on GPUWattch including how to configure it and a guide
to the source code can be found here: <http://gpgpu-sim.org/gpuwattch/>.

**GPGPU-Sim dependencies:** gcc, g++, make, makedepend, xutils, bison, flex, zlib ,CUDA Toolkit
..$sudo apt-get install build-essential xutils-dev bison zlib1g-dev flex libglu1-mesa-dev

**GPGPU-Sim documentation dependencies:** doxygen, graphvi
..$sudo apt-get install doxygen graphviz

**AerialVision dependencies:** python-pmw, python-ply, python-numpy, libpng12-dev, python-matplotlib
..$sudo apt-get install python-pmw python-ply python-numpy libpng12-dev python-matplotlib

**CUDA SDK dependencies:** $sudo apt-get install libxi-dev libxmu-dev libglut3-dev

$source setup_environment <build_type> 
 - For debugging, build_type -> debug
 - For normal release -> you dont need to specify build_type, blank as empty.

$make -> for the build of the simulator
$make clean -> To clean the build, run

**IMPORTANT**

To build the doxygen generated documentations, run

	make docs

To clean the docs run

	make cleandocs

These doxygen generated documentation will help you to understand classes, templates, functions etc.
