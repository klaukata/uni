# get 'a' from a user, that != 0
get_a <- function() {
  a <- strtoi(readline("enter a: "))
  if (a == 0) {
    get_a()
  }
  return(a)
}
a <- get_a()

# get 'b' and 'c' from a user
b <- strtoi(readline("enter b: "))
c <- strtoi(readline("enter c: "))

# calculate delta
delta <- b^2 - 4 * a * c

if (delta > 0) {
  # print x1, and x2 if delta > 0 
  delta_sq <- sqrt(delta)
  x1 <- (-b - delta_sq) / 2 * a
  x2 <- (-b + delta_sq) / 2 * a
  cat("x1 = ", x1, ", x2 = ", x2)
} else if (delta == 0) {
  # print x0 if delta == 0 
  x0 <- -b / 2 * a
  cat("x0 = ", x0)
} else {
  # print 'no solutions' if delta < 0 
  print("No solutions")
}
