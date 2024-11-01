from text_parser import get_jobs, get_details
import csv

def write_csv(func): 
   with open('result.csv', mode='w', newline='', encoding='utf-8') as f:
        '''
            With this function, I'll write a csv with such structure:
            Columns:
                1. Company: company name which posted the job listing
                2. Position: position that each company needed
                3. Skills: skills associated with each company and position
            
            The approach here is write per row. First row is dedicated for column name. 
            N-th column are dedicated for each entity.
        '''
        writer = csv.writer(f)

        listing_details = func
        writer.writerow(['company', 'position', 'skills'])

        for i in listing_details:
            skills = ', '.join(i['skills'])
            writer.writerow([i['company'], i['position'], skills])
        
        print('File is being successfully writen')

if __name__ == "__main__":
    get_jobs_func = get_jobs()
    get_details_func = get_details(get_jobs_func)
    write_csv(get_details_func)