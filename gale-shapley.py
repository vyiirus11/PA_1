# Initialize each person and hospital to be free.
# while (some hospital is free and hasn't been match/assigned
# to every applicant) {
#     Choose such a hospital H
#     a = 1st applicant on H's list to whom H has not been matched
#    if (a is free) 
#        Match H and a
#    else if (a prefers H to its current assignment H')
#        Match H and a
#        Free H'
#    else
#        a rejects H
# }