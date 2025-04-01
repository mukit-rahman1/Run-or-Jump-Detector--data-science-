import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import joblib
from scipy.stats import skew, kurtosis


'''
steps to follow

functions:
plot_predictions
keep clearing previous plot for new one
configure the graph using matplotlib
embed the plot into tkinter window
draw the plot
add it to tkinter window


MAIN APP:
Load tkinter title, button, label, frame
Load the model and scaler Z score method
Preprocess raw data by reducing noise and filling NaNs
Extract features from preprocessed data just gained
convert to dataframe then apply Z score normalization
start prediction
save result
plot predictions
'''


# configuration
WINDOW_SIZE = 500  # 5 seconds × 100 Hz
# extract features function
def extract_features(window):
    df = pd.DataFrame(window, columns=['time', 'x', 'y', 'z', 'absolute'])
    data = df['absolute']
    return {
        'absolute_mean': data.mean(),
        'absolute_std': data.std(),
        'absolute_min': data.min(),
        'absolute_max': data.max(),
        'absolute_skew': skew(data),
        'absolute_kurtosis': kurtosis(data),
        'absolute_var': data.var(),
        'absolute_range': data.max() - data.min(),
        'absolute_median': data.median(),
        'absolute_rms': np.sqrt(data.mean())
    }



# The App
class ClassifierApp:
    def __init__(self, master):
        #tkinter set up
        self.master = master
        master.title("Run vs Jump Classifier")

        self.label = tk.Label(master, text="Select a raw CSV file (x, y, z, absolute):")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(master, text="Browse CSV", command=self.load_file)
        self.browse_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        self.plot_frame = tk.Frame(master)
        self.plot_frame.pack()



        #load the model and scaler Z score method
        try:
            self.model, self.scaler = joblib.load("final_model.pkl")
        except:
            messagebox.showerror("Model Load Error", "Could not load final_model.pkl")
            master.quit()


    #load file function
    def load_file(self):
        #take in only csv files
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            #read csv as raw data
            raw_df = pd.read_csv(file_path)


            # make sure columns are named correctly
            raw_df.columns = ['time', 'x', 'y', 'z', 'absolute']


            # reduce noise by smoothing
            window_size = 50
            for axis in ['x', 'y', 'z', 'absolute']:
                raw_df[axis] = raw_df[axis].rolling(window=window_size).mean() #apply rolling to all columns except time

            # fill NaNs caused by rolling
            raw_df.interpolate(method='linear', inplace=True)
            raw_df.fillna(method='bfill', inplace=True)
            raw_df.fillna(method='ffill', inplace=True)

            data = raw_df[['time', 'x', 'y', 'z', 'absolute']].values


            # segment into windows then extract features
            num_windows = len(data) // WINDOW_SIZE
            features = []
            for i in range(num_windows):
                start = i * WINDOW_SIZE
                end = start + WINDOW_SIZE
                window = data[start:end]
                feats = extract_features(window)
                features.append(feats)


            #convert to dataframe then apply Z score normalization
            features_df = pd.DataFrame(features)
            X_raw = features_df.values
            X = self.scaler.transform(X_raw)  # Use the trained scaler


            #start prediction
            y_pred = self.model.predict(X)
            label_names = ['walking', 'jumping']
            features_df['prediction'] = [label_names[i] for i in y_pred] #add prediction column 0 for walking and 1 for jumping



            #save result
            out_path = file_path.replace('.csv', '_predicted.csv')
            features_df.to_csv(out_path, index=False)

            self.result_label.config(text=f"The predictions have been saved to:\n{out_path}")
            self.plot_predictions(y_pred) #plot predictions

        except Exception as e:
            messagebox.showerror("error", f"Error:\n{e}")


    #plot predictions function
    def plot_predictions(self, predictions):
        for widget in self.plot_frame.winfo_children(): #clear previous plot to update for new one
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(predictions, marker='o', linestyle='-', color='teal')
        ax.set_title("Predicted Labels per Window")
        ax.set_xlabel("Segment Index")
        ax.set_ylabel("Prediction")
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['Walking', 'Jumping'])
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame) #embed the plot into tkinter window as self.plot_frame
        canvas.draw() # draw the plot
        canvas.get_tk_widget().pack() #add it to tkinter window

# Run
root = tk.Tk() #make base tkinter window
app = ClassifierApp(root) #create app instance called app and pass in base window
root.mainloop()
