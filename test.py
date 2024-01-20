import unittest
import json
from http_api import app

class FlaskTest(unittest.TestCase):
    def testPredict(self):
        tester = app.test_client(self)

        # test_data = {
        #     '1980' : 23.836, '1981' : 20.305, '1982' : 24.828, '1983' : 25.388, '1984' : 24.076, 
        #     '1985' : 20.738, '1986' : 14.416, '1987' : 14.248, '1988' : 19.222, '1989' : 17.617,
        #     '1990' : 22.593, '1991' : 16.916, '1992' : 12.392, '1993' : 15.061, '1994' : 14.207,
        #     '1995' : 16.662, '1996' : 14.899, '1997' : 12.532, '1998' : 12.122, '1999' : 11.019,
        #     '2000' : 9.460, '2001' : 9.371, '2002' : 10.313, '2003' : 15.568, '2004' : 16.163, 
        #     '2005' : 16.019, '2006' : 14.700, '2007' : 12.845, '2008' : 13.087, '2009' : 15.244,  
        #     '2010' : 13.549, '2011' : 12.123, '2012' : 12.476, '2013' : 10.347, '2014' : 11.407,
        #     '2015' : 13.090, '2016' : 12.895, '2017' : 14.208, '2018' : 9.486, '2019' : 11.133,
        #     '2020' : 10.386, '2021' : 8.926, '2022' : 8.683 
        # } 

        test_data = {
            '2018' : 9.486, '2019' : 11.133, '2020' : 10.386, '2021' : 8.926, '2022' : 8.683
        }

        response = tester.post('/predict', data=json.dumps(test_data), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertIn('predicted_gdp_per_capita', response_data)

if __name__ == '__main__':
    unittest.main()