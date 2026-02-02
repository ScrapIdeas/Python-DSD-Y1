import pandas as pd
data = {
    "Name":["Alex","Jamie","Sam","NewStudent4"],
    "Attendance":[92,85,78,55],
    "Grade":["B","C","D","D"],
}
dt = pd.DataFrame(data)
print(dt)