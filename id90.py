
# pip install names

import datetime
import faker
import random
import os

fake = faker.Faker()

states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

sample_ids = [0]



class Set:

    def __init__(self, sample_count: int, min_record_count: int = 50 ,max_record_count: int = 200, set_record_count: int = 0 ):

        if set_record_count != 0:
            min_record_count = set_record_count
            max_record_count = set_record_count

        self.samples = [Sample(random.randint(min_record_count, max_record_count)) for _ in range(sample_count)]

    def get_txt_dict(self):
        out_dict = {}
        for s in self.samples:
            out_dict[s.label] = s

        return(out_dict)
    
    def write_txts(self, path):
        store_dict = self.get_txt_dict()

        if not os.path.exists(path):
            os.makedirs(path)

        save_path = (path+'\\').replace('\\\\','\\')
        ncount = 1
        for k in store_dict.keys():
            txt_name = 'id90_fake_'+k

            with open(save_path+txt_name+'.txt','w') as f:
                f.write(store_dict[k].to_txt())




class Sample:

    def __init__(self ,record_count: int):
        self.label = str(datetime.date.today()).replace('-','')+'_'+str(max(sample_ids)+1)
        self.nrow = record_count

        sample_ids.append(max(sample_ids)+1)

        self.header = open('source\\header.txt','r').read().replace('\n','')
        self.headers = [h for h in self.header.split('|')]

        self.id90dict = Row(record_count).rows


    def to_txt(self, ugly = True):
        headers = [h+'|*|' for h in self.id90dict.keys()]
        head_txt = ''.join(headers)+'|#|\n'
        head_txt = head_txt.replace('*||#','#')

        pr_ugly = 5

        if ugly and random.randint(1,pr_ugly) == 1:
            head_txt = ''

        final_txt = head_txt
        for i in range(self.nrow):
            rows = [v[i] for v in self.id90dict.values()]
            
            if ugly:
                rows_str = ['|' if random.randint(1,pr_ugly) == 1 else str(x)+'|*|' for x in rows]
            else:
                rows_str = [str(x)+'|*|' for x in rows]

            row_txt = ''.join(rows_str).rstrip('|*\n') + '|#|\n'

            final_txt += row_txt

        return(final_txt)
            

    #def fill_dict(self):
    #   return()

        


class Row:

    def __init__(self, nRow: int):
        self.gender = ['F' if random.random() < 0.6 else 'M' for _ in range(nRow)]
        self.zip = [fake.postcode() for _ in range(nRow)]

        self.rows = {
            'employee_code': [10000+i for i in range(nRow)]
            ,'last_name': [fake.last_name() for _ in range(nRow) ]
            ,'first_name': [fake.first_name_female() if i=='F' else fake.first_name_male() for i in self.gender]
            ,'middle_name': [fake.first_name_female() if i=='F' else fake.first_name_male() for i in self.gender]
            ,'name_suffix': [fake.suffix() for _ in range(nRow)]
            ,'gender': self.gender
            ,'department_code': [random.randint(11,99)*1000 for _ in range(nRow)]
            ,'date_of_hire': [fake.date() for _ in range(nRow)]
            ,'journaly_type': ['F' if random.random() < 0.7 else 'P' for _ in range(nRow)]
            ,'status_code': ['T' if random.random() < 0.5 else 'A' if random.random() < 0.90 else 'R' for _ in range(nRow)]
            ,'travel_status': ['Y' if random.random() < 0.4 else 'N' for _ in range(nRow)]
            ,'street': [fake.street_address() for _ in range(nRow)]
            ,'location': [fake.city() for _ in range(nRow)]
            ,'state': [states[random.randint(0,len(states)-1)] for _ in range(nRow)]
            ,'zip_code': self.zip
            ,'falseSTATUS': ['Y' if random.random() < 0.05 else 'N' for _ in range(nRow)]
            ,'NRSDate': [fake.date() for _ in range(nRow)]
            ,'birth_date': [fake.date() for _ in range(nRow)]
            ,'home_phone1': [random.randint(650,950) for _ in range(nRow)]
            ,'home_phone2': [random.randint(100,999) for _ in range(nRow)]
            ,'home_phone3': [random.randint(1000,9999) for _ in range(nRow)]
            ,'office_phone1': [random.randint(650,950) for _ in range(nRow)]
            ,'office_phone2': [random.randint(100,999) for _ in range(nRow)]
            ,'office_phone3': [random.randint(1000,9999) for _ in range(nRow)]
            ,'mobile_phone1': [random.randint(650,950) for _ in range(nRow)]
            ,'mobile_phone2': [random.randint(100,999) for _ in range(nRow)]
            ,'mobile_phone3': [random.randint(1000,9999) for _ in range(nRow)]
            ,'work_email': [fake.ascii_company_email() for _ in range(nRow)]
            }
















    













