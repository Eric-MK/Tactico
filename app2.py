import pandas as pd
import pickle

def getData():
    with open('outfield.pkl', 'rb') as file:
        player_df = pd.DataFrame(pickle.load(file))
    with open('player_ID.pickle', 'rb') as file:
        player_ID = pickle.load(file)
    with open('engine.pickle', 'rb') as file:
        engine = pickle.load(file)
    
    with open('gk.pkl', 'rb') as file:
        gk_df = pd.DataFrame(pickle.load(file))
    with open('gk_ID.pickle', 'rb') as file:
        gk_ID = pickle.load(file)
    with open('gk_engine.pickle', 'rb') as file:
        gk_engine = pickle.load(file)
    
    return player_df, player_ID, engine, gk_df, gk_ID, gk_engine


def getRecommendations(player_type, query, count, comparison, league):
    player_df, player_ID, engine, gk_df, gk_ID, gk_engine = getData()
      
    # Check if the player in the query matches the player_type
    if player_type == 'Outfield players' and query not in player_ID:
        return {"error": f"Player '{query}' is not an Outfield player"}
    elif player_type == 'Goal Keepers' and query not in gk_ID:
        return {"error": f"Player '{query}' is not a Goal Keeper"}


    if player_type == 'Outfield players':
        df, ID, engine = player_df, player_ID, engine
    else:
        df, ID, engine = gk_df, gk_ID, gk_engine

    # Access the 'engine' dictionary using the query
    try:
        metric = engine[query]
    except KeyError:
        return {"error": f"Player '{query}' not found"}
    
    df_res = df.iloc[:, [1, 3, 5, 6, 11,-1]].copy() if player_type == 'Outfield players' else df.iloc[:, [1, 3, 5, 6, 11]].copy()
    df_res['Player'] = list(ID.keys())
    df_res.insert(1, 'Similarity', metric)
    df_res = df_res.sort_values(by=['Similarity'], ascending=False)
    metric = [str(num) + '%' for num in df_res['Similarity']]
    df_res['Similarity'] = metric
    df_res = df_res.iloc[1:, :]

    if comparison == 'Same position' and player_type == 'Outfield players':
        q_pos = list(df[df['Player'] == query.split(' (')[0]]['Pos'])[0]
        df_res = df_res[df_res['Pos'] == q_pos]

    if league != 'All':
        df_res = df_res[df_res['Comp'] == league]

    df_res = df_res.head(count)
    
    return df_res
