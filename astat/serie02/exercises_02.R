# Aufgabe 2.1
winner <- c(183, 191, 185, 185, 182, 182, 188, 188, 188, 185, 185, 177,
            182, 182, 193, 183, 179, 179, 175)
opponent <- c(191, 165, 187, 175, 193, 185, 187, 188, 173, 180, 177, 183,
              185, 180, 180, 182, 178, 178, 173)

# a
length(winner)
length(opponent)

# b
winner[6:10]

# c
winner[c(3, 5, 10:12)]

# d
winner[c(7, 8)] <- 189
winner

# e
mean(winner)
mean(opponent)

# f
mean(winner - opponent)

# g
var(winner)
sd(winner)

# h
winner.var <- sum((winner - mean(winner))^2) / (length(winner)-1)
winner.sd <- sqrt(winner.var)

# Aufgabe 2.2
noten <- c(4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1)

# a
noten_2 <- c(1,2.3,5.6,4.5,4.8,3.9,5.9,2.4,5.9,6,4,3.7,5,5.2,1,3.6,5,6,
             2.8,3.3,5.5,1,4.9,5.1)

# b
boxplot(noten, noten_2,
        col = c("orange", "lightblue"))

# Aufgabe 2.3
# a
mannfrau <- read.csv("serie02/mannfrau.csv")
head(mannfrau)

# b
diff_alter <- mannfrau$alter.mann - mannfrau$alter.frau

boxplot(diff_alter,
        main="Altersdifferenz Ehemaenner & Ehefrauen",
        col="orange")

# Aufgabe 2.4
# a
tapply(InsectSprays[, "count"], InsectSprays[, "spray"], FUN = mean)

# b
tapply(InsectSprays$count, InsectSprays$spray, mean)

# c
boxplot(count ~ spray,
        data = InsectSprays,
        col=c("orange", "blue", "darkseagreen", "deeppink",
              "brown", "aquamarine")
)

# Aufgabe 2.5
diet <- read.csv("serie02/Diet.csv")
head(diet)

diet$weight.loss <- diet$weight6weeks - diet$pre.weight
head(diet)

# a
tapply(diet[, "weight.loss"], diet[, "Diet"], FUN = mean)

# b
tapply(diet$weight.loss, diet$Diet, mean)

# c
boxplot(weight.loss ~ Diet,
        data = diet,
        col=c("orange", "darkseagreen", "aquamarine"))
