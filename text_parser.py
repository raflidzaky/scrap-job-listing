from bs4 import BeautifulSoup
import requests

def get_jobs():
    # Real website requires requesting process to scrape info
    # .get method only return request status.
    # If the response is good (200), we can "scrape it"
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=data&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    # Since there are multiple pages, it will return from first page only
    # location_text = soup.find_all('li', class_='srp-zindex location-tru')
    # for loc in location_text:
    #   print(loc.text)

    # Get the job listing first (from each "data" jobs query)
    job_cat = soup.find('ul', class_='new-joblist')
    jobs = job_cat.find_all('li', class_='clearfix job-bx wht-shd-bx')

    return jobs

def get_details(job_input:str): 
    '''
        This func will get a details from each job listing, such as skillset, position, and firms.
        Input: jobs (from get_jobs func) 
        Output: Job details as a return (list data structure)
    '''

    # Initialize variables as returns
    job_details = [] # It will hold every details from each company's details

    # The details of each individual company will be hold in a dictionary. The dictionary will map
    # company name, company's position needed, and skills needed.
    # This is done because I need to track the skills that belonging to each company name and position
    # Appending altogether within a list will be extremely hard to track.
    # Each company's details (n-company) will be put in job_details' list (n-index)

    for job in job_input:
        '''
        =====================================================================================
            This func will iterate each job listing to get its details. 
            TASK 1: Find all of the company name and iterate it to put within the list
        =====================================================================================
        '''

        # Initialize job info (or details) per iteration
        job_info = {
            'company': '',
            'position': '',
            'skills': []
        }

        # Find the company name
        comp_name = job.find_all('h3', class_='joblist-comp-name')
        for comp in comp_name:
            job_info['company'] = comp.text.strip()
    
            '''
            =====================================================================================
                TASK 2: Find all of the position from each company. 
                Since I take the position within company name iteration, I will no need to do any
                iteration to get each position associated from job listing. 
            =====================================================================================
            '''
            # Parse the position
            position_listing = job.find('h2', class_='heading-trun')
            if position_listing:
                # If there is position posted, get the text
                position_text  = position_listing.text.strip()
                position_part  = ' '.join(position_text.split()[:2])
                if ':' in position_part:
                    job_info['position'] = position_part.replace(':', '')
            else:
                # Otherwise, just continue it
                continue

            '''
            =====================================================================================
                TASK 3: Find all of the skills related to each position from each company. 
                Since I take the position within company name iteration, I will no need to do any
                iteration to get each position associated from job listing. 
            =====================================================================================
            '''
            skill_section = job.find('div', class_='more-skills-sections')

            # If there exists skill-section from job listing, find "skills" component
            if skill_section:
                skills = skill_section.find_all('span')

            # Get each skills (multiple skills) and append it to the list. 
                for skill in skills:
                    cleaned_skill = skill.text.strip().replace('** ', '').replace(' **', '')
                    job_info['skills'].append(cleaned_skill)  # Append each cleaned skill
            
            # Append each detail to job_details' list
            job_details.append(job_info)
            
    return job_details