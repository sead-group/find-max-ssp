import unittest

from utils.misc_functions import process_ssp


class TestMainFunctions(unittest.TestCase):

    """
    This is a very basic placeholder test. More to come.
    """
    def test_ssp_calculation(self):
        some_combos = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2]]

        scenarios_in_seq_without_postfix = [
            'AP12345',
            'AP1234',
            'AP1235',
            'AP1245',
            'AP2345',
            'AP1345',
            'AP123',
            'AP124',
            'AP125',
            'AP134',
            'AP135',
            'AP234',
            'AP345',
            'AP245',
            'AP145',
            'AP235',
            'AP24']

        scen_to_prob_mapping = {
            'AP12345': 0.155,
            'AP1234': 0.0581,
            'AP1235': 0.0155,
            'AP2345': 0.0581,
            'AP1345': 0.0155,
            'AP1245': 0.0581,
            'AP123': 0.0149,
            'AP124': 0.0697,
            'AP125': 0.0149,
            'AP134': 0.0149,
            'AP135': 0.0034,
            'AP145': 0.0149,
            'AP234': 0.0697,
            'AP235': 0.0149,
            'AP245': 0.0697,
            'AP345': 0.0149,
            'AP24': 0.314,
            'APF': 0.0237}

        scen_to_beta = {
            'AP12345_1': 8.014569070058158,
            'AP1234_1': 2574.1474038883607,
            'AP1235_1': 12520.160506427546,
            'AP1235_2': 82.5231227701996,
            'AP1245_1': 10038.948392574557,
            'AP1245_2': 2555.5288681709385,
            'AP2345_1': 2574.1474038883607,
            'AP1345_1': 12520.160506427546,
            'AP1345_2': 82.5231227701996,
            'AP123_1': 21.406292632584872,
            'AP123_2': 10017.03651245981,
            'AP123_3': 2541.812420050828,
            'AP123_4': 2523.306191344672,
            'AP123_5': 35.35688219046193,
            'AP123_6': 35.05705419181285,
            'AP123_7': 8.070215446199391,
            'AP124_1': 31.79912867239273,
            'AP124_2': 52.98066058374316,
            'AP124_3': 45.41531245658949,
            'AP124_4': 2515.255286092152,
            'AP124_5': 25.60308627348496,
            'AP125_1': 30.54870455844653,
            'AP125_2': 46.20635535697413,
            'AP125_3': 2529.9751200994588,
            'AP125_4': 73.74131538662573,
            'AP134_1': 31.879867862809974,
            'AP134_2': 11.471120524095955,
            'AP134_3': 46.51476716114118,
            'AP134_4': 2520.9380583024613,
            'AP135_1': 2518.5083019471026,
            'AP135_2': 36.35625354968142,
            'AP234_1': 2517.477906092838,
            'AP234_2': 21.637236628252868,
            'AP345_1': 21.406292632584872,
            'AP345_2': 10017.03651245981,
            'AP345_3': 2541.812420050828,
            'AP345_4': 2523.306191344672,
            'AP345_5': 35.35688219046193,
            'AP345_6': 35.05705419181285,
            'AP345_7': 8.070215446199391,
            'AP245_1': 31.79912867239273,
            'AP245_2': 52.98066058374316,
            'AP245_3': 45.41531245658949,
            'AP245_4': 2515.255286092152,
            'AP245_5': 25.60308627348496,
            'AP145_1': 30.54870455844653,
            'AP145_2': 46.20635535697413,
            'AP145_3': 2529.9751200994588,
            'AP145_4': 73.74131538662573,
            'AP235_1': 31.879867862809974,
            'AP235_2': 11.471120524095955,
            'AP235_3': 46.51476716114118,
            'AP24_1': 10.078456203005413,
            'AP24_2': 19.552897570403434,
            'AP24_3': 17.03659871466652}

        expected_combo_ssp = {'[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]': 1465.8729148900923,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]': 1468.8478894794553,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]': 1468.0577716387538,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]': 1465.5688245547456,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]': 1468.5437991441086,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]': 1467.7536813034071,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]': 1466.0909748896374,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1]': 1469.0659494790004,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2]': 1468.275831638299,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]': 1466.1062138869904,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]': 1469.0811884763534,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2]': 1468.291070635652,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]': 1465.8021235516437,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]': 1468.7770981410067,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2]': 1467.9869803003053,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0]': 1466.3242738865356,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1]': 1469.2992484758986,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2]': 1468.5091306351972,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0]': 1503.1143684816534,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1]': 1506.0893430710164,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2]': 1505.299225230315,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0]': 1502.8102781463067,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1]': 1505.7852527356697,
                              '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2]': 1504.9951348949683}

        expected_best_combo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1]
        expected_best_ssp = 1506.0893430710164

        combo_ssp, best_combo, best_ssp = process_ssp(some_combos,
                                                      scenarios_in_seq_without_postfix,
                                                      scen_to_prob_mapping,
                                                      scen_to_beta)

        self.assertDictEqual(combo_ssp, expected_combo_ssp)
        self.assertListEqual(best_combo, expected_best_combo)
        self.assertEqual(best_ssp, expected_best_ssp)
