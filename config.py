inputs = {
    "target": "BC",
    "calculate_interval": False,
    "n_random_trials": 10,

}

structure = {

    "black_list" : [
                    ('Age', 'Sex'),
                    ('BMI', 'Sex'),
                    ('PA', 'Sex'),
                    ('Alcohol', 'Sex'),
                    ('Smoking', 'Sex'),
                    ('Diabetes', 'Sex'),
                    ('Obesity', 'Sex'),
                    ('Hypertension', 'Sex'),
                    ('Hyperchol.', 'Sex'),
                    ('BC', 'Sex'),
                    ('SES', 'Sex'),            

                    ('Sex', 'Age'),
                    ('BMI', 'Age'),
                    ('PA', 'Age'),
                    ('Alcohol', 'Age'),
                    ('Smoking', 'Age'),
                    ('Obesity', 'Sex'),
                    ('Diabetes', 'Age'),
                    ('Hypertension', 'Age'),
                    ('Hyperchol.', 'Age'),
                    ('BC', 'Age'),
                    ('SES', 'Age'),

                    ('BMI', 'SES'),
                    ('PA', 'SES'),
                    ('Alcohol', 'SES'),
                    ('Smoking', 'SES'),
                    ('Obesity', 'Sex'),
                    ('Diabetes', 'SES'),
                    ('Hypertension', 'SES'),
                    ('Hyperchol.', 'SES'),
                    ('BC', 'SES'),
        ], 

    "fixed_edges" : [
                    ('Sex', 'SES'),
                    ('Sex', 'BC'),

                    ('Age', 'BC'),
                    ('Age', 'Diabetes'),
                    ('Age', 'Smoking'), 
                    ('Age', 'Hypertension'), 
                    ('Age', 'BMI'),
                    ('Age', 'Obesity'),
                    ('Age', 'SES'),
                    ('Age', 'PA'),
                    
                    ('BMI', 'Diabetes'), 
                    ('BMI', 'Hyperchol.'), 
                    ('BMI', 'Hypertension'),
                    ('BMI', 'Obesity'), 

                    ('Alcohol', 'BC'),
                    ('Alcohol', 'Hypertension'),
                    ('Alcohol', 'Hyperchol.'),

                    ('Smoking', 'BC'), 
                    ('Smoking', 'Hyperchol.'),
                    ('Smoking', 'Hypertension'), 

                    ('PA', 'Diabetes'), 
                    ('PA', 'Hyperchol.'), 
                    ('PA', 'Hypertension'), 
                    ('PA', 'BMI'),
                    ('PA', 'Obesity'),

                    ('Diabetes', 'BC'), 
                    ('Diabetes', 'Hypertension'),

                    ('Hypertension', 'BC'), 

                    ('Hyperchol.', 'BC'),
                    
                    ('Obesity', 'Diabetes'),
                    ('Obesity', 'Hypertension'),
                    ('Obesity', 'BC'),

                    ('SES', 'PA'),
        ]
}


node_color = {'Age': 0.3,
                'Sex': 0.3,
                'Alcohol': 0.1,
                'Smoking': 0.1,
                'PA': 0.1,
                'BMI': 0.1,
                'Diabetes': 0.2,
                'Hypertension': 0.2,
                'Hyperchol.': 0.2,
                'Obesity': 0.2,
                'SES': 0.3,
                'BC': 0.4}


pointwise_risk_mapping = {
    "col_var": "Age",
    "row_var": "BMI"
}

interval_risk_mapping = {
    "col_var": "Age",
    "row_var": "BMI"
}

interval_path = {'path': "test14march/"}