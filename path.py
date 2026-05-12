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

    # 그래프 초기 상태 시각화
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("초기 그래프 상태")
    plt.show()

    return G


def add_obstacles(G, obstacles):
    """
    장애물(간선)을 그래프에서 제거하는 함수
    """
    for obstacle in obstacles:
        if G.has_edge(obstacle[0], obstacle[1]):
            G.remove_edge(obstacle[0], obstacle[1])
        else:
            print(f"장애물로 지정된 {obstacle}는 그래프에 존재하지 않습니다.")


def get_obstacles_input():
    """
    사용자로부터 장애물 정보를 입력받는 함수
    """
    obstacles_input = input("장애물로 설정할 간선을 입력하세요 (예: A-B, C-D). 끝내려면 엔터: ").strip()
    obstacles = []
    if obstacles_input:
        obstacle_pairs = obstacles_input.split(", ")
        for pair in obstacle_pairs:
            nodes = pair.split("-")
            obstacles.append((nodes[0], nodes[1]))
    return obstacles


def calculate_shortest_path_and_distances(G, start, end):
    path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
    total_distance = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')
    print(f"최단 경로: {path}, 총 거리: {total_distance}")

    # 경로상의 각 노드에서의 누적 거리 계산 및 출력
    current_distance = 0
    for i in range(len(path) - 1):
        edge_weight = G[path[i]][path[i + 1]]['weight']
        current_distance += edge_weight
        print(f"{path[i]}에서 {path[i + 1]}까지 이동: 누적 거리 = {current_distance}")

    return path


def draw_path(G, path):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("최단 경로 시각화")
    plt.show()

if __name__ == "__main__":
    # 그래프 생성 및 초기 상태 시각화
    G = create_and_draw_graph()

    # 사용자로부터 장애물 입력 받기
    obstacles = get_obstacles_input()
    add_obstacles(G, obstacles)

    # 장애물을 반영한 그래프 시각화
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("장애물 반영 후 그래프 상태")
    plt.show()

    # 시작점과 끝점 지정
    start, end = 'A', 'F'  # 예시로 A에서 F까지의 최단 경로를 찾습니다. 필요에 따라 변경 가능

    # 최단 경로 계산 및 시각화
    path = calculate_shortest_path_and_distances(G, start, end)
    draw_path(G, path)

# 기존 그래프 생성