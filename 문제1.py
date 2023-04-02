import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({'감정':['angry', 'disgusted','fearful', 'happy', 'neutral', 'sad', 'surprised'],
                 'angry': [976, 0, 0, 0, 6, 18, 0],
                 'disgusted': [0, 997, 0, 0, 3, 0, 0],
                 'fearful': [1, 0, 982, 0, 0, 6, 11],
                 'happy': [1, 2, 2, 995, 0, 0, 0],
                 'neutral': [14, 0, 0, 0, 975, 11, 0],
                 'sad': [17, 0, 0, 0, 5, 978, 0],
                 'surprised': [0, 0, 3, 0, 0, 0, 997]})

sns.heatmap(df.corr(), cmap='coolwarm', annot=True)
plt.xticks(rotation=45)
plt.show()