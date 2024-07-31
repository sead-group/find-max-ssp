"""
The main function to run end-to-end, for SSP results for the paper
"""

import os.path

from utils.file_utils import load_excel_file
from utils.misc_functions import get_list_of_all_possible_combinations_in_index_form, get_scenarios_in_sequence, \
                                  get_scenario_to_beta_mapping, process_ssp


def prepare_scenario_counts(scenarios):
    sc = {}
    for scen in scenarios:
        prfx = scen.split('_')[0]
        sc.update({prfx: sc.get(prfx, 0) + 1})
    return sc


def prepare_probability_mapping(df):
    probability_mapping = {
        f"AP{df.Scenario_Name[i]}": df.Probability[i]
        for i in range(0, len([elem for elem in df.Scenario_Name]))}
    return probability_mapping


if __name__ == '__main__':
    project_root = os.path.dirname(os.path.dirname(__file__))
    input_files_dir = os.path.join(project_root, 'input_files')
    plr_excel_sheet = os.path.join(input_files_dir, 'plr_sheet.xlsx')
    probabilities_excel_sheet = os.path.join(input_files_dir, 'probabilities.xlsx')

    df_plr = load_excel_file(plr_excel_sheet)
    df_probabilities = load_excel_file(probabilities_excel_sheet)

    scenarios_in_sequence, scenarios_in_sequence_without_postfix = get_scenarios_in_sequence(df_plr)
    scenario_counts = prepare_scenario_counts(scenarios=scenarios_in_sequence)
    scenario_probability_mapping = prepare_probability_mapping(df_probabilities)
    scenario_to_beta_mapping = get_scenario_to_beta_mapping(scenarios_in_sequence, df_plr)

    list_of_lengths_per_index = [scenario_counts[scenario] for scenario in scenarios_in_sequence_without_postfix]
    number_of_combos = 1
    for i in list_of_lengths_per_index:
        number_of_combos = number_of_combos * i

    list_of_all_possible_combinations = get_list_of_all_possible_combinations_in_index_form(list_of_lengths_per_index)

    combo_to_ssp, best_combo, best_ssp = process_ssp(
        list_of_all_possible_combinations,
        scenarios_in_sequence_without_postfix,
        scenario_probability_mapping,
        scenario_to_beta_mapping,
        number_of_combos=number_of_combos)

    print("BEST")
    print(best_ssp)
    print(best_combo)
