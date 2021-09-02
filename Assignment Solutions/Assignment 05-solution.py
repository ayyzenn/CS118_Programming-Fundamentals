def get_companies_names(companyList):
    companies = []
    
    for company in companyList:
        companies.append(company['Company Name'])
    
    return companies


def get_countries(companyList):
    countryDict = {}
    
    countries = []
    
    for company in companyList:
        if not company['Country'] in countries:
            countries.append(company['Country'])
            countryDict[company['Country']] = 1
            
        else:
            countryDict[company['Country']] += 1
    
    return countryDict


def get_companies(companyList, location):
    companies = []
    
    for company in companyList:
        if company['Country'] == location['country'] and company['City'] == location['city']:
            companies.append(company['Company Name'])
            
    if companies == []:
        return None
    
    return companies


if __name__ == '__main__':
    location = {'city': 'Tirana', 'country': 'Albania'}
    companies = [    {
    "Company Name": "Publer",
    "Company Moto": "Your Social Media Superhero",
    "City": "Tirana",
    "Country": "Albania",
    "Contact": {
        "Phone Number": "",
        "Email": "support@publer.me",
        "Website": "https://publer.io"
    },
    "Social Accounts": {
        "Facebook": "http://www.facebook.com/PublerNation",
        "Twitter": "https://twitter.com/PublerNation",
        "LinkedIn": "https://www.linkedin.com/company/publer-app"
    }
},
{
    "Company Name": "Communication Progress",
    "Company Moto": "Communication Progress Shpk (1998) is in the ICT industry in Albania by providing latest technology solutions & services to SME's & MNC's",
    "City": "Tiran\u00eb",
    "Country": "Albania",
    "Contact": {
        "Phone Number": "+355 4 241 3901",
        "Email": "cp@commprog.com",
        "Website": "http://www.commprog.com"
    },
    "Social Accounts": {
        "Facebook": "https://www.facebook.com/CommunicationProgress",
        "Twitter": "https://twitter.com/commprog",
        "LinkedIn": "https://www.linkedin.com/company/communication-progress"
    }
},
{
    "Company Name": "Sondor Travel",
    "Company Moto": "Sondor Travel is an adventure travel company that organizes tours in Albania, Macedonia, Kosovo, and Montenegro.",
    "City": "Tirana",
    "Country": "Albania",
    "Contact": {
        "Phone Number": "+355 4 22 25 063",
        "Email": "incoming@sondortravel.com",
        "Website": "http://www.sondortravel.com"
    },
    "Social Accounts": {
        "Facebook": "http://www.facebook.com/pages/Sondor-Travel/214092621953924",
        "Twitter": "http://twitter.com/SondorTravel",
        "LinkedIn": "http://www.linkedin.com/company/sondor-travel"
    }
},
{
    "Company Name": "Reig Capital Group",
    "Company Moto": "Reig Capital Group is a family office that engages in managing the investments of the Reig Moles family.",
    "City": "Andorra La Vella",
    "Country": "Andorra",
    "Contact": {
        "Phone Number": "(376) 874-050_",
        "Email": "info@reigcapital.com",
        "Website": "http://www.reigcapital.com/en/home.html"
    },
    "Social Accounts": {
        "Facebook": "",
        "Twitter": "",
        "LinkedIn": "http://www.linkedin.com/company/reig-capital"
    }
}]
    
    print(get_companies_names(companies))
