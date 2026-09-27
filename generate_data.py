import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

users = [f"user{i}" for i in range(1, 51)]

data = []

for i in range(n):
    user = np.random.choice(users)

    login_hour = np.random.randint(0, 24)
    files_accessed = np.random.randint(1, 50)
    data_downloaded = np.random.randint(10, 3000)

    if np.random.rand() < 0.05:
        login_hour = np.random.randint(0, 5)
        files_accessed = np.random.randint(100, 300)
        data_downloaded = np.random.randint(2000, 5000)

    data.append([user, login_hour, files_accessed, data_downloaded])

df = pd.DataFrame(data, columns=[
    "user",
    "login_hour",
    "files_accessed",
    "data_downloaded_mb"
])

df.to_csv("data/user_activity.csv", index=False)

print("✅ Dataset created successfully")