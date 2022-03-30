#make this example reproducible
set.seed(1)

#define data
x1 = rnorm(1000, mean=1123.15)
x2 = rnorm(1000, mean=5699.54)

#plot two histograms in same graph
hist(x1, model_data_2022_03_24_19_02_50_530124$AverageClusterSize[model_data_2022_03_24_19_02_50_530124$sprinklerDensity], xlim=c(1120,5720), breaks=1, main="Histogram for Average Cluster Size", xlab="Average Cluster Size", col=rgb(0,0,1,0.2))
hist(x2, model_data_2022_03_24_19_02_50_530124$AverageClusterSize[model_data_2022_03_24_19_02_50_530124$sprinklerDensity==0.8], breaks=1, col=rgb(1,0,0,0.2), add=TRUE)

#add legend
legend('topright', c('sprinklerDensity 0.2', 'sprinklerDensity 0.8'), fill=c(rgb(0,0,1,0.2), rgb(1,0,0,0.2)))
