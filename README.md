# Project 3: Office Relocation

## Process: 
1. Choose 3 Spanish cities that are popular in the gaming industry to query for locations.
2. Assign values to all requirements, based on employee value.
3. Write formulae to return the shortest distance for all requirements in the 3 cities.
4. Sum all distance values multiplied by requirement weight to determine the lowest proximity score.
5. Visualize results.

## 1. Determine Locations.

Given this map of all gaming companies globally, I have chosen the most gaming-populous cities to locate the spanish branch of my gaming company: Barcelona, Madrid, and Valencia.

https://gamedevmap.com/index.php?country=Spain&state=&city=&query=&type=

## 2. Assign Value to All Requirements.

Weight value of all employeees: Multiply salary (glassdoor avg) by number of employees in said position.

### Employees:
- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President

### Requirements:
- Design companies: Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- School: 30% of the company staff have at least 1 child.
- Startups: Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Starbucks: Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
- Airport: Account managers need to travel a lot.
- Club: Everyone in the company is between 25 and 40, give them some place to go party.
- Vegan restaurant: The CEO is vegan.
- Basketball Stadium: If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
- Dog Groomer: The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.

### Scrape Glassdoor for employee salaries:
- add employees to a dataframe.
- url glassdoor {employee name}.
- Web scrape each page for salary, add to df.
- add requirement locations to df.

## Employee Value Analysis
### Call me an American, but...
The most sensible proposition is to surround your business with a professional network. Having more businesses nearby to propogate more business: Startups first, and then design companies, as recommended by the salary scores of developers and designers. Schools are vital to 30% of the company and are deal-breakers for some fo the older, high-level executives. Then comes Starbucks for all the executives, which is not hard to find and useful by score. Clubs and other nightlife allow younger employees to propogate a company culture that will attract the interest of nearby companies. 

An airport is important for the account managers (a vital asset to the company) but everyone expects a 45 minute taxi ride from the airport for any city, so as long as the airport is within a certain radius the location is good. The stadium would rank lower, but several employees have chimed in about their interest in attending events with the maintenance man.

With a company of 87 people, the CEO is phasing out her office time to network with investors, explore new businesses, and spend time with her family. Her needs to have a vegan restaurant nearby are low, as we confirmed in our last 1:1. A dog Groomer ranked lowest because everyone loves Fido but it does not affect anyone in a significant manner, and dogs in Spain are notoriously ungroomed anyway.

The total score of all employees is 2,550, so group scores are calculated in fractions: 30% for schools (765), 20% for clubs (510), and 1% for the dog (25). The stadium was also boosted by 10% of the whole (250) because other employees also enjoy this location.

### Final results:
1. Startups (1185)
2. Design Companies (765)
3. Schools (765)
4. Starbucks (600)
5. Clubs (510)
6. Airport (500)
7. Stadium (275)
8. Vegan Eats (80)
9. Dog Groomer (25)

## 3. Query the Shortest Distances for All Employee Requirements.

### Process:
- Pass a list of potential office locations.
- Calculate the shortest ditance from each requirement for each potential office.

Dataframe structure: office_location, design_companies, school, startups, starbucks, airport, club, vegan_eat, stadium, groomer

## 4. Determine Proximity Score.

Weighted value of all requirements: Multiply weighted ranks by distance to each location to find the best possible new branch office in each city.

1. Startups (1185)
2. Design Companies (765)
3. Schools (765)
4. Starbucks (600)
5. Clubs (510)
6. Airport (500)
7. Stadium (275)
8. Vegan Eats (80)
9. Dog Groomer (25)

## 5. Visualize Results
See Analysis.ipynb