import pandas as pd

clinical = pd.read_csv("Module2_FSHD_Dataset.csv")
print("Number of patients:", len(clinical))
print("Sex:", clinical["sex"].value_counts().to_dict())

# How many patients have data at each visit for the measures we compare
cols = {
    "MRI fat fraction (R)": ["ff_baseline_R", "ff_y1_R", "ff_y2_R"],
    "Dorsiflexion QMT (R)": ["dorsiflexion_qmt_R_baseline",
                             "dorsiflexion_qmt_R_y1",
                             "dorsiflexion_qmt_R_y2"],
    "10 m walk/run": ["wr_10_baseline", "wr_10_y1", "wr_10_y2"],
    "Timed up-and-go": ["tug_time_baseline", "tug_time_y1", "tug_time_y2"],
}
counts = pd.DataFrame(
    {name: clinical[c].notna().sum().values for name, c in cols.items()},
    index=["Baseline", "Year 1", "Year 2"],
)
counts