#Installing packages #'d as per cwk instructions
#install.packages("dplyr")
#loading packages
library(dplyr)
library(ggplot2)
#1
#Ensure the data is in the CWD
getwd()
#Importing in the data
data <- read.csv("pumpkins_2.csv")

#2
data %>% #Piping the dataset into the following functions
  arrange(-weight_lbs) %>% #Sorting the rows in order of mass, greatest first
  select(variety, city, state_prov, id, weight_lbs) %>% #Selecting columns 
  head(1) #Showing the Top 1 pumpkin for mass
  #write.csv("output.docx") #Writing output to output file

#3
data$weight_kg <- NA #Creating new kgs column
lbs_to_kg <- function() {
  return(data$weight_lbs / 2.20462262)
} #Creating conversion function
data$weight_kg <- lbs_to_kg() # Applying function, populating new column

#4
data$weight_class <- NA #Creating new weight class column

for (i in 1:nrow(data)) {
  if (data$weight_kg[i] > 500) {
    data$weight_class[i] <- 'heavy'
  } else if (data$weight_kg[i] < 100) {
    data$weight_class[i] <- 'light'
  } else {
    data$weight_class[i] <- 'medium'
  }
} #Weights > 500 = heavy, weights 100-500 = medium, weights <100 = light
data$weight_class <- factor(data$weight_class) #Making vector a factor for q5 colour
  
#5
#Creating new df with outliers removed
q5data <- filter(data, (ott > 20 & est_weight > 0 & weight_lbs > 0 
                        & est_weight < 9000))
#Creating scatter graph
weightplot <- ggplot(q5data, aes(est_weight, weight_lbs, colour = weight_class)) + 
  geom_point() +
    xlab('Estimated Weight (lbs)') +
    ylab('Actual Weight (lbs)') +
    ggtitle('Estimated vs Actual Weight of Pumpkins')
#Saving as jpg
jpeg("q5_weight_graph.jpg", units = "cm", width = 20, height = 10, res = 300)
weightplot
dev.off()

#6
#Creating new df with only 3 countries, using dataset with outliers removed
q6data <- filter(q5data, country == "USA" | country == "Australia" | country == "China")
#Writing new df to a csv file
write.csv(q6data, "pumpkins_filtered.csv", row.names = F)

#7a
#Summarising mean weight by grouped country
q6data %>%
  group_by(country) %>%
  summarise(mean_weight = mean(weight_lbs, na.rm = T)) %>%
  arrange(-mean_weight)  #Ordering by descending weight

#7b
q6data %>%
  group_by(country, variety) %>%
  summarise(mean_weight = mean(weight_lbs, na.rm = T)) %>%
  arrange(mean_weight) #Ordering by ascending weight

#8
q8plot <- ggplot(q6data, aes(country, weight_lbs)) +
  geom_boxplot() +
  xlab("Country") +
  ylab("Weight (lbs)") +
  ggtitle("Weight Distribution by Country")

#Saving as jpg
jpeg("q8_weight_graph.jpg", units = "cm", width = 20, height = 10, res = 300)
q8plot
dev.off()

#9
q9plot <- ggplot(q6data, aes(country, weight_lbs)) +
  geom_boxplot() +
  facet_wrap(~variety) +
  xlab("Country") +
  ylab("Weight (lbs)") +
  ggtitle("Weight Distribution by Country and Variety")

#Saving as jpg
jpeg("q9_weight_graph.jpg", units = "cm", width = 20, height = 10, res = 300)
q9plot
dev.off()
