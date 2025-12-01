from movie import Movie
from inventory import MovieInventory

class MainClass:
    def read_movie_details():
        print("==========entering movie details==============")
        n=int(input("Enter the number of movies to be added"))
        for i in range(n):
            movie_name=input("Enter the movie name")
            aval_tickets=int(input("Enter the number of tickets available"))
            ticket_price=float(input("Enter the price of the ticket"))
            m=Movie(movie_name,aval_tickets,ticket_price)
            message=MovieInventory.add_movie(m)
            print(message)
    def show_inventory():
        print("========showing inventory======")
        lst=MovieInventory.show_movie_inventory()
        for d in lst:
            for k,v in d.items():
                print(k,v)
    def search_movie():
        print("=======search movie==========")
        movie_name=input("Enter movie name?")
        status=MovieInventory.find_movie(movie_name)
        return status
    def book_tickets():
        print("===========Booking Movie Tickets============")
        movie_name=input("Enter movie name?")
        tickets=int(input("Enter no of tickets"))
        total_cost=MovieInventory.book_movie_tickets(movie_name,tickets)
        if total_cost !=None:
            print("Movie Tickets booked and total cost RS:",total_cost)

if __name__=="__main__":
      while True:
        MainClass.read_movie_details()
        MainClass.show_inventory()
        status=MainClass.search_movie()
        print(status)
        if status=="Movie Available":
            MainClass.book_tickets()
        n=int(input("To exit press 0 to continue press 1:\n"))
        if n==0:
            break  