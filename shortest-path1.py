import matplotlib.pyplot as plt
import networkx as nx
import random

def create_and_draw_graph():
    # 그래프 생성 및 노드 간 랜덤 거리 설정
    G = nx.Graph()

    # 노드 추가
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    G.add_nodes_from(nodes)

    # 간선 및 가중치(거리) 추가 - 모든 가능한 연결을 고려
    for node1 in nodes:
        for node2 in nodes:
            if node1 != node2 and not G.has_edge(node1, node2):
                G.add_edge(node1, node2, weight=random.randint(1, 7))

    return G

def calculate_shortest_path_and_distances(G, start, end):
    path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
    total_distance = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')
    print(f"최단 경로: {path}, 총 거리: {total_distance}")

    # 경로상의 각 노드에서의 누적 거리 계산 및 출력
    current_distance = 0
    for i in range(len(path)-1):
        edge_weight = G[path[i]][path[i+1]]['weight']
        current_distance += edge_weight
        print(f"{path[i]}에서 {path[i+1]}까지 이동: 누적 거리 = {current_distance}")

    return path

def draw_path(G, path):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

G = create_and_draw_graph()

# 사용자 입력을 받아 출발지와 도착지 설정
start_point = input("출발지점을 입력하세요 (예: A): ").strip()
end_point = input("도착지점을 입력하세요 (예: F): ").strip()

# 최단 경로 계산 및 출력
shortest_path = calculate_shortest_path_and_distances(G, start_point, end_point)

# 최단 경로 시각화
draw_path(G, shortest_path)