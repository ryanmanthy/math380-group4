import numpy as np
from ortools.graph.python import min_cost_flow

def main():
    smcf = min_cost_flow.SimpleMinCostFlow()

    # Defining variables
    cap_a, cap_b, cap_c, cap_d, cap_e, cap_f, cap_g, cap_h, cap_i = 75, 60, 87, 54, 92, 90, 38, 87, 49
    cost_a, cost_b, cost_c, cost_d, cost_e, cost_f, cost_g, cost_h, cost_i = 3, 4, 1, 2, 7, 2, 6, 2, 5
    sup_0, sup_1, sup_2, sup_3, sup_4 = 60, 40, 0, -45, -55

    # Defining arrays: sources, destinations, capacities, and unit costs between each pair
    # For example, the capacity from node 0 to node 2 is 75 and the cost is 3 per unit
    start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4])
    end_nodes = np.array([2, 3, 2, 3, 4, 3, 4, 4, 2])
    capacities = np.array([cap_a, cap_b, cap_c, cap_d, cap_e, cap_f, cap_g, cap_h, cap_i])
    unit_costs = np.array([cost_a, cost_b, cost_c, cost_d, cost_e, cost_f, cost_g, cost_h, cost_i])

    # Defining an array of supplies. (Negative numbers are demands)
    # For example, node 1 has a supply of 60 and node 4 has a demand of 55
    supplies = [sup_0, sup_1, sup_2, sup_3, sup_4]

    all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
        start_nodes, end_nodes, capacities, unit_costs)

    smcf.set_nodes_supplies(np.arange(0, len(supplies)), supplies)

    # Finding the min cost flow.
    status = smcf.solve()

    if status != smcf.OPTIMAL:
        print('There was an issue with the min cost flow input.')
        print(f'Status: {status}')
        exit(1)
    print(f'Minimum cost: {smcf.optimal_cost()}')
    print('')
    print(' Arc    Flow / Capacity Cost')
    solution_flows = smcf.flows(all_arcs)
    costs = solution_flows * unit_costs
    for arc, flow, cost in zip(all_arcs, solution_flows, costs):
        print(
            f'{smcf.tail(arc):1} -> {smcf.head(arc)}  {flow:3}  / {smcf.capacity(arc):3}       {cost}'
        )


if __name__ == '__main__':
    main()