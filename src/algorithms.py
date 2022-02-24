import itertools
def get_file_specs(clients):
    
    dc = {}
    
    for c in clients:
        likes, dislikes = c

        for i in likes:
            if i not in dc:
                dc[i] = {'isliked': 1, 'isdisliked':0}
            else:
                dc[i]['isliked'] += 1

        for i in dislikes:
            if i not in dc:
                dc[i] = {'isliked': 0, 'isdisliked':1}
            else:
                dc[i]['isdisliked'] += 1
    
    # file specifications
    total_ingredients = len(dc.keys())
    total_clients = len(clients)    
    print(f'Total ingredients: {total_ingredients}, total clients: {total_clients}')
    
    dc = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1]['isliked'],reverse=True)}
    ingredients = list(dc.keys())
    
    total_non_disliked = 0
    total_moredisliked = 0
    for i in ingredients:
        if dc[i]['isdisliked'] == 0:
            total_non_disliked += 1
        if dc[i]['isliked'] < dc[i]['isdisliked']:
            total_moredisliked += 1
    
    print(f'Total non disliked ingredients: {total_non_disliked}')
    print(f'Total ingredients that are more disliked than liked: {total_moredisliked}')
    
    SHOW_INGREDIENTS = 3
    print('Most Liked Ingredients')
    for i in ingredients[0:SHOW_INGREDIENTS]:
        print(f'\t{i}: {dc[i]}')
        
    dc = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1]['isdisliked'],reverse=True)}
    ingredients = list(dc.keys())
    print('Most Disliked Ingredients')
    for i in ingredients[0:SHOW_INGREDIENTS]:
        print(f'\t{i}: {dc[i]}')
        
    return 

def get_power_set(myset):
    all_combinations = itertools.chain(*[itertools.combinations(myset,i+1) for i,_ in enumerate(myset)])
    return list(all_combinations)

def evaluate_solution(clients, ingredients):
    """
    Takes as input the list of clients with their preferences and based on the selected ingredients
    returns the number of satisfied customers.
    """
    total_clients = 0
    
    for c in clients:
        likes, dislikes = c
        if likes.intersection(ingredients) == likes and not dislikes.intersection(ingredients):
            total_clients += 1
    
    return total_clients

def brute_force_algorithm(clients):
    """
    Produces all possible subsets and returns the best solution. 
    Could be used for instances up to rouhgly 30 ingredients
    """
    print('Applying brute force algorithm')
    ingredients = set()
    for c in clients:
        likes, dislikes = c
        ingredients = ingredients.union(likes.union(dislikes))
    power_set = get_power_set(ingredients)
    power_set.append(tuple())
    print(f'Total {len(power_set)} brute force cases.')
    max_clients, max_case = 0, set()
    for subset in power_set:
        total_clients = evaluate_solution(clients, subset)
        if total_clients > max_clients:
            max_clients = total_clients
            max_case = subset
            
    print(f'Set {max_case} maximizes total clients to {max_clients}')
    return max_case

def get_ingredient_preferences(clients):
    dc = {}
    for c in clients:
        likes, dislikes = c

        for i in likes:
            if i not in dc:
                dc[i] = {'isliked': 1, 'isdisliked':0}
            else:
                dc[i]['isliked'] += 1

        for i in dislikes:
            if i not in dc:
                dc[i] = {'isliked': 0, 'isdisliked':1}
            else:
                dc[i]['isdisliked'] += 1
    return dc

def greedy_search(clients):
    """
    Add all possible ingredients and remove them one by one in decreasing order to how many people dislike them
    """
    print('Applying greedy search')

    dc = get_ingredient_preferences(clients)
    dc = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1]['isdisliked'],reverse=True)}
    disliked = list(dc.keys())

    ingredients = set(disliked)
        
    current_clients = evaluate_solution(clients, ingredients)
    best_solution = ingredients
    best_clients = current_clients
    i = 0
    while i < len(disliked):
        if i> 0 and i % 1000 == 0:
            print(i)
        ingredients = ingredients - set([disliked[i]])
        current_clients = evaluate_solution(clients, ingredients)
        if current_clients > best_clients:
            best_clients = current_clients
            best_solution = ingredients
        i = i + 1
    print(f'Greedy search found best solution: {best_clients} with {len(best_solution)} total ingredients')
    return best_solution

def incremental_greedy_search(clients):
    """
    Add all ingredients that are not disliked by anyone and add one by one all the ingredients
    in decreasing order of their likeness
    """
    print('Applying incremental greedy search')
    
    dc = get_ingredient_preferences(clients)
    dc = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1]['isliked'],reverse=True)}    
    liked = list(dc.keys())
    
    ingredients = set([k for k in dc.keys() if dc[k]['isdisliked'] == 0])
    print(f"Starting with {len(ingredients)} total ingredients")
    
    current_clients = evaluate_solution(clients, ingredients)
    best_solution = ingredients
    best_clients = current_clients
    i = 0
    while i < len(liked):
        if i> 0 and i % 1000 == 0:
            print(i)
        ingredients = ingredients.union(set([liked[i]]))
        current_clients = evaluate_solution(clients, ingredients)
        if current_clients > best_clients:
            best_clients = current_clients
            best_solution = ingredients
        i = i + 1
    print(f'Incremental greedy search found best solution: {best_clients} with {len(best_solution)} total ingredients')
    return best_solution
