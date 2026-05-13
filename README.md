# Drone-Safety-Path-Planning
English: Integrated framework for drone flight safety: Improving data quality and optimizing flight paths in restricted areas.  (한국어: 드론 운항 안전성 확보를 위한 데이터 품질 개선 및 비행 제한 구역 기반 최적 경로 설정 통합 프레임워크)


Drone-Safety-Path-Planning
Integrated Framework for Drone Flight Safety: Data Quality Improvement and Path Optimization

이 프로젝트는 드론 운항의 안전성을 높이기 위한 두 가지 핵심 연구를 통합하여 다룹니다. 고품질의 비행 데이터 구축 방법론과 이를 활용하여 제한 구역 내에서 안전하게 비행할 수 있는 최적 경로 알고리즘을 제안합니다.

📑 Featured Research (Papers)
본 프로젝트는 다음 두 개의 연구 성과를 바탕으로 구성되었습니다. (제1저자 논문)

드론 운항 안전성 제고를 위한 데이터 구축 및 품질 개선 이슈

데이터 인프라의 신뢰성을 확보하기 위한 구축 및 품질 관리 프로세스 제안

드론 운항에서의 제한 구역을 고려한 최적 경로 설정

비행 금지 구역 및 지리적 제약 조건을 고려한 알고리즘 설계

📈 Demo & Results

shortest-path1.py

<img width="230" height="154" alt="image" src="https://github.com/user-attachments/assets/2183d283-3a40-4e3f-be77-40184ccce680" />

<img width="262" height="155" alt="image" src="https://github.com/user-attachments/assets/dc324310-a5bb-49e3-9356-255a72f25666" />

<img width="959" height="503" alt="image" src="https://github.com/user-attachments/assets/afadbd2f-747a-49c3-b8eb-fba340c2d28b" />

경로를 탐색할 때 최단 경로를 찾는 모습입니다.

출발지(A)에서 도착지(F)까지의 경로가 단순 직선뿐이라면 좋겠지만

실제 도로에서는 많은 변수가 존재합니다. 

실제로 직선인 길이 항상 먼저 도착하는 것은 아닙니다.

도로상황에 따라서 차량이 많거나 사고가 발생하여 지체가 되는 등의 여러 문제들이 있습니다.

알고리즘을 통해 단순 거리뿐만 아니라 실제 비용과 시간을 적게 사용하는 것이 중요하다고 생각합니다.



shortest-path2.py

obstacle.py
<img width="959" height="503" alt="image" src="https://github.com/user-attachments/assets/a8e76e46-9dcb-4ab5-a5be-8c6f02f63718" />

코드를 실행하면 사진과 같은 결과가 나옵니다.
격자의 크기, 랜덤 장애물의 개수를 수정하면 그에 따라 변화합니다.

<img width="959" height="503" alt="image" src="https://github.com/user-attachments/assets/199da761-b1b1-4a04-8a4b-7a56381cc0c7" />

이 사진은 격자의 크기: 50, 랜덤 장애물의 개수: 640 의 결과물입니다.

실제 드론이 하늘을 비행할 때 여러 이유로 비행하면 안되는 금지 구역이 있습니다.

금지 구역을 피하며 도착지까지의 최단 경로로 이동할 수 있어야 한다고 생각했습니다.


🚀 Key Features
Data Quality Management: 드론 운항 데이터의 정확도와 정밀도를 높이는 데이터 정제 기법

Path Optimization: 복잡한 제한 구역 내에서 충돌을 방지하는 최단 및 최적 경로(Optimal Path) 계산

Safety First: 비행 안전성을 최우선으로 고려한 경로 생성 알고리즘

🛠 Tech Stack
Languages: Python

Focus: IoT, Drone Pathfinding Algorithms, Computer Vision

👤 Author
Youn minje (윤민제)

Undergraduate at Incheon National University, Electronic Engineering

Specialized in Embedded Systems & IoT Development
