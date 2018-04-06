import media
import fresh_tomatoes

# Movie instances used by fresh_tomatoes
dead_poets = media.Movie(
    "Dead Poets Society",
    "He was their inspiration. He made their lives extraordinary.",
    "https://images-na.ssl-images-amazon.com/images/I/515v-4X8ZLL.jpg",
    "https://www.youtube.com/watch?v=wrBk780aOis"
)

lord_rings = media.Movie(
    "The Fellowship of the Ring",
    "One Ring To Rule Them All.",
    "https://images-na.ssl-images-amazon.com/images/I/51Qvs9i5a%2BL.jpg",
    "https://www.youtube.com/watch?v=qyquczkXgPc"
)

pirates = media.Movie(
    "The Pirates of the Caribbean",
    "Prepare to be blown out of the water.",
    "https://images-na.ssl-images-amazon.com/images/I/51fX40gGdXL.jpg",
    "https://www.youtube.com/watch?v=G7z74BvLWUg"
)

my_movies = [dead_poets, lord_rings, pirates]
fresh_tomatoes.open_movies_page(my_movies)
