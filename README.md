# space-wargame-timing
Designed to automate controller processes for Det 340's space wargame

# Dependencies:
None, just Python 3.x. I tested this script with Python 3.13.

# Instructions:
To make adjustments to team names modify the strings within the teams tuple located at the top of the script.
To make adjustments to interval times (in seconds) modify the global variables:
  1. LAUNCH_INTERVAL = the time between launch windows opening (currently set to 2 minutes)
  2. WINDOW_SECONDS = the time that a launch window will last for a given team (currently set to 10 seconds)
  3. ORBIT_INTERVAL = the time for when the satellites in polar orbit must rotate (currently set to 5 minutes)

# Features:
  1. Live countdown
  2. Timestamps for events
  3. Notice of upcoming events
  4. Alternates between team 1 and team 2 for who has the first launch during the launch window phase
