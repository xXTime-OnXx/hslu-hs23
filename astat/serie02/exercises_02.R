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
var_winner <- (winner - )