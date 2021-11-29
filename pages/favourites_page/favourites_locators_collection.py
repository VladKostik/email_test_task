class FavouritesLocatorsCollection:
    def __init__(self):
        self.__favourites_counter_at_FP_css = (
            '#root > div > div > div > div:nth-child(1) > div > div:nth-child(2) >'
            ' div.style__ek-box__5DtwLz.style__ek-box_position_relative__3gWtyG.'
            'style__ek-box_width_1-1__mnXboa.style__ek-box_background_white__FLVI1B > '
            'div > div > div.style__ek-box__5DtwLz.style__ek-box_margin-left_xs__3FTYmy > '
            'div > div:nth-child(1) > div > a > div > div > span'
        )

    @property
    def favourites_counter_at_fp(self):
        return self.__favourites_counter_at_FP_css
