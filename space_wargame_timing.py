import time

print("Starting wargame...")

teams = ("Polaris", "Orion") # You may change the team names at will

# Intervals are in seconds
LAUNCH_INTERVAL = 120 # 2 minutes
WINDOW_SECONDS = 10   # 10 seconds
ORBIT_INTERVAL = 300  # 5 minutes

def ts():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def clear():
    print("\r" + " " * 120 + "\r", end="", flush=True)

def schedule_next_orbit(start, now):
    cycles = int((now - start) / ORBIT_INTERVAL) + 1
    return start + cycles * ORBIT_INTERVAL

def countdown_window(team, seconds):
    global next_orbit_call

    end = time.time() + seconds
    last = None

    while True:
        now = time.time()

        # orbit broadcast check
        if now >= next_orbit_call:
            clear()
            print(f"[{ts()}] BROADCAST: ROTATE POLAR ORBIT")
            next_orbit_call = schedule_next_orbit(start_time, now)

        remaining = int(end - now + 0.999)

        if remaining <= 0:
            clear()
            print(f"[{ts()}] {team} window: 00")
            return

        if remaining != last:
            print(f"\r[{ts()}] {team} window: {remaining:02d}s", end="", flush=True)
            last = remaining

        time.sleep(0.05)


start_time = time.time()
next_launch_cycle = start_time + LAUNCH_INTERVAL
next_orbit_call = start_time + ORBIT_INTERVAL

first_team_index = 0
last_render = 0

while True:
    now = time.time()

    # orbit check
    if now >= next_orbit_call:
        clear()
        print(f"[{ts()}] BROADCAST: ROTATE POLAR ORBIT")
        next_orbit_call = schedule_next_orbit(start_time, now)

    # launch cycle
    if now >= next_launch_cycle:
        clear()
        print(f"[{ts()}] Launch window has opened.")

        if first_team_index == 0:
            first, second = teams[0], teams[1]
        else:
            first, second = teams[1], teams[0]

        print(f"[{ts()}] Launch window has opened for {first}")
        countdown_window(first, WINDOW_SECONDS)

        print(f"[{ts()}] Launch window has opened for {second}")
        countdown_window(second, WINDOW_SECONDS)

        first_team_index = 1 - first_team_index
        next_launch_cycle = time.time() + LAUNCH_INTERVAL

    # status line
    if now - last_render > 0.25:
        next_event = min(next_launch_cycle, next_orbit_call)
        name = "LAUNCH WINDOW" if next_event == next_launch_cycle else "ORBIT BROADCAST"
        remaining = int(next_event - now)

        mins = remaining // 60
        secs = remaining % 60

        print(f"\r[{ts()}] Next: {name} in {mins:02d}:{secs:02d}".ljust(120), end="")
        last_render = now

    time.sleep(0.05)