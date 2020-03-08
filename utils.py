

class Paginator:
    def __init__(self):
        self.page_listing = []
        self.current_page = 1
        self.max_page = 1

    def set_current_page(self, page_number):
        self.current_page = page_number

    def set_max_page(self, page_number):
        self.max_page = page_number

    def get_page_range(self):
        if self.max_page == 1:
            self.page_listing.append(1)
        elif self.max_page < 8:
            for x in range(1, 8):
                self.page_listing.append(x)
        else:
            max_page_tracker = 6
            lower_bound = self.current_page - 3

            if lower_bound < 1:
                lower_bound = 1

            max_page_tracker -= self.current_page - lower_bound
            upper_bound = self.current_page + max_page_tracker

            if upper_bound > self.max_page:
                upper_bound = self.max_page

            for x in range(lower_bound, upper_bound):
                self.page_listing.append(x)

        return self.page_listing
