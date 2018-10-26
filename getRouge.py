from pythonrouge.pythonrouge import Pythonrouge
import os
import numpy as np

#gold folder
gold_folder = PATH_TO_GOLD_FOLDER

jm = PATH_TO_EXPT1_FOLDER

#cm = PATH_TO_EXPT2_FOLDER

jmfiles = [f for f in os.listdir(jm)]

R1 = []
R2 = []

for f in jmfiles:
  idd = f.strip().split(".")[0]
  gen_fp = open(os.path.join(cm, f), 'r')
  genlines = gen_fp.readlines()
  gensumm = ""
  for line in genlines:
    gensumm += line.strip()
  gen_fp.close()
  gold_fp = open(os.path.join(gold_folder, idd+".txt"))
  goldlines = gold_fp.readlines()
  goldsumm = ""
  for line in goldlines:
    goldsumm += line.strip()
  gold_fp.close()
  summary = [[gensumm]]
  reference = [[[goldsumm]]]
  rouge = Pythonrouge(summary_file_exist=False,
                    summary=summary, reference=reference,
                    n_gram=2, ROUGE_SU4=True, ROUGE_L=False,
                    recall_only=True, stemming=True, stopwords=True,
                    word_level=True, length_limit=True, length=50,
                    use_cf=False, cf=95, scoring_formula='average',
                    resampling=True, samples=1000, favor=True, p=0.5)
  score = rouge.calc_score()
  r1 = score['ROUGE-1']
  r2 = score['ROUGE-2']
  R1.append(r1)
  R2.append(r2)
  #print [idd, score]


print np.mean(np.array(R1))
print np.mean(np.array(R2))
