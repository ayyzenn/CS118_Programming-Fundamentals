# Your code for get_companies_names goes here
def get_companies_names(companies):
    new_list = []
    for company in companies:
        new_list.append(company["Company Name"])
    return new_list


# Your code for get_countries goes here
def get_countries(companies):
    new_dict = {}
    for company in companies:
        keys = list(new_dict)
        if company['Country'] in keys:
            count = new_dict.get(company['Country']) + 1
            new_dict[company['Country']] = count
        else:
            new_dict[company['Country']] = 1
        
    return new_dict


    
# Your code for get_companies goes here
def get_companies(companies,location):
    new_list = []
    for company in companies:
        if company.get("City")==location.get("city") and company.get("Country")==location.get("country"):
            new_list.append(company["Company Name"])
            
    if new_list == []:
        return None
    else:
        return new_list
            
    