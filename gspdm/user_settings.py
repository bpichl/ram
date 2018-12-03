# coding=utf-8
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)


class Constants(BaseConstants):

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 DESIGN SETUP                                                  #
    #                                                                                                               #
    # ============================================================================================================= #

    # NUMBER OF PLAYERS =========================================================================== #
    #   Please specify how many players per market will participate.                                #
    players_per_group = 3

    # BIDDING CURRENCY ENDOWMENT ================================================================== #
    #   Specify the amount of fictional currency units that the players distribute over resources.  #
    endowment = 100

    # VALUATION VECTORS =========================================================================== #
    #   Different player types can have different valuation vectors for resources. Set the          #
    #   valuation vectors for each type and resource (Please keep in mind that the number of value  #
    #   vectors has to be a number that is completely divisible by the variable                     #
    #   "players_per_group"). E.g., if the market has three types and six resources, set the first  #
    #   six values within the list for a type to a number. Please stick to the scheme below.        #
    #   This app supports up to 10 types and 10 resources. Types are generated by id_in_group.      #
    #   This means that if you have 4 players and 2 types, players 1 and 2 are Type1, and           #
    #   players 3 and 4 are Type2.                                                                  #
    valuations_t1 = [10, 20, 30]
    valuations_t2 = [20, 10, 30]
    valuations_t3 = [30, 20, 10]
    #   Set vectors for multiple types in the following way:
    #       valuations_t2 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       valuations_t3 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       valuations_t4 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       ...

    # RESOURCE CAPACITIES ========================================================================= #
    #   Set the quota of players that each resource can carry. Fill in as many number as in the     #
    #   valuation vectors.                                                                          #
    capacities = [1, 2, 1]

    # NR. OF RESOURCES PER PLAYER ================================================================= #
    #   Specify the number of resources that every player can be potentially allocated to. This     #
    #   number has to be constant across all players in the market.                                 #
    s_len = 3

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 APPEARANCE SETTINGS                                           #
    #                                                                                                               #
    # ============================================================================================================= #

    # FRAMING ===================================================================================== #
    #   Here you can choose between a neutral framing (participants/resources) and a application    #
    #   framing (students/courses).                                                                 #
    application_framing = False

    # SHOW INSTRUCTIONS =========================================================================== #
    #   Should the instructions for the mechanism be included?                                      #
    instructions = True

    # SHOW EXAMPLE IN INSTRUCTIONS ================================================================ #
    #   If "instructions = True", should the instructions also include a minimal example of the     #
    #   mechanism in place?                                                                         #
    instructions_example = False

    # SHOW POINTS LEFT ============================================================================ #
    #   If "show_counter" is set to "True", players will have a live counter on the decision page   #
    #   that indicates how many fictional currency units are left to bid.                           #
    show_counter = True

    # SHOW CONFIRM BUTTON ========================================================================= #
    #   If "confirm_button" is set to "True", players will have to confirm their inputs made on     #
    #   Decision.html to. This can be used to avoid accidental submission of the page.              #
    confirm_button = True

    # SHOW RESULTS ================================================================================ #
    #   Should a results screen be included? The results screen shows a summary of results of the   #
    #   market (i.e., preferences submitted, bids made, clearing bids, allotted resources), and the #
    #   final payoff for the player.                                                                #
    results = True

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 INFORMATION SETTINGS                                          #
    #                                                                                                               #
    # ============================================================================================================= #

    # SHOW CAPACITIES ============================================================================= #
    #   If set to "True", the quota specified in "capacities" above will be shown to players on the #
    #   decision screen and in the instructions.                                                    #
    show_capacities = True

    # SHOW TYPES ================================================================================== #
    #   If "show_types" is set to "True", players will have a hint on the decision page and in the  #
    #   instructions that there are different types of players in the market. Only works if         #
    #   multiple type vectors have been specified above.                                            #
    show_types = False

    # SHOW OTHERS' VALUATIONS ===================================================================== #
    #   Should players see the other players' valuation profiles and on the decision page? Only     #
    #   works if "show_types" has been set to "True" above.                                         #
    show_valuations = False

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 MISCELLANEOUS SETTINGS                                        #
    #                                                                                                               #
    # ============================================================================================================= #

    # ENFORCE BINDING CONSTRAINT ================================================================== #
    #   If set to "True", players are forced to use up all bidding points specified in "endowment". #
    enforce_binding = False

    ####################################################################################################################
    ####################################################################################################################
    # ------------------------------              DO NOT MODIFY BELOW HERE              ------------------------------ #
    ####################################################################################################################
    ####################################################################################################################

    capacities = [i for i in capacities if i is not None]
    nr_courses = len(capacities)

    valuations_list = ["valuations_t" + str(i) for i in range(1, 11)]
    valuations_raw = []
    for i in valuations_list:
        if i in locals():
            valuations_raw.append(locals()[i])

    valuations = []
    for i in valuations_raw:
        valuations.append([j for j in i if j is not None])

    nr_types = len(valuations)

    name_in_url = "gspdm"
    num_rounds = 1
