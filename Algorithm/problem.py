test_number = 2
test_case = [
    {"number_of_bus": 4, "buses": "15 25 30 35 45 50 10 20", "number_of_city":2, "cities":[15, 25]},
    {"number_of_bus": 10, "buses": "10 15 5 12 40 55 1 10 25 35 45 50 20 28 27 35 15 40 4 5", "number_of_city":3, "cities":[5, 10, 27]}
    ]

def count_bus(test_number, test_case):
    # n번의 케이스에 대해서 실행
    for case in range(test_number):

        # 버스명 리스트로 생성
        bus_list = test_case[case]['buses'].split()

        # 버스 이름 생성
        n = test_case[case]['number_of_bus']
        bus_path = []
        for i in range(1,n+1):
            if int(bus_list[2*i-2]) > int(bus_list[2*i-1]):
                bus_path.append((int(bus_list[2*i-1]),int(bus_list[2*i-2])))
            elif int(bus_list[2*i-2]) < int(bus_list[2*i-1]):
                bus_path.append((int(bus_list[2*i-2]),int(bus_list[2*i-1])))

        # 도시를 지나가는지 확인
        bus_number = []
        for city in test_case[case]['cities']:
            n = 0
            # 버스가 해당 도시를 지나가면 count
            for bus in bus_path:
                if city in range(bus[0], bus[1]+1):
                    n += 1

            bus_number.append(n)

        print(f"문제#{case+1}:", bus_number)

count_bus(test_number,test_case)
