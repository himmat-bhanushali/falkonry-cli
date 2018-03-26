# import os
# import unittest
# from unittest.mock import Mock, patch
# from .context import falkonry as FalkonryCli
# from falkonryclient import client as Falkonry
# import xmlrunner
#
# class TestDatastream(unittest.TestCase):
#     """Class containing all the tests pertaining to Datastreams"""
#     def setUp(self):
#         self.host = 'https://localhost:8080'1
#         self.token = 't6vl8dty74ngy9r4vy29r6pkth4b4npj'
#         # self.cli = mock.Mock(Fclient.REPL())
#         # self.cli = Fclient.REPL()
#         # Fclient.validate_login = mock.Mock(return_value=True)
#     # @patch('falkonry._falkonry', side_effect=Falkonry('host','token'))
#     # @patch('falkonry.REPL', return_value=True)
#     # def test_do_datastream_get_list(self,mockFalkonryCli, mockFalkonry):
#     #     falkonry_cli = mockFalkonryCli
#     #     falkonry_cli._falkonry = mockFalkonry
#     #     FalkonryCli.REPL.do_datastream_get_list(mockFalkonryCli,'')
#         # falkonry_cli.assert_any_call()
#     # @patch('falkonry.REPL')
#     # @patch('falkonry.validate_login',return_value=True)
#     @patch('falkonry.check_login', return_value=True)
#     @patch('falkonry._falkonry',)
#     def test_do_datastream_get_list(self, mockClient, mockLoggedIn):
#         falkonry_cli = Mock(FalkonryCli)
#         falkonry_cli.REPL = Mock(FalkonryCli.REPL())
#         mockClient.return_value = Mock(Falkonry(host=self.host, token=self.token, options={"header":"falkonry-cli"}))
#         falkonry_cli.REPL.do_datastream_get_list(falkonry_cli.REPL,'')
#         assert mockClient.called
#         # falkonry_cli.REPL.do_datastream_get_list = Mock(FalkonryCli.REPL.do_datastream_get_list)
#         # falkonry_cli.REPL.do_datastream_get_list.assert_any_call()
#     # @patch('falkonry.validate_login',return_value=True)
#     # def test_do_login(self,mockValidateLogin):
#     #     FalkonryCli.REPL.do_login = Mock(return_value=True)
#     #     FalkonryCli.REPL.do_login()
#
#
# if __name__ == '__main__':
#     unittest.main(
#         testRunner=xmlrunner.XMLTestRunner(output='out'),
#         failfast=False, buffer=False, catchbreak=False)
