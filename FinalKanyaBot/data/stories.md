## happy path
* greet
  - utter_greet

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy 

## affirm 1 
* affirm 
  - utter_happy 

## deny 1 
* deny 
  - custom_fallback

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot 

## period
* periods
  - utter_periods

## periods day
* periods_days
  - utter_periods

## stomach cramp
* stomach_pain
  - utter_cramps

## pills
* periods_pills
  - utter_pills

## precautions taken
* periods_precaution
  - utter_precaution

## periods pain
* back_pain
  - utter_backpain

## sanitary pads
* sanitary_pads
  - utter_pads

## sanitary disposal
* sanitary_pads_disposal
  - utter_pad_dispose

## sanitary hygiene
* sanitary_pad_hygiene
  - utter_pad_hygeine

## sanitary duration
* santinary_pads_durations
  - utter_pad_duration

## diaper ques
* silly_ques_periods
  - utter_silly

## cups menstrual
* menstrual_cups
  - utter_cups

## cups time
* cups_duration
  - utter_cup_dur

## periods tamp
* tampons
  - utter_tampons

## tamp dur
* tampons_duration
  - utter_tamp_dur 

## help path 1
* help 
  - utter_help 
* police
  - utter_police
  - utter_did_that_help 

## help path 2 
* help 
  - utter_help 
* gynecologist
  - utter_gynecologist 
  - utter_did_that_help 

## help path 3 
* gynecologist
  - utter_gynecologist 
  - utter_did_that_help   

## durperiods
* durperiods
  - utter_durperiods

## cyclegap
* cyclegap
  - utter_cyclegap

## periodslate
* lateperiods
  - utter_lateperiods

## nopain
* nopain
  - utter_nopainperiods

## lightperiods
* lessbleeding
  - utter_lessbleeding

## twiceperiods
* twiceperiods
  - utter_twiceperiods
