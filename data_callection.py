

import glassdoor_scraping as gs
import pandas as pd

path = "C:\\Users\\exeller\\Documents\\Data Science Projects\\ds_salary_proj\\chromedriver"

df = gs.get_jobs("data scientist", 1000, False, path, 2)

df.to_csv('glassdoor_jobs.csv',index = False)
