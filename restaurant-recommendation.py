import tkinter.filedialog
import readrestaurant
from operator import itemgetter
file_name=tkinter.filedialog.askopenfilename()
thisfile=open(file_name,"r")



def recommend(thisfile,price,cuisines_list):
    """(file open for reading,str,list of str)->list of list of str

    find restaurants in file that are in the price range and serve the cuisine
    in the cuisine list.Return a list of lists of the form
    [rating%,resturant name],sorted by rating%.
    >>>recommend(thisfile,"$","Pub Food")
    the final results is [('American Grill', 80.0), ('Deep Fried Everything', 52.0)]
    """ 
    
    result={}
    final_result={}
    result_sorted={}
    #Read the file and build the data structures.
    #-a dic of{restaurant name:rating%}
    #-a dic of {price: list of restaurant names}
    #-a dic of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = readrestaurant.read_restaurant(thisfile)
    print(name_to_rating)
    print(price_to_names)
    print(cuisine_to_names)
    #get the list of restuarant names that in this price range
    names_matching_price=price_to_names[price]
    print(price)
    print (names_matching_price)
    
    #get the list of restuarant names that server the cuisine
    names_matching_cuisine=cuisine_to_names[cuisines_list]
    print(names_matching_cuisine)
    #check get a new list of restuarant names that both in names_matching_price and names
    #_matching_cuisine
    for name in names_matching_price:
        if name in names_matching_cuisine:
            
            #get new dic of result{"name":"rating"}
            result[name]=float(name_to_rating[name])
            #get big dic of results,could use sorted method do sorting on dic, list item desn't have
            #items()method
            final_result=dict(list(final_result.items())+list(result.items()))
    #should get the new list of resturant names and its rating ,do the sorting
    print("the result is",final_result)
    result_sorted=filter(final_result)
    print ("the final results is",result_sorted)

def filter(dic):
    """(dic)->list
    >>>final_result={"Deep Fried Everything":52.0,"American Grill":80.0}
      [('American Grill', 80.0), ('Deep Fried Everything', 52.0)]
    """#sort dic based on the value instead of the key ,return a list
    result_acs=sorted(dic.items(),key=itemgetter(1))
    result_dec=result_acs[::-1]
    
    return(result_dec)
            

