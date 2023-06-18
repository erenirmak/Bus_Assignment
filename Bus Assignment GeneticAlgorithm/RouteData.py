
# Define matrices
# Define the time matrix of bus stops (in mins)
time_matrix = [
    [0, 36, 54, 18, 36, 54, 63, 99, 90],
    [36, 0, 27, 45, 63, 72, 63, 72, 54],
    [54, 27, 0, 45, 54, 63, 54, 45, 36],
    [18, 45, 45, 0, 18, 36, 54, 90, 90],
    [36, 63, 54, 18, 0, 18, 45, 81, 72],
    [54, 72, 63, 36, 18, 0, 36, 72, 90],
    [63, 63, 54, 54, 45, 36, 0, 36, 63],
    [99, 72, 45, 90, 81, 72, 36, 0, 36],
    [90, 54, 36, 90, 72, 90, 63, 36, 0]
    ]

# Define the cost matrix with passengers (in TL)
cost_with_passengers = [
    [0, 45, 70, 25, 45, 70, 80, 125, 115],
    [45, 0, 35, 55, 80, 90, 80, 90, 70],
    [70, 35, 0, 55, 70, 80, 70, 55, 45],
    [25, 55, 55, 0, 25, 45, 70, 115, 115],
    [45, 80, 70, 25, 0, 25, 55, 100, 90],
    [70, 90, 80, 45, 25, 0, 45, 90, 115],
    [80, 80, 70, 70, 55, 45, 0, 45, 80],
    [125, 90, 55, 115, 100, 90, 45, 0, 45],
    [115, 70, 45, 115, 90, 115, 80, 45, 0]
    ]

# Define the cost matrix without passengers (in TL)
cost_without_passengers = [
    [0, 108, 168, 60, 108, 168, 192, 300, 276],
    [108, 0, 84, 132, 192, 216, 192, 216, 168],
    [168, 84, 0, 132, 168, 192, 168, 132, 108],
    [60, 132, 132, 0, 60, 108, 168, 276, 276],
    [108, 192, 168, 60, 0, 60, 132, 240, 216],
    [168, 216, 192, 108, 60, 0, 108, 216, 276],
    [192, 192, 168, 168, 132, 108, 0, 108, 192],
    [300, 216, 132, 276, 240, 216, 108, 0, 108],
    [276, 168, 108, 276, 216, 276, 192, 108, 0]
    ]

# Trip class
class Sefer:
    def __init__(self, start_loc, end_loc, start_time):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.trip_start_time = start_time
        self.trip_duration_time = self.time_spent()
        self.trip_complete_time = self.trip_end_time()
        self.cost_full = self.trip_cost_with_passenger()
        self.cost_empty = self.trip_cost_without_passenger()
        self.cost_wait_per_min = 5

    def time_spent(self):
        return time_matrix[self.start_loc][self.end_loc]

    def trip_cost_with_passenger(self):
        return cost_with_passengers[self.start_loc][self.end_loc]

    def trip_cost_without_passenger(self):
        return cost_without_passengers[self.start_loc][self.end_loc]

    def trip_end_time(self):
        spent = self.time_spent()
        return self.trip_start_time + spent

# pre-defined trip routes
seferler = {"sefer1" : Sefer(0, 1, 30),
            "sefer2" : Sefer(0, 1, 60),
            "sefer3" : Sefer(0, 2, 20),
            "sefer4" : Sefer(2, 3, 75),
            "sefer5" : Sefer(1, 4, 110),
            "sefer6" : Sefer(1, 2, 80),
            "sefer7" : Sefer(2, 0, 40),
            "sefer8" : Sefer(1, 0, 30),
            "sefer9" : Sefer(2, 0, 20),
            "sefer10" : Sefer(3, 2, 70),
            "sefer11" : Sefer(3, 2, 90),
            "sefer12" : Sefer(4, 5, 20),
            "sefer13" : Sefer(2, 6, 40),
            "sefer14" : Sefer(5, 6, 45),
            "sefer15" : Sefer(5, 2, 40),
            "sefer16" : Sefer(5, 8, 50),
            "sefer17" : Sefer(5, 0, 55),
            "sefer18" : Sefer(6, 1, 75),
            "sefer19" : Sefer(7, 1, 95),
            "sefer20" : Sefer(6, 3, 100),
            "sefer21" : Sefer(8, 3, 120),
            "sefer22" : Sefer(5, 3, 110),
            "sefer23" : Sefer(8, 3, 125),
            "sefer24" : Sefer(1, 2, 125),
            "sefer25" : Sefer(0, 5, 130),
            "sefer26" : Sefer(2, 4, 150),
            "sefer27" : Sefer(3, 4, 160),
            "sefer28" : Sefer(4, 3, 160),
            "sefer29" : Sefer(5, 3, 180),
            "sefer30" : Sefer(6, 1, 190),
            "sefer31" : Sefer(6, 8, 190),
            "sefer32" : Sefer(7, 8, 210),
            "sefer33" : Sefer(7, 8, 220),
            "sefer34" : Sefer(8, 5, 240),
            "sefer35" : Sefer(0, 1, 240),
            "sefer36" : Sefer(0, 2, 250),
            "sefer37" : Sefer(0, 2, 260),
            "sefer38" : Sefer(2, 3, 300),
            "sefer39" : Sefer(1, 4, 330),
            "sefer40" : Sefer(1, 2, 115),
            "sefer41" : Sefer(2, 0, 140),
            "sefer42" : Sefer(1, 0, 150),
            "sefer43" : Sefer(2, 0, 130),
            "sefer44" : Sefer(3, 2, 140),
            "sefer45" : Sefer(3, 2, 180),
            "sefer46" : Sefer(4, 5, 200),
            "sefer47" : Sefer(2, 6, 230),
            "sefer48" : Sefer(5, 6, 220),
            "sefer49" : Sefer(5, 2, 210),
            "sefer50" : Sefer(5, 8, 180),
            "sefer51" : Sefer(5, 0, 185),
            "sefer52" : Sefer(6, 1, 195),
            "sefer53" : Sefer(7, 1, 205),
            "sefer54" : Sefer(6, 3, 225),
            "sefer55" : Sefer(8, 3, 255),
            "sefer56" : Sefer(5, 3, 300),
            "sefer57" : Sefer(8, 3, 330),
            "sefer58" : Sefer(1, 2, 290),
            "sefer59" : Sefer(0, 5, 280),
            "sefer60" : Sefer(2, 4, 350),
            "sefer61" : Sefer(3, 4, 380),
            "sefer62" : Sefer(4, 3, 390),
            "sefer63" : Sefer(5, 3, 410),
            "sefer64" : Sefer(6, 1, 420),
            "sefer65" : Sefer(6, 8, 395),
            "sefer66" : Sefer(7, 8, 380),
            "sefer67" : Sefer(7, 8, 440),
            "sefer68" : Sefer(8, 5, 440),
            "sefer69" : Sefer(0, 1, 450),
            "sefer70" : Sefer(0, 2, 480),
            "sefer71" : Sefer(0, 2, 490),
            "sefer72" : Sefer(2, 3, 500),
            "sefer73" : Sefer(1, 4, 500),
            "sefer74" : Sefer(1, 2, 475),
            "sefer75" : Sefer(2, 0, 485),
            "sefer76" : Sefer(1, 0, 535),
            "sefer77" : Sefer(2, 0, 525),
            "sefer78" : Sefer(3, 2, 510),
            "sefer79" : Sefer(3, 2, 520),
            "sefer80" : Sefer(4, 5, 520),
            "sefer81" : Sefer(2, 6, 550),
            "sefer82" : Sefer(5, 6, 550),
            "sefer83" : Sefer(5, 2, 580),
            "sefer84" : Sefer(5, 8, 600),
            "sefer85" : Sefer(5, 0, 610),
            "sefer86" : Sefer(6, 1, 630),
            "sefer87" : Sefer(7, 1, 630),
            "sefer88" : Sefer(6, 3, 640),
            "sefer89" : Sefer(8, 3, 640),
            "sefer90" : Sefer(5, 3, 650),
            "sefer91" : Sefer(8, 3, 660),
            "sefer92" : Sefer(1, 2, 680),
            "sefer93" : Sefer(0, 5, 670),
            "sefer94" : Sefer(2, 4, 700),
            "sefer95" : Sefer(3, 4, 690),
            "sefer96" : Sefer(4, 3, 690),
            "sefer97" : Sefer(5, 3, 690),
            "sefer98" : Sefer(6, 1, 700),
            "sefer99" : Sefer(6, 8, 710),
            "sefer100" : Sefer(7, 8, 730)}

# Define some constants
NUM_BUSES = 10 # Number of busses
NUM_TRIPS = 100 # Number of trip routes
POP_SIZE = 100 # Population size for genetic algorithm
GENS = 1000 # Number of generations for genetic algorithm
CROSS_RATE = 0.8 # Crossover rate for genetic algorithm
MUT_RATE = 0.1 # Mutation rate for genetic algorithm
ELITE_RATE = 0.1 # Elitism rate for genetic algorithm
MAX_TIME = 480 # Maximum travel time for each bus in minutes
PENALTY = 100000 # Penalty cost for violating the constraint
WAIT_COST = 5 # Cost for waiting at the same bus stop

# Create a dictionary of trips from the given data
trips = {} # Initialize an empty dictionary for trips
for i in range(NUM_TRIPS):
    trips[i] = {"start_location": seferler[f"sefer{i+1}"].start_loc,
                "end_location": seferler[f"sefer{i+1}"].end_loc,
                "start_time": seferler[f"sefer{i+1}"].trip_start_time,
                "end_time": seferler[f"sefer{i+1}"].trip_complete_time,
                "time_duration": seferler[f"sefer{i+1}"].trip_duration_time,
                "cost_with_passengers": seferler[f"sefer{i+1}"].cost_full,
                "cost_without_passengers": seferler[f"sefer{i+1}"].cost_empty,
                "cost_for_waiting": seferler[f"sefer{i+1}"].cost_wait_per_min}

