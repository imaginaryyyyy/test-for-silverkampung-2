import streamlit as st
import datetime as dt

#Kaiser's function to read a .json file
def ReadFromJson(fp, *locations):
  with open(fp,"r") as f:
    myFile = json.load(f)
  return reduce(operator.getitem, locations, myFile)

st.title("Silver Kampong")

#e.g ReadFromJson(file.json, "movies")

#Movies dictionary
movies = [
        {"title": "My Children", "desc": "A man who values his children", "showtimes": "9.00 AM", "halls": "Cinema Hall 1", "photos": "https://images.pexels.com/photos/15914002/pexels-photo-15914002.jpeg", "date": "2026-08-26"},
        {"title": "My Struggle", "desc": "Is this source reliable?", "showtimes": "12.00 PM", "halls": "Cinema Hall 2", "photos": "https://images.pexels.com/photos/9804995/pexels-photo-9804995.jpeg", "date": "2026-08-27"},
        {"title": "-man", "desc": "-I am powerless", "showtimes": "3.00 PM", "halls": "Cinema Hall 3", "photos": "https://images.pexels.com/photos/28344947/pexels-photo-28344947.jpeg", "date": "2026-08-28"}]

#Setting the filters selection
filters = st.selectbox("", options=["All", "Showtimes", "Halls", "Date"], index=0)

filtered_movies = []


if filters == "All":
    filtered_movies = movies

elif filters == "Date":
    selected_date = st.date_input("Select Date", max_value=dt.date(2026, 12, 31), format="DD/MM/YYYY")
    date_str = str(selected_date)
    for movie in movies:
        if movie["date"] == date_str:
            filtered_movies.append(movie)

elif filters == "Showtimes":
    all_times = []
    for movie in movies:
        if movie["showtimes"] not in all_times:
            all_times.append(movie["showtimes"])
    showtimes_filter = st.pills("", options=all_times, default=all_times, selection_mode="multi")

    for movie in movies:
        if movie["showtimes"] in showtimes_filter:
            filtered_movies.append(movie)


elif filters == "Halls":
    all_halls = []
    for movie in movies:
        if movie["halls"] not in all_halls:
            all_halls.append(movie["halls"])
    halls_filter = st.pills("", options=all_halls, default=all_halls, selection_mode="multi")

    for movie in movies:
        if movie["halls"] in halls_filter:
            filtered_movies.append(movie)

if filtered_movies:
    cols = st.columns(len(filtered_movies), border=True, vertical_alignment="center")
    for i in range(len(filtered_movies)):
        movie = filtered_movies[i]
        col = cols[i]
        with col:
            st.subheader(movie["title"])
            st.caption(movie["desc"])
            st.image(movie["photos"])
            if filters != "Date":
                st.write("Date: ")
                st.button(movie["date"])
            if filters != "Showtimes"
                st.write("Showtimes: ")
                st.button(movie["showtimes"], key=f"{movie['title']}, {movie["showtimes"]}")
            if filters != "Halls":
                st.write("Halls: ")
                st.button(movie["halls"], key=f"{movie['title']}, {movie['halls']}")
else:
    st.info("There are no movies. Please seek help as soon as possible.")
    st.balloons()
