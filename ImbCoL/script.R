# testing ImbCoL library

# downloading imbcol
if (!require("devtools")) {
  install.packages("devtools")
}
devtools::install_github("victorhb/ImbCoL")
library("ImbCoL")

# flower species dataset

ImbCoL::complexity(Species ~ ., iris)
ImbCoL::overlapping(Species ~ ., iris)

#read xls
install.packages("readxl")
library(readxl)
dataset = read_excel('datasets/intersectional-bias3.xlsx')
dataset <- dataset[, -Race]

ImbCoL::complexity(Race ~ ., dataset)
