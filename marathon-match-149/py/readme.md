Challenge Overview

Important Links
Submission-Review You can find your submissions artifacts here. Artifacts will contain output.txt's for both example test cases and provisional test cases with stdout/stderr and individual test case scores.
Other Details For other details like Processing Server Specifications, Submission Queue, Example Test Cases Execution.
Overview
You are tasked with designing an irrigation system for a gridded garden of size N by N. The garden contains plants that need to be irrigated. Luckily a few water points are available which can be used to connect pipes and sprinklers to the irrigation system. Your design needs to provide water to as many of the plants as possible while minimising the total cost of the irrigation system.

The garden contains S water source cells where pipes can be connected. These pipes can only be placed in horizontal and vertical directions. Each cell containing a pipe incurs a cost of P. Connectors are automatically placed by the tester application wherever pipes intersect, whenever a pipe changes direction, and where pipes stop. Connecting a pipe at a water source does not use any connectors. The cost of a connector is calculated as (C * X), where C represents the base cost of a connector and X is the number of pipes attached to the connector.

Sprinklers can be placed on top of any cell that contains a pipe, at a cost of T. Additionally, each sprinkler covers a radius of Z cells, where the cells that satisfy (dx * dx + dy * dy <= Z * Z) become irrigated by the sprinkler when water flows through it. dx and dy are the distances from the sprinkler to the plant in the horizontal and vertical directions, respectively. Any plant that was not irrigated will cost you a penalty of N * N.

Here is an example solution for seed=1. The water flow is opened after all your commands have been processed. Plants are drawn in green when they are irrigated and red when not. Black pipes indicate no water flow while pipes turn blue when the water flows through them. The cyan circles show the sprinkler placements. Water sprayed by the sprinklers can be seen in blue. The color intensity of the connectors indicates their cost. Water sources are shown as blue circles within black cells.

Seed1 example

Input and Output
Your code will receive as input the following values, each on a separate line:

N, the size of the grid.
C, the connector cost.
P, the pipe cost.
T, the sprinkler cost.
Z, the sprinkler radius.
N*N lines representing the grid in row-major order. Each cell is either empty (0), a water source (1) or a plant (2).
Your code needs to output the following:

The number of commands K.
K lines each containing a command that will build your irrigation system, you have the following two options:
Formatted as "P r1 c1 r2 c2" (without the quotes), where r1, c1, r2 and c2 are 0-based row and column coordinates, respectively. This will place a pipe between (r1, c1) and (r2, c2). Only horizontal or vertical pipes are allowed (r1==r2 or c1==c2).
Formatted as "S r c" (without the quotes), where r and c are 0-based row and column coordinates, respectively. This will place a sprinkler at cell (r, c).
Scoring
The raw score is the cost of all the pipes, sprinklers and connectors placed plus the penalty for each plant not irrigated. If your return was invalid, then your raw score on this test case will be -1. Possible reasons include:

Placing a pipe on top of a plant or an already placed pipe.
Placing a sprinkler on top of a water source, plant or sprinkler.
Placing a sprinkler not on top of a pipe.
Placing a pipe or a sprinkler outside of the grid.
Exceeding the time limit.
If your raw score for a test case is negative then your normalized score for that test case is 0. Otherwise, your normalized score for each test case is MIN/YOUR, where YOUR is your raw score and MIN is the smallest positive raw score currently obtained on this test case (considering only the last submission from each competitor). Finally, the sum of all your test scores is normalized to 100.

Test Case Generation
Please look at the generate() method in the visualizer's source code for the exact details about test case generation. Each test case is generated as follows:

The size of the grid N is chosen between 8 and 50, inclusive.
The number of water sources S is chosen between 1 and 5, inclusive.
The cost of a connector C is chosen between 1 and 30, inclusive.
The cost of a pipe P is chosen between 1 and 30, inclusive.
The cost of a sprinkler T is chosen between 30 and 90, inclusive.
The radius of a sprinkler Z is chosen between 1 and 4, inclusive.
The plant density factor D is chosen between 0.05 and 0.3, inclusive.
Plants that can not be reached by a water pipe with a sprinker are removed from the grid by the makeValid() method.

Notes
The time limit is 10 seconds per test case (this includes only the time spent in your code). The memory limit is 1024 megabytes.
The compilation time limit is 30 seconds.
There are 10 example test cases and 100 full submission (provisional) test cases. There will be 2000 test cases in the final testing.

The match is rated.
Languages Supported
C#, Java, C++ and Python

Submission Format
Your submission must be a single ZIP file not larger than 500 MB, with your source code only.
Please Note: Please zip only the file. Do not put it inside a folder before zipping, you should directly zip the file.

Make sure you name your Source Code file as Irrigation*. <appropriate extension>*

SAMPLE SUBMISSIONS
Here are example solutions for different languages, modified to be executed with the visualizer. You may modify and submit these example solutions:

Java Source Code - Irrigation.java.zip
C++ Source Code - Irrigation.cpp.zip
Python3.6 Source Code - Irrigation.py.zip
C# Source Code - Irrigation.cs.zip
Tools
An offline tester is available below. You can use it to test/debug your solution locally. You can also check its source code for an exact implementation of test case generation and score calculation. You can also find links to useful information and sample solutions in several languages.

Downloads
Visualizer Source - IrrigationTester.zip
Visualizer Binary - tester.jar.zip
Offline Tester / Visualizer
Your solution should interact with the tester/visualizer by reading data from standard input and writing data to standard output.

To run the tester with your solution, you should run:

java -jar tester.jar -exec "<command>" -seed <seed>

Here, <command> is the command to execute your program, and <seed> is seed for test case generation.
If your compiled solution is an executable file, the command will be the full path to it, for example, "C:\TopCoder\Irrigation.exe" or "~/topcoder/Irrigation".
In case your compiled solution is to be run with the help of an interpreter, for example, if your program is in Java, the command will be something like "java -cp C:\TopCoder Irrigation".

Additionally you can use the following options:

-seed <seed> Sets the seed used for test case generation, default is seed 1.
-debug. Print debug information.
-novis. Turns off visualisation.
-pause. Starts the visualizer in paused mode. See more information below.
-delay <delay> Sets the delay (in milliseconds) between visualizing consecutive simulation steps, default is 1500.
-N <N> Sets a custom grid size.
-S <S> Sets a custom number of water sources.
-P <P> Sets a custom pipe cost.
-C <C> Sets a custom connector cost.
-T <T> Sets a custom sprinkler cost.
-Z <Z> Sets a custom sprinkler range.
-D <D> Sets a custom plant density factor.
-showAllSteps Visualize every command one by one.
The visualizer works in two modes. In regular mode, steps are visualized one after another with a delay specified with the -delay parameter. In paused mode, the next move will be visualized only when you press any key. The space key can be used to switch between regular and paused modes. The default starting mode is regular. You can use the -pause parameter to start in paused mode.

Marathon local testers have many useful options, including running a range of seeds with a single command, running more than one seed at time (multiple threads), controlling time limit, saving input/output/error and loading solution from a file. The usage of these options are described here.

public static final String controlBests = "bests";
public static final String debug = "debug";
public static final String delay = "delay";
public static final String exec = "exec";
public static final String infoScale = "infoScale";
public static final String loadSolOutput = "loadSolOutput";
public static final String noAntialiasing = "noAntialiasing";
public static final String noOutput = "noOutput";
public static final String noReplay = "noReplay";
public static final String noSummary = "noSummary";
public static final String noVis = "novis";
public static final String paintInfo = "paintInfo";
public static final String printRuntime = "printRuntime";
public static final String saveAll = "saveAll";
public static final String saveScores = "saveScores";
public static final String saveSolError = "saveSolError";
public static final String saveSolInput = "saveSolInput";
public static final String saveSolOutput = "saveSolOutput";
public static final String saveVis = "saveVis";
public static final String screen = "screen";
public static final String seed = "seed";
public static final String size = "size";
public static final String startPaused = "pause";
public static final String windowPosition = "windowPos";
public static final String threads = "threads";
public static final String timeLimit = "timeLimit"