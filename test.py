from rapidfuzz import fuzz
import jaro
import time

s2 = "Amoonguss (Master Ball Pattern)"
s1 = "Amoonguss"

s = time.time()
print(fuzz.ratio(s1, s2), time.time()-s)
s = time.time()
print(jaro.jaro_winkler_metric(s1, s2), time.time()-s)
s = time.time()
print(fuzz.token_set_ratio(s1, s2), time.time()-s)