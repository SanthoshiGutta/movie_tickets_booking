from myexception import MovieAlreadyavailableError,MovieNotAvailableerror,TicketsNotAvailableError
class MovieInventory:
    all_movies=[]
    @staticmethod
    def add_movie(movie_obj):
        try:
            if movie_obj.movie_name not in [str(m.values()) for m in MovieInventory.all_movies]:
                movie={
                    "movie_name":movie_obj.movie_name,
                    "available_tickets":movie_obj.available_tickets,
                    "ticket_price":movie_obj.ticket_price
                }
                MovieInventory.all_movies.append(movie)
                return "movie added"
            else:
                raise MovieAlreadyavailableError("Movie already exist")
        except MovieAlreadyavailableError as e:
            print(e) 
    @staticmethod
    def show_movie_inventory():
        return MovieInventory.all_movies
    @staticmethod
    def find_movie(movie_name):
        try:
            if any(d['movie_name']==movie_name for d in MovieInventory.all_movies):
                return "Movie Available"
            else:
                raise MovieNotAvailableerror("movie not available")
        except MovieNotAvailableerror as e:
            print(e)
    @staticmethod
    def book_movie_tickets(movie_name,tickets):
        try:
            if any(d['movie_name']==movie_name for d in MovieInventory.all_movies):
                for d in MovieInventory.all_movies:
                    try:
                        if d['movie_name']==movie_name and d['available_tickets']>=tickets:
                            d['available_tickets']-=tickets
                            total_cost=tickets*d['ticket_price']
                            return total_cost 
                        elif d['movie_name']==movie_name:
                            raise TicketsNotAvailableError("Insufficient movie tickets")
                    except TicketsNotAvailableError as e:
                        print(e)
            else:
                raise MovieNotAvailableerror("movie not available")
        except MovieAlreadyavailableError as e:
            print(e)





