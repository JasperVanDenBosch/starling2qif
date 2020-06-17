from unittest import TestCase
from unittest.mock import patch, mock_open


EXAMPLE_IN = """Date,Counter Party,Reference,Type,Amount (GBP),Balance (GBP),Spending Category
01/04/2020,Starling Bank,March Interest Earned,DEPOSIT INTEREST,0.02,100.02,INCOME
10/04/2020,J Van Den Bosch,STARLING TRANSFER,FASTER PAYMENT,100.00,200.02,INCOME
12/04/2020,Starbucks,PYV*Thai Food Theory B S-GRAVENHAGE  NLD,GOOGLE PAY,-31.48,168.54,EATING_OUT
14/04/2020,SPAR,IZ *Free Beer Co.      ?S-GRAVENHAGE NLD,GOOGLE PAY,-12.22,156.32,GROCERIES
"""


EXAMPLE_OUT = """!Type:Bank
D01/04/2020
Starling Bank
T0.02
^
D10/04/2020
J Van Den Bosch
T100.00
^
D12/04/2020
PPYV*Thai Food Theory B S-GRAVENHAGE  NLD
T-31.48
^
D14/04/2020
PIZ *Free Beer Co.      ?S-GRAVENHAGE NLD
T-12.22
^
"""


class MainTests(TestCase):

    def test_convert_contents(self):
        """Test the data that convert() writes to the qif output file.
        """
        with patch("builtins.open", mock_open(read_data=EXAMPLE_IN)) as mock_file:
            import starling2qif.main
            starling2qif.main.convert('statement.csv')
            mock_file().write.assert_called_once_with(EXAMPLE_OUT)

    def test_convert_io(self):
        """Test the filepaths that convert() uses.
        """
        with patch("builtins.open", mock_open(read_data=EXAMPLE_IN)) as mock_file:
            import starling2qif.main
            starling2qif.main.convert('path/to/my_statement.csv')
            mock_file.assert_any_call('path/to/my_statement.csv')
            mock_file.assert_called_with('path/to/my_statement.qif', 'wb')
