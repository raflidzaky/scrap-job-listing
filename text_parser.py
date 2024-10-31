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
    
def write_txt(job_input:str): 
    with open('result.txt', 'w') as f:
    # We want to find company name inside the job variable
        for job in job_input:
            comp_name = job.find_all('h3', class_='joblist-comp-name')
            list_comp = []

            for comp in comp_name:
                list_comp.append(comp.text.strip())
            # print(comp_name.text.strip())

            # Parse the position
            position_listing = job.find('h2', class_='heading-trun')
            if position_listing:
                position_text  = position_listing.text.strip()
                position_part  = ' '.join(position_text.split()[:2])
                if ':' in position_part:
                    position_clean = position_part.replace(':', '')
                

            # I also want to find the skills needed
            skill_section = job.find('div', class_='more-skills-sections')

            if skill_section:
                skills = skill_section.find_all('span')

            list_skill = []
            for skill in skills:
                if '** ' in skill.text:
                    cleaned_skill = skill.text.replace('** ', '')
                    list_skill.append(cleaned_skill.strip())
                elif ' **' in skill.text:
                    cleaned_skill = skill.text.replace(' **', '')
                    list_skill.append(cleaned_skill.strip())
                else:
                    list_skill.append(skill.text.strip())
        
            # Since write does not accept list input,
            # I have to join it as a string
            f.write("Companies:\n")
            f.write("\n".join(list_comp) + "\n")  # Join the list into a single string with line breaks
            f.write(position_clean + "\n")
            f.write("\n")
            f.write("Skills:\n")

            for i, s in enumerate(list_skill):
                f.write(f"{i+1}. {s}\n")
            f.write("========\n\n")

    print('File is being successfully written')
   

if __name__ == "__main__":
    write_txt(get_jobs())