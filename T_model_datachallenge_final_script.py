import pickle
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# load file to score
df = pd.read_csv('data_challenge_2023.csv',index_col=0)
#features_cols = [x for x in df.columns if x not in ['home_win_flag', 'draw_flag', 'away_win_flag', 'div','season','match_id']]

features_cols = ['odds_home_team_win',
 'odds_draw',
 'odds_away_team_win',
 'home_team_match_nr',
 'home_team_goal_roll1_sum',
 'home_team_goal_roll2_sum',
 'home_team_goal_roll3_sum',
 'home_team_goal_roll4_sum',
 'home_team_opponents_goal_roll1_sum',
 'home_team_opponents_goal_roll2_sum',
 'home_team_opponents_goal_roll3_sum',
 'home_team_opponents_goal_roll4_sum',
 'home_team_shot_roll1_sum',
 'home_team_shot_roll2_sum',
 'home_team_shot_roll3_sum',
 'home_team_shot_roll4_sum',
 'home_team_opponents_shot_roll1_sum',
 'home_team_opponents_shot_roll2_sum',
 'home_team_opponents_shot_roll3_sum',
 'home_team_opponents_shot_roll4_sum',
 'home_team_shot_on_target_roll1_sum',
 'home_team_shot_on_target_roll2_sum',
 'home_team_shot_on_target_roll3_sum',
 'home_team_shot_on_target_roll4_sum',
 'home_team_opponents_shot_on_target_roll1_sum',
 'home_team_opponents_shot_on_target_roll2_sum',
 'home_team_opponents_shot_on_target_roll3_sum',
 'home_team_opponents_shot_on_target_roll4_sum',
 'home_team_fault_roll1_sum',
 'home_team_fault_roll2_sum',
 'home_team_fault_roll3_sum',
 'home_team_fault_roll4_sum',
 'home_team_opponents_fault_roll1_sum',
 'home_team_opponents_fault_roll2_sum',
 'home_team_opponents_fault_roll3_sum',
 'home_team_opponents_fault_roll4_sum',
 'home_team_corner_roll1_sum',
 'home_team_corner_roll2_sum',
 'home_team_corner_roll3_sum',
 'home_team_corner_roll4_sum',
 'home_team_opponents_corner_roll1_sum',
 'home_team_opponents_corner_roll2_sum',
 'home_team_opponents_corner_roll3_sum',
 'home_team_opponents_corner_roll4_sum',
 'home_team_yellow_card_roll1_sum',
 'home_team_yellow_card_roll2_sum',
 'home_team_yellow_card_roll3_sum',
 'home_team_yellow_card_roll4_sum',
 'home_team_opponents_yellow_card_roll1_sum',
 'home_team_opponents_yellow_card_roll2_sum',
 'home_team_opponents_yellow_card_roll3_sum',
 'home_team_opponents_yellow_card_roll4_sum',
 'home_team_red_card_roll1_sum',
 'home_team_red_card_roll2_sum',
 'home_team_red_card_roll3_sum',
 'home_team_red_card_roll4_sum',
 'home_team_opponents_red_card_roll1_sum',
 'home_team_opponents_red_card_roll2_sum',
 'home_team_opponents_red_card_roll3_sum',
 'home_team_opponents_red_card_roll4_sum',
 'home_team_point_roll1_sum',
 'home_team_point_roll2_sum',
 'home_team_point_roll3_sum',
 'home_team_point_roll4_sum',
 'home_team_expected_point_roll1_sum',
 'home_team_expected_point_roll2_sum',
 'home_team_expected_point_roll3_sum',
 'home_team_expected_point_roll4_sum',
 'odds_home_team_win_roll1_mean',
 'odds_home_team_win_roll2_mean',
 'odds_home_team_win_roll3_mean',
 'odds_home_team_win_roll4_mean',
 'odds_home_team_draw_roll1_mean',
 'odds_home_team_draw_roll2_mean',
 'odds_home_team_draw_roll3_mean',
 'odds_home_team_draw_roll4_mean',
 'odds_home_team_defeat_roll1_mean',
 'odds_home_team_defeat_roll2_mean',
 'odds_home_team_defeat_roll3_mean',
 'odds_home_team_defeat_roll4_mean',
 'home_team_point_mean',
 'home_team_expected_point_mean',
 'away_team_match_nr',
 'away_team_goal_roll1_sum',
 'away_team_goal_roll2_sum',
 'away_team_goal_roll3_sum',
 'away_team_goal_roll4_sum',
 'away_team_opponents_goal_roll1_sum',
 'away_team_opponents_goal_roll2_sum',
 'away_team_opponents_goal_roll3_sum',
 'away_team_opponents_goal_roll4_sum',
 'away_team_shot_roll1_sum',
 'away_team_shot_roll2_sum',
 'away_team_shot_roll3_sum',
 'away_team_shot_roll4_sum',
 'away_team_opponents_shot_roll1_sum',
 'away_team_opponents_shot_roll2_sum',
 'away_team_opponents_shot_roll3_sum',
 'away_team_opponents_shot_roll4_sum',
 'away_team_shot_on_target_roll1_sum',
 'away_team_shot_on_target_roll2_sum',
 'away_team_shot_on_target_roll3_sum',
 'away_team_shot_on_target_roll4_sum',
 'away_team_opponents_shot_on_target_roll1_sum',
 'away_team_opponents_shot_on_target_roll2_sum',
 'away_team_opponents_shot_on_target_roll3_sum',
 'away_team_opponents_shot_on_target_roll4_sum',
 'away_team_fault_roll1_sum',
 'away_team_fault_roll2_sum',
 'away_team_fault_roll3_sum',
 'away_team_fault_roll4_sum',
 'away_team_opponents_fault_roll1_sum',
 'away_team_opponents_fault_roll2_sum',
 'away_team_opponents_fault_roll3_sum',
 'away_team_opponents_fault_roll4_sum',
 'away_team_corner_roll1_sum',
 'away_team_corner_roll2_sum',
 'away_team_corner_roll3_sum',
 'away_team_corner_roll4_sum',
 'away_team_opponents_corner_roll1_sum',
 'away_team_opponents_corner_roll2_sum',
 'away_team_opponents_corner_roll3_sum',
 'away_team_opponents_corner_roll4_sum',
 'away_team_yelllow_card_roll1_sum',
 'away_team_yelllow_card_roll2_sum',
 'away_team_yelllow_card_roll3_sum',
 'away_team_yelllow_card_roll4_sum',
 'away_team_opponents_yellow_card_roll1_sum',
 'away_team_opponents_yellow_card_roll2_sum',
 'away_team_opponents_yellow_card_roll3_sum',
 'away_team_opponents_yellow_card_roll4_sum',
 'away_team_red_card_roll1_sum',
 'away_team_red_card_roll2_sum',
 'away_team_red_card_roll3_sum',
 'away_team_red_card_roll4_sum',
 'away_team_opponents_red_card_roll1_sum',
 'away_team_opponents_red_card_roll2_sum',
 'away_team_opponents_red_card_roll3_sum',
 'away_team_opponents_red_card_roll4_sum',
 'away_team_point_roll1_sum',
 'away_team_point_roll2_sum',
 'away_team_point_roll3_sum',
 'away_team_point_roll4_sum',
 'away_team_expected_point_roll1_sum',
 'away_team_expected_point_roll2_sum',
 'away_team_expected_point_roll3_sum',
 'away_team_expected_point_roll4_sum',
 'odds_away_team_win_roll1_mean',
 'odds_away_team_win_roll2_mean',
 'odds_away_team_win_roll3_mean',
 'odds_away_team_win_roll4_mean',
 'odds_away_team_draw_roll1_mean',
 'odds_away_team_draw_roll2_mean',
 'odds_away_team_draw_roll3_mean',
 'odds_away_team_draw_roll4_mean',
 'odds_away_team_defeat_roll1_mean',
 'odds_away_team_defeat_roll2_mean',
 'odds_away_team_defeat_roll3_mean',
 'odds_away_team_defeat_roll4_mean',
 'away_team_point_mean',
 'away_team_expected_point_mean']
def create_home_win_flag_model_db(df,features_cols):
    p_home_win = pickle.load(open('pipe_home_win_base_model_3.p', "rb"))
    val_df = pd.DataFrame(df['match_id'])
    val_df.columns = ['match_id']
    val_df[['home_win_p0','home_win_p1']] = p_home_win.predict_proba(df[features_cols])
    return val_df[['match_id','home_win_p1']]

def create_draw_flag_model_db(df,features_cols):
    p_draw =     pickle.load(open('pipe_p_draw_base_model_3.p', "rb"))
    val_df = pd.DataFrame(df['match_id'])
    val_df.columns = ['match_id']
    val_df[['draw_p0','draw_p1']] = p_draw.predict_proba(df[features_cols])
    return val_df[['match_id','draw_p1']]

def create_away_win_flag_model_db(df,features_cols):
    p_away_win =  pickle.load(open('pipe_p_away_win_base_model_3.p', "rb"))
    val_df = pd.DataFrame(df['match_id'])
    val_df.columns = ['match_id']
    val_df[['away_win_p0','away_win_p1']] = p_away_win.predict_proba(df[features_cols])
    return val_df[['match_id','away_win_p1']]

def write_out_final_results(final_results_db,team_name='T-Model'):

    final_results_db[['match_id' , 'home_win_p1', 'draw_p1', 'away_win_p1']].to_csv(team_name+'.csv',encoding='utf-8')

home_win_flag_model_db = create_home_win_flag_model_db(df,features_cols)
draw_flag_model_db     = create_draw_flag_model_db(df,features_cols)
away_win_flag_model_db = create_away_win_flag_model_db(df,features_cols)

final_results_db = home_win_flag_model_db.merge(draw_flag_model_db,how='inner',on='match_id').merge(away_win_flag_model_db,how='inner',on='match_id')

write_out_final_results(final_results_db,team_name='T-Model')