from os import sep

file = open("Experimento-forest_fire_vs_sprinklers"+sep+"agent_data_iter_300_forest_size_100_tree_density_0.65_sprinkler_density_manipulated_steps_til_estabilize_system_2022-03-24 19-02-50.530124.csv")
data = open("agent_data_iter_300_forest_size_100_tree_density_0.65_sprinkler_density_manipulated_steps_til_estabilize_system_2022-03-24 19-02-50.530124.csv","w")

line = file.readline()
data.write(line.replace("AgentId,Condition", "Fine,Protected,Burned Out,On Fire"))

# ,sprinkler_density,Run,AgentId,Condition,forest_size,tree_density

steps = 0
sprinkler = 0
run = "0"
fine = 0
protected = 0
burn = 0
fire = 0
fsize = 0
tree = 0

prevrun = run
cm = ","
linenumber = 1
# print(linenumber)

line = file.readline()
cols = line.split(",")

while line != "happyending\n":
    steps = cols[2]
    run = cols[2]
    sprinkler = cols[1]
    fsize = cols[6]
    tree = cols[7]

    if cols[5] == "Fine":
        fine += 1
    elif cols[5] == "Protected" or cols[5] == "Sprinkler":
        protected += 1
    elif cols[5] == "Burned Out":
        burn += 1
    else:
        fire += 1

    if prevrun != run:
        print(run)
        data.write(steps+cm+ sprinkler+cm+ prevrun+cm+ str(fine)+cm+ str(protected)+cm+ str(burn)+cm+ str(fire)+cm+ fsize+cm+ tree)

        fine = 0
        protected = 0
        burn = 0
        fire = 0

    prevrun = run
    linenumber += 1
    # print(linenumber)

    line = file.readline()
    cols = line.split(",")
data.write(steps+cm+ sprinkler+cm+ prevrun+cm+ str(fine)+cm+ str(protected)+cm+ str(burn)+cm+ str(fire)+cm+ fsize+cm+ tree)
