from text_parser import get_jobs, get_details

def write_txt(func): 
    '''
        This func will write the details over a txt file, using with open functionalities
    '''
    with open('result.txt', 'w') as f:    
        listing_details = func

        for i in listing_details:
            f.write("Companies:\n")
            f.write(i['company'] + "\n")  # Join the list into a single string with line breaks

            f.write("\nPositions:\n")
            f.write(i['position'] + "\n")
            
            f.write("\nSkills:\n")
            for i, s in enumerate(i['skills']):
                f.write(f"{i+1}. {s}\n")
            f.write("============================================\n\n")
    print('File is being successfully written')
   

if __name__ == "__main__":
    get_jobs_func = get_jobs()
    get_details_func = get_details(get_jobs_func)
    write_txt(get_details_func)