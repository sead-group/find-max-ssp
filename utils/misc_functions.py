import numpy


def get_scenarios_in_sequence(df_plr):
    scenarios_in_sequence = [elem for elem in df_plr.Scenario_Name]
    scenarios_in_sequence_without_postfix = []
    for scenario in scenarios_in_sequence:
        prefix = scenario.split('_')[0]
        if prefix not in scenarios_in_sequence_without_postfix:
            scenarios_in_sequence_without_postfix.append(prefix)

    return scenarios_in_sequence, scenarios_in_sequence_without_postfix


def get_scenario_to_beta_mapping(scenarios_in_sequence, df_plr):
    # need to get the beta for each scenario
    scenario_to_beta_mapping = {}
    for i in range(0, len(scenarios_in_sequence)):
        scenario_to_beta_mapping[scenarios_in_sequence[i]] = get_beta(df_plr, i)
    return scenario_to_beta_mapping


def get_u_plus_delta(comma_separated_string_form):
    split_form = [float(elem) for elem in comma_separated_string_form.split(', ')]
    u = numpy.mean(split_form)
    delta = u - split_form[0]
    return u + delta


def get_list_of_all_possible_combinations_in_index_form(list_of_lengths_per_index):
    """

    :param list_of_lengths_per_index: This is a list that looks something like: [1, 3, 1]
                                        meaning, the first element is only a single value, the next one has 3 possible
                                        values. For example, binary would be [2, 2, 2]

    :return: list_of_all_possible_combinations_in_index_form: Example:
        ["0,0", "0,1", "1,0", "1,1"] (if input was binary)
        ["0,0,0", "0,1,0", "0,2,0"] if input was [1, 3, 1]
    """
    growing_list = []
    for main_index in reversed(range(0, len(list_of_lengths_per_index))):
        num_of_options = list_of_lengths_per_index[main_index]
        current_options = [f"{i}" for i in range(0, num_of_options)]

        # dump the current_options in a list (for reuse)
        add_to_growing_list = []
        for i in current_options:
            # create "prefix,i,element" for element in growing_list
            if growing_list:
                add_to_growing_list = add_to_growing_list + [f"{i},{elem}" for elem in growing_list]
            else:
                add_to_growing_list = add_to_growing_list + [f"{i}"]

        growing_list = add_to_growing_list

    non_string_growing_list = []
    for entry in growing_list:
        list_form = [int(elem) for elem in entry.split(',')]
        non_string_growing_list.append(list_form)

    return non_string_growing_list


def protect_against_zero(val):
    conversion_for_zero = 0.0001

    if val == 0:
        return conversion_for_zero
    else:
        return val


def get_beta(df, index):
    alpha = 0.25

    plr_cell_1 = protect_against_zero(float(get_u_plus_delta(df.CELL_1_PLR[index])))
    plr_cell_2 = protect_against_zero(float(get_u_plus_delta(df.CELL_2_PLR[index])))
    plr_cell_3 = protect_against_zero(float(get_u_plus_delta(df.CELL_3_PLR[index])))
    plr_cell_4 = protect_against_zero(float(get_u_plus_delta(df.CELL_4_PLR[index])))
    plr_cell_5 = protect_against_zero(float(get_u_plus_delta(df.CELL_5_PLR[index])))

    beta = (alpha/plr_cell_1) + (1/plr_cell_2) + (alpha/plr_cell_3) + (1/plr_cell_4) + (alpha/plr_cell_5)

    return beta


def process_ssp(list_of_of_all_possible_combinations,
                scenarios_in_sequence_without_postfix,
                scenario_probability_mapping,
                scenario_to_beta_mapping,
                print_all=False):
    combo_to_ssp = {}
    best_combo = None
    best_ssp = 0
    for combo in list_of_of_all_possible_combinations:
        # this is a list of indices
        # Go through the full combo, calculate the 'SSP'
        ssp = 0
        for index in range(0, len(scenarios_in_sequence_without_postfix)):
            # assemble state name:
            state_name_no_postfix = scenarios_in_sequence_without_postfix[index]
            state_name = state_name_no_postfix + f"_{combo[index] + 1}"

            probability = scenario_probability_mapping[state_name_no_postfix]
            beta = scenario_to_beta_mapping[state_name]

            ssp += probability * beta

        combo_to_ssp[str(combo)] = ssp

        if print_all:
            print(f"{combo}: {ssp}")

        if ssp > best_ssp:
            # keep track of the best SSP so far
            best_combo = combo
            best_ssp = ssp

    return combo_to_ssp, best_combo, best_ssp
