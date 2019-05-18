def phred33_to_q(qual):
  #Turn Phred+33 ASCII-encoded quality into Phred-scaled integer
  return ord(qual)-33

def q_to_p(Q):
  #Turn Phred-scaled integer into error probability
  return 10.0 ** (-0.1 * Q)

print(q_to_p(phred33_to_q('!')))
print(q_to_p(phred33_to_q('I')))
