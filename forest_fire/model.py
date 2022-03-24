from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import Grid
from mesa.time import RandomActivation
from mesa.batchrunner import BatchRunner

from datetime import datetime
from os import sep

from .agent import TreeCell

import sys
from .sylar_bib import *


class ForestFire(Model):
    """
    Simple Forest Fire model.
    """

    def __init__(self, forest_size=100, tree_density=0.65, sprinkler_density=0.4):
        sys.setrecursionlimit(3900)
        self.gridsize = forest_size
        """
        Create a new forest fire model.
        Args:
            width, height: The size of the grid to model
            density: What fraction of grid cells have a tree in them.
        """
        # Set up model objects
        self.schedule = RandomActivation(self)
        self.grid = Grid(forest_size, forest_size, torus=False)

        self.tree_density = tree_density
        self.sprinkler_density = sprinkler_density
        self.fman_density = sprinkler_density * 0.025

        self.datacollector = DataCollector(
            {
                "Fine": lambda m: self.count_type(m, "Fine") + self.count_type(m, "Fireman"),
                "On Fire": lambda m: self.count_type(m, "On Fire"),
                "Burned Out": lambda m: self.count_type(m, "Burned Out"),
                "Protected": lambda m: self.count_type(m, "Protected"),
                "Clusters": lambda m: self.cluster_count,
                "Average Cluster Size": lambda m: (self.count_type(m, "Fine") + self.count_type(m, "Protected") + self.count_type(m, "Fireman")) / self.cluster_count if self.cluster_count != 0 else 0,
            }
        )

        self.datacollector_model = DataCollector(
            {
                "Forest Density": lambda m: self.tree_density,
                "Sprinkler Density": lambda m: sprinkler_density,
                "Unaffected Vegetation": lambda m: self.count_type(m, "Fine") / (self.count_type(m, "Fine") + self.count_type(m, "Fireman") + self.count_type(m, "Protected") + self.count_type(m, "Burned Out")),
                "Saved Vegetation": lambda m: (self.count_type(m, "Protected") + self.count_type(m, "Fireman")) / (self.count_type(m, "Fine") + self.count_type(m, "Fireman") + self.count_type(m, "Protected") + self.count_type(m, "Burned Out")),
                "Wasted Vegetation": lambda m: self.count_type(m, "Burned Out") / (self.count_type(m, "Fine") + self.count_type(m, "Fireman") + self.count_type(m, "Protected") + self.count_type(m, "Burned Out")),
            }
        )

        self.alltrees = newMatrix(self.gridsize)
        self.cluster_count = 0

        self.st98 = []
        self.st94 = []
        self.st86 = []
        self.st70 = []
        self.st40 = []

        # Place a tree in each cell with Prob = density
        for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < self.fman_density:
                # Create a fireman
                new_fman = TreeCell((x, y), self)
                new_fman.condition = "Fireman"
                new_fman.strength = 0.92
                self.grid._place_agent((x, y), new_fman)
                self.schedule.add(new_fman)
                addStrength(self,x,y)
                self.alltrees[x][y] = new_fman

            elif self.random.random() < tree_density:
                # Create a tree
                new_tree = TreeCell((x, y), self)
                # Set all trees in the first column on fire.
                if x == 0:
                    new_tree.condition = "On Fire"
                elif self.st98.count((x,y)):
                    new_tree.strength = 0.88
                elif self.st94.count((x,y)):
                    new_tree.strength = 0.84
                elif self.st86.count((x,y)):
                    new_tree.strength = 0.76
                elif self.st70.count((x,y)):
                    new_tree.strength = 0.6
                elif self.st40.count((x,y)):
                    new_tree.strength = 0.3

                self.grid._place_agent((x,y), new_tree)
                self.schedule.add(new_tree)
                self.alltrees[x][y] = new_tree
        
        self.count_clusters()

        self.running = True
        self.datacollector.collect(self)


    def count_clusters(self):
        self.minitrees = newMatrix(self.gridsize)
        for x in range(0,self.gridsize):
            for y in range(0,self.gridsize):
                tree = self.alltrees[x][y]
                if (type(tree) == TreeCell) and ((tree.condition == "Fine") or (tree.condition == "Protected") or (tree.condition == "Fireman")):
                    self.minitrees[x][y] = 1
        self.cluster_count = countIslands(self.minitrees)


    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()

        self.count_clusters()
        # collect data
        self.datacollector.collect(self)

        # Halt if no more fire
        if self.count_type(self, "On Fire") == 0:
            self.running = False

            now = str(datetime.now()).replace(":", "-")
            df_agent = self.datacollector.collect(self)
            # df_agent.to_csv("dataframe" + sep + "agent_data tree_density=" + str(self.tree_density) + " fireman_groups=" + str(self.sprinkler_density) + " " + now + ".csv")
            
            self.datacollector_model.collect(self)
            df_model = self.datacollector_model.collect(self)
            # df_model.to_csv("dataframe" + sep + "model_data tree_density=" + str(self.tree_density) + " fireman_groups=" + str(self.sprinkler_density) + " " + now + ".csv")
    

    @staticmethod
    def count_type(model, tree_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for tree in model.schedule.agents:
            if tree.condition == tree_condition:
                count += 1
        return count


def batch_run():
    fixed_params = {
        'forest_size': 100,
        'tree_density': 0.65
    }
    variable_params = {
        'sprinkler_density': [0.0, 0.1, 0.2, 0.4, 0.6, 0.8]
    }
    experiments_per_parameter_configuration = 2
    max_steps_per_simulation = 300

    batch_run = BatchRunner(
        ForestFire,
        variable_params,
        fixed_params,
        iterations=experiments_per_parameter_configuration,
        max_steps=max_steps_per_simulation,
        model_reporters = {
            'Clusters': allclusters,
            'Average Cluster Size': clusterssize
        },
        # agent_reporters = {
        #     "Fine": lambda m: self.count_type(m, "Fine") + self.count_type(m, "Fireman"),
        #     "On Fire": lambda m: self.count_type(m, "On Fire"),
        #     "Burned Out": lambda m: self.count_type(m, "Burned Out"),
        #     "Protected": lambda m: self.count_type(m, "Protected"),
        # }
    )
    batch_run.run_all()

    run_model_data = batch_run.get_model_vars_dataframe()
    # run_agent_data = batch_run.get_agent_vars_dataframe()

    now = str(datetime.now()).replace(':','-')
    file_name_suffix =  ('_iter_'+str(experiments_per_parameter_configuration)+
                        '_steps_'+str(max_steps_per_simulation)+'_'+now)
    run_model_data.to_csv('Experimento-forest_fire_vs_sprinklers'+sep+'model_data'+file_name_suffix+'.csv')
    # run_agent_data.to_csv('agent_data'+file_name_suffix+'.csv')