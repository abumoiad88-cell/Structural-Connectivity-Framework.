import networkx as nx
import numpy as np
import os

def calculate_structural_connectivity(file_path, network_name):
    if not os.path.exists(file_path):
        print(f"❌ Error: File {file_path} not found.")
        return

    # 1. تحميل الشبكة
    G = nx.read_edgelist(file_path)
    nodes = G.number_of_nodes()
    edges = G.number_of_edges()
    
    print(f"\n--- Analyzing {network_name} Network ---")
    print(f"Nodes: {nodes}, Edges: {edges}")

    # 2. حساب معاملات التوصيل (Control Parameter - Phi)
    degrees = [d for n, d in G.degree()]
    k_mean = np.mean(degrees)
    k2_mean = np.mean(np.square(degrees))
    
    # Molloy-Reed Criterion (kc)
    kc = k2_mean / k_mean
    phi = k_mean / kc  # Dimensionless reduced control parameter

    # 3. حساب المكونات المتصلة (Giant Component S1 & Signal S2)
    components = sorted(nx.connected_components(G), key=len, reverse=True)
    s1 = len(components[0]) / nodes
    s2 = len(components[1]) / nodes if len(components) > 1 else 0

    # 4. طباعة النتائج النهائية (تطابق المخرجات المتوقعة في بحثك)
    print(f"Control Parameter (Phi)  : {phi:.4f}")
    print(f"Giant Component (S1)     : {s1:.4f}")
    print(f"Structural Signal (S2)   : {s2:.4f}")
    
    if 0.95 <= phi <= 1.05:
        print(">>> Signal Peak Detected: Critical Transition Point.")

# --- تشغيل التحليل على البيانات المتاحة ---
# تأكد من وجود مجلد باسم data يحتوي على الملفات
if __name__ == "__main__":
    # تحليل شبكة فيسبوك
    calculate_structural_connectivity('data/facebook_data.txt', 'Facebook')
