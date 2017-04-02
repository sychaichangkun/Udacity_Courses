#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print enron_data['LAY KENNETH L']
i = 0 
for v in enron_data.values():
    if v['poi'] == True:
        i += 1
print i

salary_num = 0
email_num = 0
nonsalary_num =0
poi_num = 0
for name in enron_data:
    if 'LAY' in name or 'SKILLING' in name or 'FASTOW' in name:
        print name , enron_data[name]['total_payments']
    if isinstance(enron_data[name]['salary'],int):
        salary_num += 1
    if '@' in enron_data[name]['email_address']:
        email_num += 1
    if enron_data[name]['poi'] == True :
        poi_num += 1
        if 'NaN' == enron_data[name]['total_payments']: 
            nonsalary_num += 1


print salary_num
print email_num
print poi_num
print nonsalary_num
print 1.0*nonsalary_num/poi_num
print len(enron_data)