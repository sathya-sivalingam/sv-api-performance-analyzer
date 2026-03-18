import pandas as pd
import matplotlib.pyplot as plt

def analyze(file_path):
    df = pd.read_csv(file_path)

    print("===== PERFORMANCE REPORT =====")
    print(f"Average Response Time: {df['response_time'].mean()}")
    print(f"Max Response Time: {df['response_time'].max()}")

    plt.plot(df['response_time'])
    plt.title("Response Time Trend")
    plt.xlabel("Requests")
    plt.ylabel("Response Time")
    plt.savefig("reports/performance_graph.png")
    print("Graph saved to reports/")
