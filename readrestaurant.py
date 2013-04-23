def read_restaurant(file):
    """(file)->(dic,dic,dic)
return a tuple of three dictionaries based on the information in the file
precodinton: the content starts from second line
restaurant name   rating    cost    cusine
Georgie Porgie
87
$$$
Canadian,Pub Food

Queen St.Cafe
82
$
Malaysian, Thai

Dumplings R Us
71
$
Chinese

Mexican Grill
85
$$
Mexican

Deep Fried Everything
52
$
Pub Food

>>>name_to_ratings={'Mexican Grill': '85', 'Georgie Porgie': '87', '
Dumplings R Us': '71', 'Deep Fried Everything': '52', 'Queen St.Cafe': '82'}
>>>price_to_names={'$': ['Queen St.Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
'$$$': ['Georgie Porgie'], '$$': ['Mexican Grill'], '$$$$': []}

>>cuisine_to_names={'Thai': ['Queen St.Cafe'], 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
'Mexican': ['Mexican Grill'], 'Canadian': ['Georgie Porgie'],
'Chinese': ['Dumplings R Us'], 'Malaysian': ['Queen St.Cafe']}


"""

    name_to_rating={}
    price_to_names={"$":[],"$$":[],"$$$":[],"$$$$":[]}
    cuisine_to_names={}
    
    line=file.readline()
    #skip over the header
    while line!="\n":
        line=file.readline()
        
    line=file.readline()
    while line !="":
        #get the name
        name=line.strip()
        line=file.readline()
        #get the rating
        name_to_rating[name]=line.strip()
        line=file.readline()
        price_tag=line.strip()
        #get the price range and assosicated name
        price_to_names[price_tag].append(name)
        line=file.readline()
        #get the cuisine name
        
        cuisine_name_list=line.strip().split(",")
        #check each cuisine_name if listed
        for item in cuisine_name_list:
            
            
        #if the cuisine name is not listed
            if not(item in cuisine_to_names):
                cuisine_to_names[item]=[name]
                
            else:
                cuisine_to_names[item].append(name)
            
        line=file.readline()
        line=file.readline()
    return(name_to_rating,price_to_names,cuisine_to_names)
   
        
        
        
   
